#!/bin/zsh

# 使用webp转换图片为webp格式，以压缩体积；不支持svg
# brew install webp

# vscode 当中 搜索
# (assets/[^)\s]+?)\.(png|jpg|jpeg|JPG|PNG)
# 改成
# $1.webp

# 开启递归 glob
setopt globstar null_glob

# 使用第一个参数作为起始路径，如果没有参数则使用当前路径
start_path="${1:-.}"
cd "$start_path"

for f in **/*.(jpg|JPG|jpeg|JPEG|png|PNG|svg); do
    [[ -f "$f" ]] || continue
    out="${f%.*}.webp"
    echo "Converting: $f -> $out"
    if cwebp -q 85 "$f" -o "$out"; then
        echo "Removing original file: $f"
        rm "$f"
    else
        echo "Conversion failed for: $f"
        echo "Keeping original file"
    fi
done
