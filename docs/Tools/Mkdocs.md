# Mkdocs

## Markdown



[Markdown 教程-常见Markdown错误和解决方法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/672261576)


### 代码块
[Code blocks(代码块) - Material for MkDocs](https://wdk-docs.github.io/mkdocs-material-docs/reference/code-blocks/#annotations-with-numbers)

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

[mkdocs-material集成评论系统 - 知识库 (geodoer.github.io)](https://geodoer.github.io/Z-工具/博客相关工具/mkdocs/mkdocs-material/评论系统/#commentshtml)



```
<script src="https://giscus.app/client.js"
        data-repo="Phil-Fan/Phil-Fan.github.io"
        data-repo-id="R_kgDOLJH-6w"
        data-category="General"
        data-category-id="DIC_kwDOLJH-684Ccv_n"
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


