# 功能： 渲染.excalidraw文件，支持亮/暗色
# 改编自 https://github.com/qdeli187/mkdocs-excalidraw/tree/v0.3.3
# 下载 vscode excalidraw插件，可以实现vscode内编辑

# 原代码遵循 Apache License 2.0，原作者 qdeli187，本代码同样遵循 Apache License

# 本代码修改部分：移植成为hooks函数格式

import re
import os
from pathlib import Path
from bs4 import BeautifulSoup
# pip install beautifulsoup4==4.13.5


# 匹配 Markdown 中的 excalidraw 图片引用
EXCALIDRAW_PATTERN = r'!\[.*?\]\((.*?\.excalidraw)\)'

# Excalidraw 依赖
EXCALIDRAW_CSS = "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.css"
EXCALIDRAW_JS = "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.js"

def _load_renderer_js():
    """加载 excalidraw-renderer.js 文件"""
    js_path = os.path.join(
        os.path.dirname(__file__),
        'static',
        'excalidraw-renderer.js'
    )
    with open(js_path, 'r') as f:
        return f.read()

def on_page_markdown(markdown, **kwargs):
    """
    处理 Markdown 中的 excalidraw 图片引用
    将 ![](*.excalidraw) 格式的引用转换为 <excalidraw-renderer> 标签
    """
    page = kwargs['page']
    config = kwargs['config']
    
    # 查找所有 excalidraw 图片引用
    matches = re.finditer(EXCALIDRAW_PATTERN, markdown)
    has_excalidraw = False
    
    # 替换所有匹配项
    result = markdown
    for match in re.finditer(EXCALIDRAW_PATTERN, markdown):
        has_excalidraw = True
        # 获取图片路径
        excalidraw_path = match.group(1)
        
        # 构建相对于文档根目录的路径
        if not excalidraw_path.startswith('/'):
            # 如果是相对路径，转换为相对于文档根目录的路径
            page_dir = os.path.dirname(page.file.src_path)
            excalidraw_path = os.path.normpath(os.path.join(page_dir, excalidraw_path))
        
        # 替换为 excalidraw-renderer 标签
        old_text = match.group(0)
        new_text = f'<excalidraw-renderer src="{excalidraw_path}"></excalidraw-renderer>'
        result = result.replace(old_text, new_text)
        print(f"Replaced Excalidraw reference: {old_text} -> {new_text}")
    
    # 如果没有 excalidraw 引用，直接返回原始内容
    if not has_excalidraw:
        return markdown
    
    return result

def on_post_page(output, **kwargs):
    """
    在页面渲染后注入必要的 JS 和 CSS
    """
    if "excalidraw-renderer" not in output:
        return output
        
    soup = BeautifulSoup(output, 'html.parser')
    
    # 添加 Excalidraw CSS
    css_tag = soup.new_tag('link')
    css_tag["rel"] = "stylesheet"
    css_tag["href"] = EXCALIDRAW_CSS
    
    # 添加 Excalidraw JS
    js_tag = soup.new_tag('script')
    js_tag['src'] = EXCALIDRAW_JS
    
    # 添加 renderer 组件
    renderer_js = soup.new_tag('script')
    renderer_js['type'] = "module"
    renderer_js.string = _load_renderer_js()
    
    # 将标签添加到页面
    if soup.head is not None:
        soup.head.extend([css_tag, js_tag, renderer_js])
    else:
        soup.extend([css_tag, js_tag, renderer_js])
    
    return str(soup)