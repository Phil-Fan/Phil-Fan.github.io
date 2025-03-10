# Mkdocs
[material文档](https://squidfunk.github.io/mkdocs-material/)
## Markdown



[Markdown 教程-常见Markdown错误和解决方法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/672261576)

### 方块
```markdown
!!! info

!!! inline info ""
```

### 列表
```
- [x] finished
- [ ] not finished
```




### 代码块
[Code blocks(代码块) - Material for MkDocs](https://wdk-docs.github.io/mkdocs-material-docs/reference/code-blocks/#annotations-with-numbers)

`hl_lines="2 3"` 高亮行

`linenums="1"` 显示行号

`title="bubble_sort.py"` 显示文件名字


### Jupyter Notebook
使用mkdocs-jupyter插件可以支持jupyter notebook文件
[mkdocs-jupyter](https://pypi.org/project/mkdocs-jupyter/)
[Jupytext demo (.py) - mkdocs-jupyter demo](https://mkdocs-jupyter.danielfrg.com/demo-script/)

[mkdocs-jupyter/demo/mkdocs.yml at main · danielfrg/mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter/blob/main/demo/mkdocs.yml)


```shell
pip install mkdocs-jupyter
```


```yml title="mkdocs.yml" hl_lines="11" linenums="1"
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
        custom_mathjax_url: "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"
```

!!! bug "遇到的问题"
    1. 无法显示数学公式（解决方法：加上了js文件）
    2. toc配置与之前的逻辑不同，导致自动配置123的时候出现错误
    3. 奇怪的路径问题

    ```
      DeprecationWarning: Jupyter is migrating its paths to use standard platformdirs
      given by the platformdirs library.  To remove this warning and
      see the appropriate new directories, set the environment variable
      `JUPYTER_PLATFORM_DIRS=1` and then run `jupyter --paths`.
      The use of platformdirs will be the default in `jupyter_core` v6
    ```

    [DeprecationWarning: Jupyter is migrating its paths to use standard platformdirs · Issue #148 · danielfrg/mkdocs-jupyter](https://github.com/danielfrg/mkdocs-jupyter/issues/148)


如果想要实现material中的某些功能，需要自己写html代码

```html
<details class="tip">
    <summary>Extra: What are latent variables?</summary>
    <p><br>
    If you go about exploring any paper talking about Variational Inference, then most certainly, the papers mention about latent variables instead of parameters. The parameters are fixed quantities for the model whereas latent variables are  <strong>unobserved</strong> quantities of the model conditioned on parameters. Also, we model parameters by probability distributions. For simplicity, let's consider the running terminology of  <strong>parameters </strong> only.
    </p>
</details>
```
  

```html
<div class="admonition success">
    <p class="admonition-title">Success</p>
    <p>
        The above ELBO equation is the final one which needs to be optimized.
    </p>
</div>
```

### 嵌入b站视频


1.打开B站的视频
2.点击“分享”按钮，获取“嵌入代码”：B站视频的下一行，点击“分享”按钮，下方弹出分享页面。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241031230641.png)

禁用方法很简单，就是在视频 url 链接最后加上 autoplay=0。例如：

```html title="禁止自动播放"
<iframe src="//player.bilibili.com/player.html?aid=951910057&bvid=BV1zs4y177sv&cid=1078968085&page=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="500" height="300"> </iframe>
```


| 参数用途                         | 参数名      | 使用方法          |
|----------------------------------|-------------|-------------------|
| 是否自动播放(默认否)            | `autoplay`    | 1: 开启, 0: 关闭  |
| 默认弹幕开关(默认开启)          | `danmaku`    | 1: 开启, 0: 关闭  |
| 是否默认静音(默认否)            | `muted`       | 1: 开启, 0: 关闭  |
| 一键静音按钮是否显示(默认不显示) | `hasMuteButton` | 1: 开启, 0: 关闭  |
| 视频封面下方是否显示播放量弹幕量等信息(默认显示) | `hideCoverInfo` | 1: 开启, 0: 关闭  |
| 是否隐藏弹幕按钮(默认不隐藏)    | `hideDanmakuButton` | 1: 开启, 0: 关闭 |
| 是否隐藏全屏按钮(默认显示)      | `noFullScreenButton` | 1: 开启, 0: 关闭 |
| 是否开始记忆播放(默认开启)      | `fw`          | 1: 开启, 0: 关闭  |
| 默认开始时间(默认0)             | `t`           | 直接填写数值, 单位秒 |
| 是否显示高清(默认否)            | `highQuality` | 1: 开启, 0: 关闭 (貌似是无用的, 各位可以试试) |


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

!!! question "这是 question 类型的提示框"
    这是一个问题，请回答！

!!! warning "这是 warning 类型的提示框"
    注意！注意！注意！

!!! success "这是 success 类型的提示框"
    恭喜你，完成了一个任务！

!!! example "这是 example 类型的提示框"

!!! info "这是 info 类型的提示框"

!!! abstract "这是 abstract 类型的提示框"

!!! quote "这是 quote 类型的提示框"


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


picgo中的设置如下

1. 设定`keyid`，就是创建用户的`AccessKey ID`，
2. `KeySecret` 就是`AccessKeySecret`
3. 存储空间名就是创建Bucket的名字，存储区域也是创建时设定的， 忘记的可以通过Bucket概览查看，如下图所示：
4. 存储路径默认设置img/即可
5. 如果自己有已经备案的域名，可以填写设定自定义域名，如果没有不填即可。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240813014140.png)

#### 图床的迁移

[利用 PicGo 快速迁移 Gitee 图床外链图片到服务器-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1975652)


### 解决列表无法嵌套的问题

> 来自 [解决 mkdocs 不支持无序列表嵌套 - SegmentFault 思否](https://segmentfault.com/a/1190000042842937)

安装 `mdx_truly_sane_lists` 

```shell
pip install mdx_truly_sane_lists
```

然后在 `mkdoc.yml` 的 `markdown_extensions` 添加 `mdx_truly_sane_lists` 就好了



### 显示音乐符号

关于安装lilypond

LilyPond (荷花池) 是一个音乐雕版软件，致力产生最高质量的乐谱。它把传统音乐雕版印刷的美学，呈现在计算机打印的乐谱上。LilyPond 是自由软件，也是 GNU Project 的一部分。

[Download (LilyPond – 人人的乐谱软件)](https://lilypond.org/download.zh.html)

下载之后，是没有安装的，但是需要将其添加到环境变量中.win菜单搜索`查看高级环境设置`,在path中添加`lilypond\bin\`的路径

编译

```shell
lilypond -o output music.ly
```

[LilyPond 学习手册: LilyPond — 学习手册](https://lilypond.org/doc/v2.23/Documentation/learning/index)

[关于在 Markdown 中描述音乐符号](https://blog.twofei.com/1425/)



[Lilypond in Markdown](https://lilypond-in-markdown.netlify.app/)


[Render LilyPond in Markdown](https://pianomanfrazier.com/post/lilypond-in-markdown/)

[uliska/markdown-lilypond： 支持 LilyPond（符号软件）输入的 MkDocs 插件](https://github.com/uliska/markdown-lilypond)

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


