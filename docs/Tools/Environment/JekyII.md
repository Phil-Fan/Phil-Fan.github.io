---
comments: true
---
# Jekyll

[Jekyll • 简单静态博客网站生成器 - 将纯文本转换为静态博客网站](https://jekyllcn.com/)

## windows 安装

[Windows 系统上安装 Jekyll（简单详细教程） - pergrand - 博客园](https://www.cnblogs.com/pergrand/p/12875597.html)

### 安装 ruby

[Downloads](https://rubyinstaller.org/downloads/)

```shell
ruby -v
```

### rubygems 
[下载 RubyGems](https://rubygems.org/pages/download)

下载后解压到任意路径。打开Windows的cmd界面，输入命令： 
```shell
$ cd 解压的路径
```

### 切换镜像源

```shell
gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/
```
```shell title="验证"
gem sources -l
```

```shell title="验证"
*** CURRENT SOURCES ***
https://gems.ruby-china.com/
```

### 安装`Jekyll`
```shell
gem install jekyll
```

!!! bug "ERROR: Could not find a valid gem 'sass-embedded' (~> 1.54) (required by 'jekyll' (>= 0)) in any repository ERROR: Possible alternatives: sass-embedded"
    这一步报错了，所以再把镜像源切换回官方的

    ```shell
    gem sources -a https://rubygems.org/
    ```

### 安装`jekyll-paginate`

```shell
gem install jekyll-paginate
```

验证 jekyll :  
```shell
jekyll -v
```

### 安装 Bundler
安装 一个名为 Bundler 的程序 —— 用于自动安装其他所需的程序
```shell
gem install bundler
```
### 本地启动服务
在命令行中切换到你的网站仓库内
```shell
bundle install（这一步不要）

jekyll serve 
```

### 查看网站
 
`127.0.0.1:4000` 或 `localhost:4000`

注意：如端口被占用修改端口 

```shell
jekyll serve -P 5555
```

## 极简风个人网站搭建


[academicpages](https://github.com/academicpages/academicpages.github.io)



## 个人网站参考


[Wanjia Zhao](https://wanjiazhao1203.github.io/#academicservices)
[Leo / Zeqing Yuan](https://leoyuan.site/)