# 逆运动学 - 已知位姿求解角度

## 数学基础：三角变换
=== "诱导公式"
    奇变偶不变，符号看象限，即形如$(2k + 1)\cdot90\pm\alpha$

=== "和角公式"
    - $\sin(\alpha + \beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$
    - $\sin(\alpha - \beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta$
    - $\cos(\alpha + \beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$
    - $\cos(\alpha - \beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$
    - $\tan(\alpha + \beta)=\frac{\tan\alpha+\tan\beta}{1 - \tan\alpha\tan\beta}$
    - $\tan(\alpha - \beta)=\frac{\tan\alpha-\tan\beta}{1+\tan\alpha\tan\beta}$

=== "倍角公式"
    - $\sin2\alpha = 2\sin\alpha\cos\alpha$
    - $\cos2\alpha=\cos^{2}\alpha-\sin^{2}\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha$
    - $\tan2\alpha=\frac{2\tan\alpha}{1 - \tan^{2}\alpha}$

=== "半角公式"
    - $\sin\frac{\alpha}{2}=\pm\sqrt{\frac{1 - \cos\alpha}{2}}$
    - $\cos\frac{\alpha}{2}=\pm\sqrt{\frac{1+\cos\alpha}{2}}$
    - $\tan\frac{\alpha}{2}=\pm\sqrt{\frac{1 - \cos\alpha}{1+\cos\alpha}}=\frac{\sin\alpha}{1+\cos\alpha}=\frac{1 - \cos\alpha}{\sin\alpha}$

=== "和差化积公式"
    - $\sin\alpha+\sin\beta = 2\sin\frac{\alpha + \beta}{2}\cos\frac{\alpha - \beta}{2}$  帅+帅 = 帅哥
    - $\sin\alpha-\sin\beta = 2\cos\frac{\alpha + \beta}{2}\sin\frac{\alpha - \beta}{2}$ 帅-帅 = 哥帅
    - $\cos\alpha+\cos\beta = 2\cos\frac{\alpha + \beta}{2}\cos\frac{\alpha - \beta}{2}$ 哥+哥 = 哥哥
    - $\cos\alpha-\cos\beta=-2\sin\frac{\alpha + \beta}{2}\sin\frac{\alpha - \beta}{2}$ 哥-哥 = 负嫂嫂

=== "万能公式"
    - $\sin\alpha=\frac{2\tan\frac{\alpha}{2}}{1 + \tan^{2}\frac{\alpha}{2}}$
    - $\cos\alpha=\frac{1-\tan^{2}\frac{\alpha}{2}}{1 + \tan^{2}\frac{\alpha}{2}}$
    - $\tan\alpha=\frac{2\tan\frac{\alpha}{2}}{1-\tan^{2}\frac{\alpha}{2}}$

=== "辅助角公式"
    - $a\sin\alpha + b\cos\alpha=\sqrt{a^{2}+b^{2}}\sin(\alpha + \varphi)$，其中 $\tan\varphi=\frac{b}{a}$


**正弦定理**

$\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R$

**余弦定理**

- $a^{2}=b^{2}+c^{2}-2bc\cos A$
- $b^{2}=a^{2}+c^{2}-2ac\cos B$
- $c^{2}=a^{2}+b^{2}-2ab\cos C$

##

给定工具坐标系的位置和姿态，解算出个各关节变量

??? info "自由度 - 刚体本身具有可独立运动方向的数目"
    > 手臂：7自由度；无穷多个解
    > 腿：6自由度;8个解

    $$
    F = 6(l - n - 1)+\sum_{i = 1}^{n}f_{i} \\
    l为连杆数（包括基座），n为关节总数，f_i为第i个关节的自由度数
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/017a2277142fe6ab01f933ad81c3e281_1440w.webp" alt="img" style="zoom:50%;" />

    > 一个6自由度的机械手，即使某两组构型对应的末端机构的三维位置相同，机械手在从一个构型移动到另一个构型的时候无法保持末端机构始终不动。
    >
    > 如果有人在电视里看过工业机器人焊东西的话，就会发现它在同一个位置焊接的时候，一会儿整个扭到这边，一会儿整个扭到那边，看起来非常酷炫的样子。事实上这么做只是因为，虽然焊接只是想改变末端机构的朝向，而不改变末端机构的位置，但是由于定理的限制，它必须要往后退一些，然后各种扭，才能保证在移动末端机构的朝向的过程中不会撞到东西，因为移动的时候末端机构的三维位置一定会乱动。如果它能够随便转一点点就可以达到目的，还费那个力气酷炫地整体都转起来干啥……
    >
    > 而多了一个自由度以后就不一样了。
    >
    > 想想开门时拧钥匙的动作，这个情况下是人胳膊的末端机构（手）的三维位置没有变（始终在钥匙孔前），但是末端机构（手）的三维旋转变了（转动了钥匙）。人能够实现这个简单的动作，就是因为我们的胳膊有7个自由度。


