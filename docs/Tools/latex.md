# Latex常用

## 希腊符号

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

## 计算符号

| LaTeX 代码 | 运算符号  | LaTeX 代码 | 运算符号   |
| ---------- | --------- | ---------- | ---------- |
| `+`        | $+$       | `-`        | $-$        |
| `\times`   | $\times$  | `\cdot`    | $\cdot$    |
| `\div`     | $\div$    | `\sqrt{x}` | $\sqrt{x}$ |
|            |           | `^\circ`   | $^\circ$   |
|            |           |            |            |
|            |           |            |            |
| `>`        | $>$       |            |            |
| `<`        | $<$       | `\neq`     | $\neq$     |
| `=`        | $=$       | `\equiv`   | $\equiv$   |
| `\approx`  | $\approx$ | `\in`      | $\in$      |









## 箭头

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

## 括号



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



## 矩阵与向量

|               |                  |
| ------------- | ---------------- |
| \vec{}        | $\vec{a}$        |
| \mathbf       | $\mathbf{A}$     |
| \boldsymbol{} | $\boldsymbol{A}$ |



## 标注

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
