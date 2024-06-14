# Latex备忘录

## 环境与配置

### Overleaf | 从入门到入土









### `TexLive`

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
|            |           | `^\circ`   | $^\circ$   |
| `\oplus`   | $\oplus$  |            |            |
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



