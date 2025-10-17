import os
import re
import requests
import subprocess
from tqdm import tqdm
from PIL import Image

def sanitize_filename(filename):
    # 移除url中的无效字符
    return re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)

def ensure_dir_exists(path):
    os.makedirs(path, exist_ok=True)

def is_image_url(url):
    # 检查结尾是否常见图片格式
    url_no_query = url.split('#')[0].split('?')[0].lower()
    return url_no_query.endswith(('.png', '.jpg', '.jpeg', '.gif', '.JPG', '.PNG', '.JPEG', '.GIF', '.webp', '.svg', '.tiff'))

def is_convertible_to_webp(path):
    ext = os.path.splitext(path)[1].lower()
    # 不转换svg/tiff/gif/webp本身
    return ext in ('.png', '.jpg', '.jpeg', '.JPG', '.PNG', '.JPEG')

def convert_to_webp(image_path):
    # 返回新 webp 路径，若失败返回None
    try:
        img = Image.open(image_path)
        ext = os.path.splitext(image_path)[1].lower()
        # 透明通道处理：有透明度的图片用lossless
        save_kwargs = {}
        if img.mode in ['RGBA', 'LA'] or (img.mode == 'P' and 'transparency' in img.info):
            save_kwargs['lossless'] = True
        webp_path = image_path.rsplit('.', 1)[0] + '.webp'
        img.save(webp_path, 'webp', quality=85, **save_kwargs)
        img.close()
        os.remove(image_path)
        return webp_path
    except Exception as e:
        print(f"转换为webp失败: {image_path}, {e}")
        return None

def oss_upload(local_path, oss_path):
    # 调用ossutil上传图片，如果ossutil未安装，这条命令会报错
    try:
        subprocess.run(['ossutil', 'cp', local_path, oss_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ossutil 上传失败: {local_path} -> {oss_path}\n{e}")
        return False

def find_image_refs_in_md(root_path):
    # 匹配 Markdown 图片引用的正则表达式: ![alt](url)
    img_pattern = re.compile(r'!\[[^\]]*\]\((.*?)\)')
    # 支持 HTML 图片标签: <img src="xxx" ...>
    html_img_pattern = re.compile(r'<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)

    net_img_count = 0
    local_img_count = 0
    local_img_total_size = 0
    local_img_files = set()
    downloaded_net_imgs = set()

    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.lower().endswith('.md'):
                md_files.append(os.path.join(dirpath, filename))

    for full_path in tqdm(md_files, desc="处理Markdown文件"):
        dirpath = os.path.dirname(full_path)
        filename = os.path.basename(full_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # 匹配 Markdown 和 HTML 图片
            md_imgs = img_pattern.findall(content)
            html_imgs = html_img_pattern.findall(content)
            all_imgs = set(
                img for img in (md_imgs + html_imgs)
                if is_image_url(img)
            )
            # 网络图片
            net_imgs = [img for img in all_imgs if img.startswith('http://') or img.startswith('https://')]

            # 用于内容替换
            replace_map = {}

            # =============== 网络图片保持原处理 =================
            for img_url in tqdm(net_imgs, leave=False, desc=f"下载/替换网络图片: {filename}"):
                net_img_count += 1
                try:
                    # assets 目录
                    md_basename = os.path.splitext(filename)[0]
                    assets_dir = os.path.join(dirpath, "assets", f"{md_basename}.assets")
                    ensure_dir_exists(assets_dir)
                    img_url_no_query = img_url.split('#')[0]
                    base_name = os.path.basename(img_url_no_query.split("?")[0])
                    local_img_name = sanitize_filename(base_name)
                    local_img_path = os.path.join(assets_dir, local_img_name)

                    # 用于 md 内部的本地相对路径
                    rel_assets_dir = os.path.relpath(assets_dir, dirpath)
                    rel_local_img_path = os.path.join(rel_assets_dir, local_img_name).replace("\\", "/")

                    net_img_key = (img_url, full_path)

                    if os.path.exists(local_img_path):
                        replace_map[img_url] = rel_local_img_path
                        downloaded_net_imgs.add(net_img_key)
                        continue

                    try:
                        resp = requests.get(img_url, timeout=10)
                        if resp.status_code == 200:
                            with open(local_img_path, "wb") as img_f:
                                img_f.write(resp.content)
                            replace_map[img_url] = rel_local_img_path
                            downloaded_net_imgs.add(net_img_key)
                        else:
                            print(f"\n下载失败: {img_url} -> HTTP {resp.status_code}")
                    except Exception as ex:
                        print(f"\n下载图片出错: {img_url} 于 {full_path}: {ex}")
                except Exception as e:
                    print(f"\n下载/替换图片异常: {img_url} 于 {full_path}: {e}")

            # =============== 本地图片webp转换并oss上传处理 =================
            local_imgs_set = all_imgs - set(net_imgs)
            for img_url in local_imgs_set:
                local_img_count += 1
                img_path = img_url
                img_path = img_path.split('#')[0].split('?')[0]
                abs_img_path = img_path
                if not os.path.isabs(img_path):
                    abs_img_path = os.path.normpath(os.path.join(dirpath, img_path))

                if os.path.isfile(abs_img_path):
                    if abs_img_path not in local_img_files:
                        file_size = os.path.getsize(abs_img_path)
                        local_img_total_size += file_size
                        local_img_files.add(abs_img_path)

                    # 检查是否需要webp转换
                    ext = os.path.splitext(abs_img_path)[1].lower()
                    final_img_path = abs_img_path
                    if ext != ".webp" and is_convertible_to_webp(abs_img_path):
                        webp_path = convert_to_webp(abs_img_path)
                        if webp_path:
                            final_img_path = webp_path

                    oss_base = f'oss://philfan-pic/web_pic/'
                    # oss文件名：从文件路径生成唯一且有辨识度的名字
                    # 用md相对文档根路径 + "__" + 文件名，避免冲突
                    # root_path.../some/xxx.md
                    rel_root_img_path = os.path.relpath(final_img_path, root_path)
                    oss_name = sanitize_filename(rel_root_img_path.replace(os.sep, "__"))
                    oss_ext = os.path.splitext(final_img_path)[1].lower()
                    # 上传
                    oss_url = oss_base + oss_name
                    if not oss_url.endswith(oss_ext):
                        oss_url = oss_url + oss_ext
                    # 只有这次上传一次，防止重复上传
                    if not getattr(find_image_refs_in_md, 'uploaded_imgs', None):
                        find_image_refs_in_md.uploaded_imgs = set()
                    already_uploaded_key = (final_img_path, oss_url)
                    if already_uploaded_key not in find_image_refs_in_md.uploaded_imgs:
                        ok = oss_upload(final_img_path, oss_url)
                        find_image_refs_in_md.uploaded_imgs.add(already_uploaded_key)
                    # oss 访问url
                    oss_http_url = oss_url.replace('oss://philfan-pic/', 'https://philfan-pic.oss-cn-beijing.aliyuncs.com/')
                    # 只替换精确img_url字符串（保留相对路径和./前缀的兼容）
                    replace_map[img_url] = oss_http_url
                    if not img_url.startswith("./") and "./"+img_url in all_imgs:
                        replace_map["./"+img_url] = oss_http_url

            # ================= 替换内容并写回 ===================
            content_changed = content
            if replace_map:
                # Markdown
                content_changed = re.sub(
                    r'!\[[^\]]*\]\((.*?)\)',
                    lambda m: f'![]({replace_map.get(m.group(1), m.group(1))})',
                    content_changed
                )
                # HTML
                content_changed = re.sub(
                    r'(<img[^>]+src=["\'])(.*?)(["\'])',
                    lambda m: m.group(1) + replace_map.get(m.group(2), m.group(2)) + m.group(3),
                    content_changed
                )
                if content_changed != content:
                    with open(full_path, 'w', encoding='utf-8') as fw:
                        fw.write(content_changed)

    print(f"网络路径图片数量: {net_img_count}")
    print(f"本地路径图片数量: {local_img_count}")
    print(f"本地图片实际文件数（去重）: {len(local_img_files)}")
    print(f"本地图片总大小: {local_img_total_size / 1024/1024:.2f} MB")

# 示例调用
find_image_refs_in_md('../docs') # 你可以替换为你的文档根目录
