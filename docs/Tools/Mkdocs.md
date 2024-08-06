# Mkdocs

## Markdown



[Markdown 教程-常见Markdown错误和解决方法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/672261576)


### 代码块
[Code blocks(代码块) - Material for MkDocs](https://wdk-docs.github.io/mkdocs-material-docs/reference/code-blocks/#annotations-with-numbers)

`hl_lines="2 3"` 高亮行

`linenums="1"` 显示行号

`title="bubble_sort.py"` 显示文件名字


### Jupyter Notebook
使用mkdocs-jupyter插件可以支持jupyter notebook文件
[mkdocs-jupyter](https://pypi.org/project/mkdocs-jupyter/)
[Jupytext demo (.py) - mkdocs-jupyter demo](https://mkdocs-jupyter.danielfrg.com/demo-script/)

```shell
pip install mkdocs-jupyter
```


```yml
nav:
    - Home: index.md
    - Notebook page: notebook.ipynb
    - Python file: python_script.py
plugins:
    - mkdocs-jupyter
        execute: true
        kernel_name: python3
        theme: dark
        include_source: True
```





## 配置

### Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

??? note "安装代码" 
	```Shell
    pip install mkdocs
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    pip install mkdocs-git-revision-date-localized-plugin
    pip install mkdocs-statistics-plugin
    pip install mkdocs-heti-plugin
	```



!!! failure "这是 failure 类型的提示框" 
	注意`extension`不要拼成`extention`！！

!!! bug "这是 bug 类型的提示框" 
    发现一个 bug，请尽快修复！

!!! tip "tip"

!!! note "note"

### 插件

#### Github评论

- 安装[giscus](https://giscus.app/zh-CN)
1. 安装 giscus GitHub App。这一步只需要在 GitHub 官网上点击安装即可。
2. 访问 giscus 官网，配置与 giscus 评论系统关联的 GitHub 仓库。

请确保：
- 该仓库是**公开**的，否则访客将无法查看 Discussions。
- **giscus app** 已安装，否则访客将无法评论和回应。
- Discussions 功能已在你的仓库中启用。

在`mkdocs.yml`中添加如下配置

```yml linenums="1" hl_lines="3"
theme:
  name: material
  custom_dir: overrides  #主要是这一行
```

访问[giscus](https://giscus.app/)网站，并通过网站上的配置工具生成代码段。复制此代码段，下面的步骤要用
复制如下面格式的代码到`overrides/comments.html`文件中

```html
<script src="https://giscus.app/client.js"
        data-repo="Phil-Fan/Phil-Fan.github.io"
        data-repo-id=""
        data-category="General"
        data-category-id=""
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="dark"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
```

```html hl_line="5"
{% if page.meta.comments %}
  <h2 id="__comments">{{ lang.t("meta.comments") }}</h2>

  <!-- Insert generated snippet here -->
  <!-- 在这里粘贴刚才获得代码段 -->
  <!-- ... -->

  <!-- Synchronize Giscus theme with palette -->
  <script>
    var giscus = document.querySelector("script[src*=giscus]")

    /* Set palette on initial load */
    var palette = __md_get("__palette")
    if (palette && typeof palette.color === "object") {
      var theme = palette.color.scheme === "slate" ? "dark" : "light"
      giscus.setAttribute("data-theme", theme) 
    }

    /* Register event handlers after documented loaded */
    document.addEventListener("DOMContentLoaded", function() {
      var ref = document.querySelector("[data-md-component=palette]")
      ref.addEventListener("change", function() {
        var palette = __md_get("__palette")
        if (palette && typeof palette.color === "object") {
          var theme = palette.color.scheme === "slate" ? "dark" : "light"

          /* Instruct Giscus to change theme */
          var frame = document.querySelector(".giscus-frame")
          frame.contentWindow.postMessage(
            { giscus: { setConfig: { theme } } },
            "https://giscus.app"
          )
        }
      })
    })
  </script>
{% endif %}
```


**一个页面单独添加**

在每个文档头前添加comments: true
```markdown
---
comments: true
---
```


**所有页面**

在`mkdocs.yml`的插件中添加

```yml
plugins:
  - comments
```


[mkdocs-material集成评论系统 - 知识库 (geodoer.github.io)](https://geodoer.github.io/Z-工具/博客相关工具/mkdocs/mkdocs-material/评论系统/#commentshtml)
[为Mkdocs网站添加评论系统（以giscus为例）\_giscus mkdocs-CSDN博客](https://blog.csdn.net/m0_63203517/article/details/133819706)


### 图床的配置与更换

原先配置的时候使用的是gitee的仓库配置

但在发布网站后发现所有的图片都无法显示

#### 原因

[查询资料](https://blog.csdn.net/qq_45173404/article/details/123759688)后发现是Gitee防盗链的原因

>发现图片请求的过程与上面不同，请求头中多了一个`Referer`字段，也就是我自己的gitee地址。
>应该是Gitee添加了防盗链机制，当我们通过直接访问存储在Gitee上的图片时，Http请求头没有Referer字段，所以被Gitee服务器当作黑名单而拒绝响应。而前面我们通过Gitee Page部署的Hexo博客请求时，由于代码都托管在Gitee上，在加载所有图片的时候都附加了Referer字段指向Gitee，相当于被Gitee服务器看作白名单因而可以访问。


#### 解决办法

将图像存储更改为阿里云OSS，根据[教程](https://zhuanlan.zhihu.com/p/104152479)做出以下操作

- 购买阿里云oss服务
- 创建用户，记录id和密码
- 将图床中的所有图片迁移到阿里云当中
- 更换picgo中服务
- 更换`.md`中所有图片的链接



## 发布

发布也遇到了好几个坑

[GitHub Pages 文档自动化部署 - MkDocs - Arisa | Blog](https://blog.arisa.moe/blog/2022/220407-github-pages/#vcs)

[github pages绑定域名-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1454059)

- 编写`workflow`文件

在仓库上方有actions选项，点击new workflow，我这里选择了自己编写的workflow文件，貌似也有针对Mkdocs的模板

```yml
name: deploy

on:
  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0    # for mkdocs-git-revision-date-localized-plugin
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: pip install -r requirements.txt
      - name: Create CNAME file
        run: echo "www.philfan.cn" > docs/CNAME   # Adjust the path if your configuration is different
      - run: mkdocs gh-deploy --force
```

- 设置deploy from branch

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240707225202.png)

- 设置自定义域名
将域名填入`CNAME`文件中，然后打开仓库的设置界面，在cumtom domain 中设置好自己的域名


