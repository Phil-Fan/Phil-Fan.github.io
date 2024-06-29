# Latex备忘录

## 环境与配置
### `TexLive` | windows 的 `LaTeX `环境

[Installing TeX Live over the Internet - TeX Users Group (tug.org)](https://www.tug.org/texlive/acquire-netinstall.html)

### `IguanaTex` | LaTeX in PPT

假设已经安装好了Texlive

[IguanaTex - A Free Latex Add-In for PowerPoint on Windows and Mac (jonathanleroux.org)](https://www.jonathanleroux.org/software/iguanatex/)

**注意设置好路径**



#### [`GhostScript`](https://ghostscript.com/releases/gsdnld.html) and [`ImageMagick`](https://www.imagemagick.org/script/download.php#windows)

required to use pdflatex/xelatex/lualatex.

1. **Install and set path to GhostScript and ImageMagick**:

- Set the **full** path to `gswin32c.exe` or `gswin64c.exe` (note the "`c`"!) and to ImageMagick's magick.exe in the "Main Settings" window.
- Best way to make sure the path is correct is to use the "..." button next to each path and navigate to the correct file.
- Some default paths include `%USERPROFILE%`. It is recommended to click on "..." to make sure the path gets properly converted to the actual user profile path.

#### **`TeX2img`**（SVG）

(Optional): [TeX2img](https://github.com/abenori/TeX2img), used for vector graphics output via EMF ([Download](https://www.ms.u-tokyo.ac.jp/~abenori/soft/index.html#TEX2IMG)). Note that vector graphics output via SVG is now recommended if you have Office 2019 or 365.

- Only needed for vector graphics support via EMF (compared to SVG, pros: available on all PowerPoint versions, fully modifiable shapes; cons: some displays randomly suffer from distortions)
- Download from [this link](https://www.ms.u-tokyo.ac.jp/~abenori/soft/index.html#TEX2IMG) (more details on TeX2img on their [Github repo](https://github.com/abenori/TeX2img))
- After unpacking TeX2img somewhere on your machine, run TeX2img.exe once to let it automatically set the various paths to latex/ghostscript, then set the **full** path to `TeX2imgc.exe` (note the "`c`"!) in the "Main Settings" window.

!!! bug "中文公式输入错误"

![image-20240609200702478](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240609200702478.png)

```latex
\documentclass{article}
\usepackage{amsmath}
\pagestyle{empty}

\begin{document}
\begin{align*}
  
\end{align*}
\end{document}
```

## Overleaf | 边学边用的使用指南



最早是看到98上发的有关latex的帖子，说可以快速高效地写实验报告。也从雪松前辈发的模版中学习到一些latex排版的基础知识。再加上去年《数学软件》短学期老妖的一些小作业的磨炼，可以说对latex的基本用法有了浅薄的了解。这个学期的所有课程作业报告和论文就没有使用过word了（真香啊:laughing:）。

!!! tip "趁手的工具才是最好的工具"

!!! note "为什么要写这一个章节"
    众所周知，大学中有很多课程都需要写实验报告/解题报告/小作业报告/论文等等，除却写作内容，排版也是非常令人头疼的一部分。常用的排版工具有两大类，一类是以word为代表的“所见即所得”式，另一类是像latex这样子的“所想即所得”的编程式排版。

	发现身边有很多朋友并不是非常会排版，或者是排版会花费很多时间。而在现行的评价体系下，在内容质量大致相似的情况下，图文并茂，排版整洁的作业印象分一定会高不少。笔者latex水平不高，目的就是想要快点把实验报告写掉:laughing:，中间也花了很多时间迭代这几个模版，所以就有了这个笔记+分享性质的章节。

    这一个章节面向0 latex 基础小白，使用`overleaf`平台，希望实现的效果是基本掌握后，只用15-20min就能完成日常论文/实验报告作业的排版。



=== "我为什么要用latex"
    - 复用性高，所有设置都比较明晰 :yellow_heart:
    - 只要做一个称心如意的模版，便可以**专注于内容本身，而将麻烦的排版交给编译器**:full_moon_with_face:
    - 无敌的公式体验：公式编辑较word方便和美观太多
    - 公式、图表、参考文献都可以自动标号

=== "我为什么要用overleaf"
    - 云端自动保存、不怕写了半天的论文突然消失
    - 不用进行包管理、环境配置简单、打开网址就可以用
    - 有很多模版供使用

这里分享4个我自己魔改的模版，基本上覆盖到了大部分的日常学习场景。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240629181605.png)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240629181704.png)

- [Template1：日常课程小作业](https://www.overleaf.com/read/hqckgzcdwscq#d182d9)
- [Template2：中文课程论文](https://www.overleaf.com/read/yqgsngdxvvcd#a149e2)
- [Template3：实验报告](https://www.overleaf.com/read/zxmwdhtbssrf#ee235c) 按照嵌入式系统等一些课程给的word模版改编
- [Template4：实验报告](https://www.overleaf.com/read/kjpmbgxvmcwr#e6e432)  这一个是笔者使用频率最高的模版。

使用模版的时候，**点击复制按钮，将模版复制一份使用**！

在进行排版之前，你至少需要以下：

- 文本
- 插入的图片（最好可以按照一定的顺序保存在某个文件夹中，并命好名）
- 参考文献（`bibtex`版本）：可以直接从`cnki`中导出或者使用`endnote`或者`zotero`等工具

> 如果上面都没有，你想要边写边排也是可以的:laughing:

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628200644890.png" alt="界面介绍" style="zoom:50%;" />

### 工具栏与快捷键

首先来认识一下工具栏，这里标出了常见的功能。其中中文论文使用的比较多的可能是多级标题、图片、表格、文献。

> 如果你还是一头雾水，不要着急，慢慢拆分一个个讲解

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628201309401.png" alt="image-20240628201309401" style="zoom:50%;" />

`ctrl+B`:加粗

`ctrl+/`:注释，latex中的注释是以`%`开头的，

```latex
% 我是一行注释
\section{} %我是一句注释
```



### 个人信息

先填好自己的个人信息，包括姓名、学号

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628203915349.png" alt="image-20240628203915349" style="zoom:70%;" />

### 标题与小标题

一般不建议使用3-4甚至更高的标题

```latex
\section{} % 我是一级标题
\subsection{} % 我是二级标题
\subsubsection{} % 我是三级标题
```



### 表格

- latex表格比较麻烦，一种简单快捷的方式是使用其他软件（excel、tableau）直接生成表格，另存为图片格式复制进latex中（最简单省时）
- 如果你还是想在latex中打表格 :laughing: ，推荐一个网站[Create LaTeX tables online – TablesGenerator.com](https://www.tablesgenerator.com/#)，在excel中打好之后。复制到这个网站中，点击`generate`，把生成的代码复制进编辑区域
> 有时候会遇到一些奇怪的问题
- 还可以使用`excel2latex`等excel的插件，不过感觉使用体验没有第二种方法好。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628205446618.png" alt="image-20240628205446618" style="zoom:33%;" />



### 图片怎么插入

- 方法一：点击工具栏里边的图片按钮
- 方法二：直接在编辑窗口粘贴你想要的图片

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628203629409.png" alt="image-20240628203629409" style="zoom: 50%;" />

插入之后编辑区域就会出现这样的代码

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.5\linewidth]{figures/example.png} % 数字表示放缩比例
    \caption{Enter Caption} % 图片标题
    \label{fig:enter-label} % 图片tag，用于交叉引用
\end{figure}
```

注意！！！

- 如图，`folder location`请放在`figures`这个文件夹下，你可以在左侧的列表中看到。
- 请在`\begin{figure}`后边加上`[htbp]`!



**如何插入并排的图片**

使用下面的代码，把`example`位置替换为想插入的图片的路径即可。

同样的，这里的数字代表放缩的比例，可以修改一下看看会发生什么。

```latex
\begin{figure}[!htbp]
    \centering
    \begin{minipage}[b]{0.45\linewidth}
        \centering
        \includegraphics[width=0.9\textwidth]{example}
        \caption{非子图并排题注1}
    \end{minipage}%
    \begin{minipage}[b]{0.45\linewidth}
        \centering
        \includegraphics[width=0.9\textwidth]{example}
        \caption{非子图并排题注2}
    \end{minipage}
\end{figure}
```



**如何插入2x2，3个并排或者其他类型**

在`pic.tex`文件中，由多种图片展示形式，选择你想要的形式，将代码复制到主文件下，把`\includegraphics[width=0.5\linewidth]{figures/example.png}`这一行改成你想要的图片的路径。



### 参考文献如何设置

`latex`中的参考文献是使用`bibtex`，什么意思呢？就是要用类似下面的语句来声明一个你要引用的文献

```latex
@book{14,
  title={新时代的中国绿色发展},
  author={{中华人民共和国国务院新闻办公室}},
  publisher={人民出版社},
  year={2023},
  address={北京}
}
```

这种格式如何获取呢？

=== "方式一：从你找到论文的网页获取"
	<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628210459330.png" alt="image-20240628210459330" style="zoom: 50%;" />

=== "方式2：使用`endnote`或者`zotero`等文献管理软件"
	<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240628210840951.png" alt="image-20240628210840951" style="zoom:50%;" />

=== "方式3——GPT"
	你已经有了一版参考文献的列表，但是你懒得一个一个去知网找了；打开任意一个大模型，输入你的参考文献的列表，说"请把上边的参考文献改写成为bibtex的格式"



获取之后，请把对应的代码放在`ref.bib`文件下，这个代码中的`number1`可以改成任何你记得住的数字或者字符，相当于给这个参考文献一个名字。

```latex
@book{number1,
  title={新时代的中国绿色发展},
  author={{中华人民共和国国务院新闻办公室}},
  publisher={人民出版社},
  year={2023},
  address={北京}
}
```



**在文中如何引用呢？**

在准备好上面的文献列表以后，在文中想要插入引用文献的地方打`\cite{xxx}`命令，xxx就是你刚才给文献取的名字。

### 交叉引用

你的论文或许有这样的片段——“如图1所示” “由表1可知”

但是如果你的图片不止一张，或者你在这张图片前面又加了一张图片，那顺序不就乱了吗？难道还要一个一个手动编号吗！！！？:sob: 

当然不用！:laughing:

聪明的你可能注意到了，在刚才图片或者表格的代码当中，有一行是`label`，这一行的名字就相当于图片的tag。

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.5\linewidth]{figures/example.png} % 数字表示放缩比例
    \caption{Enter Caption} % 图片标题
    \label{xxxx} % 图片tag，用于交叉引用
\end{figure}
```

`如图1所示`——就可以改写成`如图\ref{xxxx}所示`，其中`xxxx`是你要交叉引用的对象的label


### 公式
这点应该是latex的强项了
可以依照参考文献中的资料，自己学习一下相关语法

遇到不会的上网搜索一下，应该问题不大。

推荐一个小工具 https://www.latexlive.com/


### 共享与同步

点击右上角的`share`按钮，就可以打开共享链接，分为两种权限——只读和可编辑。发给同伴以后就可以一起编辑了。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240629191400.png)

### 其他

至此，你已经可以使用上面的功能去编辑一篇有模有样的论文了。快去试试吧！

要记住的是，使用一种新的工具，遇到问题是很正常的事情。遇到问题先自行排查问题原因，搜索解决方案，这也是学习latex的很好途径。

如果遇到了解决不了的问题，先上网搜有没有相似的问题，再问问GPT。也可以在98上发帖求助，但先看一下[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)和[别像弱智一样提问](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这两篇文章





### 拓展阅读 & 98资源整合

感谢各位前辈的分享！

=== "教程类"

    [Documentation - Overleaf](https://www.overleaf.com/learn)

    [一份其实很短的 LaTeX 入门文档](https://www.cc98.org/topic/4914572)

=== "模版类"

    [如何使用zjuthesis编写毕业论文：LaTeX零基础入门](https://www.cc98.org/topic/5511675)

    [魔改了个课程大作业报告 Latex 模版](https://www.cc98.org/topic/5548440)

    [Typora 实验报告模板 基于github上项目typora-latex-theme](https://www.cc98.org/topic/5834340)

    [开坑LaTeX笔记模板，目标将ElegantNote斩于马下](https://www.cc98.org/topic/5337819)

    [分享一个微调后的数院学位论文latex模板（hyperref+bibtex）](https://www.cc98.org/topic/5141677)

    [本科生实验报告 LaTeX 模板](https://www.cc98.org/topic/5068412)

    [本科生毕业设计与展示latex模板](https://www.cc98.org/topic/5070413)

    [自制了一个简单的课程论文的LaTex模板](https://www.cc98.org/topic/5063731)

=== "笔记 & 技巧类"

    [Latex笔记美化](https://www.cc98.org/topic/5325844)

    [我是如何用vim+latex记笔记的](https://www.cc98.org/topic/5319293)

    [发现一个超好用的\LaTeX公式和绘图工具](https://www.cc98.org/topic/5089911)

    [开一个帖子记录下使用latex时学会的一些技巧](https://www.cc98.org/topic/5126300)

    [latex一夜入门 搞定 简历模版](https://www.cc98.org/topic/5008837)

    [🍃overleaf本地部署｜会员｜解除时间限制](https://www.cc98.org/topic/5874634)

    [合法免费白嫖 Overleaf 高级会员方法，解决编译时间限制问题（已失效）](https://www.cc98.org/topic/5749388)

## 排版

### 字号与字体

设置字体大小的基本尺寸为10pt，11pt和12pt，其中默认为10pt

```latex
\documentclass[12pt]{article}
```

|      声明       | 对应字号 |
| :-------------: | :------: |
|     `\tiny`     |   5pt    |
|  `\scriptsize`  |   7pt    |
| `\footnotesize` |   8pt    |
|    `\small`     |   9pt    |
|  `\normalsize`  |   10pt   |
|    `\large`     |   12pt   |
|    `\Large`     |  14.4pt  |
|    `\LARGE`     | 17.28pt  |
|     `\huge`     | 20.74pt  |
|     `\Huge`     | 24.88pt  |

### 对齐

```latex
\leftline{尊敬的各位老师}     %左对齐
\rightline{书略陈固陋，勿劳赐复}    %右对齐
\centering	%居中
```



### 换行换页

```latex
\newline

\newpage
\clearpage
```

**解决英文断字重排的问题**
```latex
\hyphenpenalty=5000
\tolerance=1000
```
可以把这两个参数的调整加到tex文件里。hyphenpenalty的意思比较显而易见，这个值越大断字出现的就越少。tolerance越大，换行就会越少，也就是说，latex会把本该断开放到下一行的单词，整个儿的留在当前行。调这两个值就可以得到不一样的排版，有可能可以解决断字太多的问题。

也可以手动指定。
```latex
\hyphenation{hy-phen-a-tion}
```


### 图片位置

[htbp]



缩小放大











## 公式与符号

### 希腊符号

| LaTeX 代码 | 希腊字母   | LaTeX 代码 | 希腊字母   |
| ---------- | ---------- | ---------- | ---------- |
| `\alpha`   | $\alpha$   | `\Alpha`   | $\Alpha$   |
| `\beta`    | $\beta$    | `\Beta`    | $\Beta$    |
| `\gamma`   | $\gamma$   | `\Gamma`   | $\Gamma$   |
| `\delta`   | $\delta$   | `\Delta`   | $\Delta$   |
| `\epsilon` | $\epsilon$ | `\Epsilon` | $\Epsilon$ |
| `\zeta`    | $\zeta$    | `\Zeta`    | $\Zeta$    |
| `\eta`     | $\eta$     | `\Eta`     | $\Eta$     |
| `\theta`   | $\theta$   | `\Theta`   | $\Theta$   |
| `\iota`    | $\iota$    | `\Iota`    | $\Iota$    |
| `\kappa`   | $\kappa$   | `\Kappa`   | $\Kappa$   |
| `\lambda`  | $\lambda$  | `\Lambda`  | $\Lambda$  |
| `\mu`      | $\mu$      | `\Mu`      | $\Mu$      |
| `\nu`      | $\nu$      | `\Nu`      | $\Nu$      |
| `\xi`      | $\xi$      | `\Xi`      | $\Xi$      |
| `\omicron` | $\omicron$ | `\Omicron` | $\Omicron$ |
| `\pi`      | $\pi$      | `\Pi`      | $\Pi$      |
| `\rho`     | $\rho$     | `\Rho`     | $\Rho$     |
| `\sigma`   | $\sigma$   | `\Sigma`   | $\Sigma$   |
| `\tau`     | $\tau$     | `\Tau`     | $\Tau$     |
| `\upsilon` | $\upsilon$ | `\Upsilon` | $\Upsilon$ |
| `\phi`     | $\phi$     | `\Phi`     | $\Phi$     |
| `\chi`     | $\chi$     | `\Chi`     | $\Chi$     |
| `\psi`     | $\psi$     | `\Psi`     | $\Psi$     |
| `\omega`   | $\omega$   | `\Omega`   | $\Omega$   |

### 计算符号

| LaTeX 代码 | 运算符号  | LaTeX 代码 | 运算符号   |
| ---------- | --------- | ---------- | ---------- |
| `+`        | $+$       | `-`        | $-$        |
| `\times`   | $\times$  | `\cdot`    | $\cdot$    |
| `\div`     | $\div$    | `\sqrt{x}` | $\sqrt{x}$ |
| `\pm`      | $\pm$     | `^\circ`   | $^\circ$   |
| `\oplus`   | $\oplus$  | `\sum`     | $\sum$     |
| `\int`     | $\int$    |            |            |
|            |           |            |            |
|            |           |            |            |
| `>`        | $>$       |            |            |
| `<`        | $<$       | `\neq`     | $\neq$     |
| `=`        | $=$       | `\equiv`   | $\equiv$   |
| `\approx`  | $\approx$ | `\in`      | $\in$      |









### 箭头

|                                   |                                   |
| --------------------------------- | --------------------------------- |
| `\uparrow`                        | $\uparrow$                        |
| `\downarrow`                      | $\downarrow$                      |
| `\Uparrow`                        | $\Uparrow$                        |
| `\Downarrow`                      | $\Downarrow$                      |
| `\updownarrow`                    | $\updownarrow$                    |
| `\Updownarrow`                    | $\Updownarrow$                    |
| `\rightarrow`                     | $\rightarrow$                     |
| `\Longrightarrow`                 | $\Longrightarrow$                 |
| `\Longleftarrow`                  | $\Longleftarrow$                  |
| `\rightleftharpoons`              | $\rightleftharpoons$              |
| `\nLeftarrow`                     | $\nLeftarrow$                     |
| `\nRightarrow`                    | $\nRightarrow$                    |
| `X\stackrel{F}{\longrightarrow}Y` | $X\stackrel{F}{\longrightarrow}Y$ |

### 括号



| LaTeX 代码          | 括号类型             | 例子                                         |
| ------------------- | -------------------- | -------------------------------------------- |
| `()`                | 小括号               | `\left( x \right)` 表示 $(x)$                |
| `[]`                | 中括号               | `\left[ x \right]` 表示 $[x]$                |
| `{}`                | 大括号               | `\left\{ x \right\}` 表示 $\{x\}$            |
| `||`                | 绝对值符号           | `\left| x \right|` 表示 $|x|$                |
| `\lfloor x \rfloor` | 取整符号（向下取整） | `\lfloor x \rfloor` 表示 $\lfloor x \rfloor$ |
| `\lceil x \rceil`   | 取整符号（向上取整） | `\lceil x \rceil` 表示 $\lceil x \rceil$     |
| `\langle x \rangle` | 尖括号               | `\langle x \rangle` 表示 $\langle x \rangle$ |
| `\rangle`           | 右尖括号             | `\rangle` 表示 $\rangle$                     |



**大括号最重要的代码段是**

```
\left\{
	\begin{}
	···
	\end{}
\right.
```



```
\left\{  
             \begin{array}{**lr**}  
             x=\dfrac{3\pi}{2}(1+2t)\cos(\dfrac{3\pi}{2}(1+2t)), &  \\  
             y=s, & 0\leq s\leq L,|t|\leq1.\\  
             z=\dfrac{3\pi}{2}(1+2t)\sin(\dfrac{3\pi}{2}(1+2t)), &    
             \end{array}  
\right.  
```

$$
\left\{  
             \begin{array}{**lr**}  
             x=\dfrac{3\pi}{2}(1+2t)\cos(\dfrac{3\pi}{2}(1+2t)), &  \\  
             y=s, & 0\leq s\leq L,|t|\leq1.\\  
             z=\dfrac{3\pi}{2}(1+2t)\sin(\dfrac{3\pi}{2}(1+2t)), &    
             \end{array}  
\right.
$$





```
\begin{gathered}
\begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix}
\quad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\quad
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\quad
\begin{Bmatrix} 1 & 0 \\ 0 & -1 \end{Bmatrix}
\quad
\begin{vmatrix} a & b \\ c & d \end{vmatrix}
\quad
\begin{Vmatrix} i & 0 \\ 0 & -i \end{Vmatrix}
\end{gathered}
```

$$
\begin{gathered}
\begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix}
\quad
\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
\quad
\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
\quad
\begin{Bmatrix} 1 & 0 \\ 0 & -1 \end{Bmatrix}
\quad
\begin{vmatrix} a & b \\ c & d \end{vmatrix}
\quad
\begin{Vmatrix} i & 0 \\ 0 & -i \end{Vmatrix}
\end{gathered}
$$



### 矩阵与向量

|               |                  |
| ------------- | ---------------- |
| \vec{}        | $\vec{a}$        |
| \mathbf       | $\mathbf{A}$     |
| \boldsymbol{} | $\boldsymbol{A}$ |



### 标注

|                                                            |                            |
| ---------------------------------------------------------- | -------------------------- |
| 加^号 输入`\hat`  或 `\widehat`                            | $\hat{A}$<br>$\widehat{A}$ |
| 加横线 输入 `\overline`                                    | $\overline{A}$             |
| 加波浪线 输入` \widetilde`                                 | $\widetilde{A}$            |
| 加一个点` \dot`{要加点的字母}加两个点`\ddot`{要加点的字母} | $\dot{A},\ddot{A}$         |



字母正下方加文字

```
\mathop{expr1}\limits_{expr2}^{expr3}
```

$\mathop{expr1}\limits_{expr2}^{expr3}$​

$\sum\limits_{i=0}^n {x_i}$​

`limits`命令必需加在数学符号后边，所以使用`\mathop{}`包裹

$f_3(d) = \mathop{max}\limits_{x_3}(2x_3 + f_4(d-x_3))$



