# 研究方法论

!!! note "三步走：通过学习模仿➡️迭代更新效率➡️形成自己的方法论"

[pengsida/learning_research: 本人的科研经验](https://github.com/pengsida/learning_research?tab=readme-ov-file)

limu [博士这五年 - 知乎](https://zhuanlan.zhihu.com/p/25099638)

[Principles of Effective Research – Michael Nielsen](https://michaelnielsen.org/blog/principles-of-effective-research/)

[An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html)

[You and Your Research, by Richard Hamming - Sam Altman](https://blog.samaltman.com/you-and-your-research)

[A Survival Guide to a PhD](https://karpathy.github.io/2016/09/07/phd/)

[研究生期间如何成为科研大佬？ - 知乎](https://www.zhihu.com/question/458196603/answer/3266020661)

[Ways to Fail a PhD](https://matt.might.net/articles/ways-to-fail-a-phd/)

## Zotero
[Zotero](https://www.zotero.org/),[Zotero 中文社区 | Zotero 中文维护小组](https://zotero-chinese.com/)
[【ZOTERO】从安装到使用 个人向整理全集（含4篇超长pdf！！） - CC98论坛](https://www.cc98.org/topic/5880486)
[对文献管理&阅读感到头大？——Zotero介绍以及我的文献阅读工作流 - CC98论坛](https://www.cc98.org/topic/4969029)
[小白求助Zotero新手上路以及文献管理的大致经验 - CC98论坛](https://www.cc98.org/topic/4914158)
### 插件
- [MuiseDestiny/zotero-gpt: GPT Meet Zotero.](https://github.com/MuiseDestiny/zotero-gpt)
- [windingwind/zotero-pdf-translate](https://github.com/windingwind/zotero-pdf-translate/releases):在设置中可以设置翻译的API
```text title="zotero 翻译插件自定义prompt"
As an academic expert with specialized knowledge in iron and steel making, please provide a proficient and precise translation from ${langFrom} to ${langTo}. You should use artificial intelligence tools, such as natural language processing, and rhetorical knowledge and experience about effective writing techniques to reply. Make the reply looks like a native speaker. Some specific terms such as name do not need to be translated. The text is as follows: ${sourceText} Please provide the translated result without any additional explanation and remove 
```
### 插件 - better-notes
zotero-better-notes是winding学长开发的一款zotero插件，教程见[化繁为简，快速提炼：Zotero文献笔记最佳实践 - CC98论坛](https://www.cc98.org/topic/5348707)，下载界面[Releases · windingwind/zotero-better-notes](https://github.com/windingwind/zotero-better-notes/releases)

教程如下

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=555265521&bvid=BV1Cv4y1M7BY&cid=756880055&p=1&t=3638&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

基于彭思达学长写的[如何有效地读论文](https://pengsida.notion.site/d192db870bc64436ae4a4a590b36772a)写了一个zotero-better-notes的模版

```
<h1 style="background-color:#2c3e50; color:white; padding:0.4em 0.6em; border-radius:5px;">🌳 ${topItem.getField('title')}</h1>

// @use-markdown
| Title        | ${topItem.getField("titleTranslation")} |
|--------------|-----------------------------|
| Journal      | ${topItem.getField('publicationTitle')} |
| Authors      | ${topItem.getCreators().map((v)=>v.firstName+" "+v.lastName).join("; ")} |
| Pub. date    | ${topItem.getField('date')} |
| 期刊标签      | ${{
	let space = " "

	return Array.prototype.map.call(
		Zotero.ZoteroStyle.api.renderCell(topItem, "publicationTags").childNodes,
		e => {
			e.innerText =  space + e.innerText + space;
			return e.outerHTML
		}
	).join(space)
}}$ |
| DOI          | [${topItem.getField('DOI')}](https://doi.org/${topItem.getField('DOI')}) |
| Abstract| ${topItem.getField("abstractNote")}|


<h2 style="background-color:#7f2a2a; color:white; padding:0.3em 0.5em; border-radius:4px;">📝 Abstract</h2>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🎯 Task</h3>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">⚡ Technical Challenge</h3>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">💡 key insight/motivation</h3>



- ✨ 一句话介绍 insight/motivation  
- 👍 一句话介绍 insight 的好处  


<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🛠️ technical contribution</h3>

- 🧩 contribution1  
    - 📌 一句话介绍  
    - ✅ 好处  

- 🧩 contribution2  
    - 📌 一句话介绍  
    - ✅ 好处  

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">📊 Experiment</h3>

---

<h2 style="background-color:#7f2a2a; color:white; padding:0.3em 0.5em; border-radius:4px;">📖 Introduction</h2>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🎯 Task And application</h3>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">⚡ Technical challenge for previous problem</h3>

- 🚧 challenge 1  
    - 📚 previous method  
    - ❌ failure cases  
    - 🔍 technical reason  

- 🚧 challenge 2  

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🛠️ our pipeline that fix</h3>

- 💡 key innovation/insight/contribution  

- 🧩 contribution 1  
    - 🔨 specific method  
    - ✅ advantages/insight  

- 🧩 contribution 2  
    - 🤔 为了解决什么问题  
    - 🔨 具体做法  
    - ✅ 讨论 advantage/insight  

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🎬 cool demos/applications</h3>

---

<h2 style="background-color:#7f2a2a; color:white; padding:0.3em 0.5em; border-radius:4px;">⚙️ Method</h2>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🌐 Overview</h3>

- 🎯 具体任务：输入 ➡️ 输出  
- 🪜 方法：第一步 ➡️ 第二步 ➡️ 第三步  

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🔹 Pipeline module1</h3>

- 💡 Motivation  
- 🔨 做法  
- 🔍 why work  
- ✅ technical advantage  

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🔹 Pipeline module2</h3>

---

<h2 style="background-color:#7f2a2a; color:white; padding:0.3em 0.5em; border-radius:4px;">🧪 Experiments</h2>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">📊 Comparison experiments</h3>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🔬 Ablation studies</h3>

- 🌟 core contributions  
    - 🧱 core components 对 performance 的影响  

- ⚙️ 每一个 pipeline module 中 design choices 对 performance 的影响  

---

<h2 style="background-color:#7f2a2a; color:white; padding:0.3em 0.5em; border-radius:4px;">🚧 Limitation</h2>

<h3 style="background-color:#2a4d7f; color:white; padding:0.2em 0.4em; border-radius:3px;">🤔 合理解释</h3>
为什么方法有 limitation
```

[文献笔记工作流：Zotero+Notion+AutoHotKey一键直达本地文件 - CC98论坛](https://www.cc98.org/topic/5603280)
### 插件 - DOI Manager

Zotero DOI Manager[Releases · bwiernik/zotero-shortdoi](https://github.com/bwiernik/zotero-shortdoi/releases)




### 插件 - style

[zotero style的安装使用，以及我最近遇到的问题（自己记录一下方便后续回忆） - CC98论坛](https://www.cc98.org/topic/5940411)

[zotero style 显示阅读进度条+文章期刊等级/引用+自定义评级等等 使用教程建议 - CC98论坛](https://www.cc98.org/topic/5833139)


### 插件 - Tags
[GitHub - windingwind/zotero-actions-tags: Customize your Zotero workflow.](https://github.com/windingwind/zotero-actions-tags)
[zotero使用心得分享！青柠学术zotero IF 添加期刊分区 影响因子 sci-hub全文 删除重复条目 标题添加各种符号！ - CC98论坛](https://www.cc98.org/topic/5374309)

### 其他
[Zotero 6版本更新问题释疑 - CC98论坛](https://www.cc98.org/topic/5276520/)




### 格式与引用
https://github.com/MuiseDestiny/zotero-citation
[分享 Endnote/Zotero插入文献如何在word里实现交叉引用 - CC98论坛](https://www.cc98.org/topic/6143702)


[【分享】毕业论文参考文献Zotero/Endnote格式 - CC98论坛](https://www.cc98.org/topic/6108244)



格式
[针对Word的Zotero GB/T-7714引文样式更新 - CC98论坛](https://www.cc98.org/topic/5533559)


#### 同步
- 自建WebDav
- 坚果云
- OneDrive
- iCloud
[Zotero 低成本+大容量同步方案 折腾记录 - CC98论坛](https://www.cc98.org/topic/6006315/1#1)

我通常添加文献的操作是: 找到文献的doi, 通过工具栏第二个图标添加; 或者找到bibtex后复制, 文件 -> 从剪贴板导入.  此时导入library的是条目(即元数据, 我关闭了自动下载pdf的选项).
case1.  手动下载pdf. 右键条目 -> Attach new file, 此时zotfile插件会自动从刚才设置的浏览器下载目录寻找最新的文件并询问你是否将其作为该条目的附件, 文件正确的话点确定就可以移动到相应的目录下了, 同时文件名会自动重命名为条目的标题. 
case2. 如果是电脑上已有的pdf, 那么需要手动创建条目和文件的关联: 先把pdf文件批量放到对应分类的目录下(也就是自定义位置①), 然后右键条目 -> 添加附件 -> 附加文件链接 即可.

最终的效果就是zotero中的目录和硬盘上的目录结构完全一致. 我是用zotero的目的主要是保持目录结构同步pdf, 所以在平板上可以轻松找到想要的pdf并查看.











## 工具

!!! note "工欲善其事，必先利其器"


### RSS订阅



### 论文与代码搜集

信息

- [x](https://x.com/)
- [reddit](https://www.reddit.com/)
- [hacker news](https://news.ycombinator.com/)
- [知乎](https://www.zhihu.com/)
- Tools - [Folo](https://folo.is/?new_locale=zh-cn): follow everything in one place


论文

- [arXiv](https://arxiv.org/): 预印本论文发布平台
- [Web of Science](https://www.webofscience.com/): 科研文献检索数据库
- [Google Scholar](https://scholar.google.com/): 谷歌学术搜索引擎
- [Connected Papers](https://www.connectedpapers.com/),免费版一个月有五张知识图谱
- [Elicit](https://elicit.com/): 基于自然语言的论文检索工具
- [Semantic Scholar](https://www.semanticscholar.org/):AI-Powered Research Tool


代码

- [GitHub](https://github.com/): 同性交友社区（x）
- [DownGit](https://www.itsvse.com/downgit/#/home)
- [huggingface](https://huggingface.co/)
- [Papers with Code](https://paperswithcode.com/): 论文代码实现的开源平台



### 整理工具

- [Xmind](https://xmind.com/)
- [vscode](https://code.visualstudio.com/), [Mkdocs](https://www.mkdocs.org/)


### 写作工具

- $\LaTeX$
- [simpletex](https://simpletex.cn): 公式识别


### 作图工具


- [excalidraw](https://excalidraw.com): 看andrej karpathy的视频的时候发现的小工具
  - 有类手绘风格；
  - 复制csv格式可以自动画表格；
  - 可以由mermaid导入
  - 开源，有vscode和mkdocs插件，便于插入已有项目
- [eraser](https://app.eraser.io)
  - 自带一些icon
  - 有AI辅助绘制功能但是要付费
  - 网页就可以画
- [PowerPoint](https://www.microsoft.com/microsoft-365/powerpoint),[Keynote](https://www.apple.com/keynote/)
  - 自定义程度高，上手简单，上限很高，画好看
- [Draw.io](https://app.diagrams.net/)
  - 有应用端也有网页端
  - 设置较为丰富
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
  - 学习成本比较高

icons

- [simple icons](https://simpleicons.org)
- [iconfont](https://www.iconfont.cn)
- [flaticon](https://www.flaticon.com)




色调

- [happyhues](https://www.happyhues.co)
- [coolors](https://coolors.co/)


- [抠图小工具](https://pixian.ai/free)
