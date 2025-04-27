# Node.js

## 基础简介
npm:  nodejs 下的包管理器。

webpack: 它主要用途是通过CommonJS 的语法把所有浏览器端需要发布的静态资源作相应的准备，比如资源的合并和打包。

vue-cli: 用户生成Vue工程模板。（帮你快速开始一个vue的项目，也就是给你一套vue的结构，包含基础的依赖库，只需要npm install 就可以安装。

reveal.js: 用于制作演示文稿。

reveal-md: 用于将markdown文件转换为reveal.js的演示文稿。


## 安装

[Node.js — Download Node.js®](https://nodejs.org/en/download)

使用这个网站上面的安装的指令


### nodejs
[windows安装npm教程\_npm 安装-CSDN博客](https://blog.csdn.net/zhouyan8603/article/details/109039732)



[Node.js — Run JavaScript Everywhere](https://nodejs.org/en/)

安装以后可以把nodejs的本地仓库从c盘移出来

```shell
npm config set prefix "<path>\nodejs\node_global"
npm config set cache "<path>\nodejs\node_cache"
```


```shell title="cmd验证安装"
npm -v
npm info vue
```

```shell title="配置镜像站点"
npm config set registry=http://registry.npm.taobao.org 
```

```
npm install vue -g
npm install vue-router -g
```

```shell title="创建vue工程"
vue init webpack vue01
cd vue01
npm install
npm run dev

npm run build
```

成功界面，提示打开地址http://localhost:8080

## 卸载

```
sudo npm uninstall npm- g
```

```shell
cd /usr/local/lib/node_modules/

rm -rf npm
```

```shell
sudo apt-get remove nodejs
sudo apt-get remove npm
sudo apt-get remove node
```

```shell
node -v
npm -v 
```










### reveal-md
reveal.js 是一个开源的 HTML 框架，用于创建交互式演示文稿。

[官方网站 | reveal.js](https://revealjs.com/)

[TonyCrane 的模板](https://github.com/TonyCrane/slide-template?tab=readme-ov-file)
```shell
npm install -g reveal-md
```

## reveal-md 使用
[MartenBE/mkslides: Use mkslides to easily turn markdown files into beautiful slides using the power of Reveal.js!](https://github.com/MartenBE/mkslides)

[使用 reveal-md 来写 Slides - Isshiki修's Notebook](https://note.isshikih.top/others/reveal-md2Slides/)

```shell
## 最基础的命令，根据 Markdown 文件在本地 1948 端口生成 Slides 服务。
$ reveal-md your-md-file.md

## 为了实现在线部署，需要导出为静态资源。
$ reveal-md your-md-file.md --static your-static-dir
```


```markdown
---
separator: <!--s-->
verticalSeparator: <!--v-->
---
```

### reveal-md 模版


[TonyCrane/slide-template: TonyCrane's slide template for reveal-md](https://github.com/TonyCrane/slide-template)


```shell title="开启本地实时预览"
make  # or make live
```

```shell title="构建静态文件"
make build
```


- 生成 pdf 版：在 url 后面加上 `?print-pdf` 使用浏览器打印