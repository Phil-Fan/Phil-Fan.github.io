# 传感器与相机




**功能**

异常检测和图像分析；物体检测和识别；物体分割和识别；扫描测绘；环境理解；

![image-20240416180035101](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416180035101.png)



[三维视觉测量技术：“被动”和“主动”视觉测量 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/590263368)

[Stanford University CS231n: Deep Learning for Computer Vision](https://cs231n.stanford.edu/assignments.html)

### 被动视觉传感器

定义：**被动视觉测量**不需要特殊的照明投射装置，仅利用相机拍摄被测物的图像，建立被测物与相机之间的相对位置关系，从而获取被测物表面的三维信息

原理：借助外部光源的漫反射并结合小孔成像

CCD传感器：放在成像面的一块具有反光能力的芯片

缺点：

- 无法获得物体的深度和大小（了解大小需要参照物 ）
- 在外部光弱的情况下无法成像，依赖于外部环境影响

双目相机可以获得深度

![image-20240426112619019](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426112619019.png)

- 视差角的概念（图中a）
- 需要认识两个图片直接的像素关系
  - 改进措施：左目主动发射光源



### 主动视觉传感器

主动视觉测量与被动视觉测量最大的不同在于需要向被测物体投射光源



### 机器人视觉应用

- 划痕检测
- 土壤分析
- 文字识别
- 人脸识别
- 视觉定位、导航

视觉提供了一种**几何测量**的工具，也提供一种**语义认知**的工具

各种视觉应用是两种工具功能的组合



### 图像函数

图像是定义在CCD阵列下的离散函数  
$$
I:(u,v) ∈ [0,W-1] × [0,H-1] → q ∈ R^N  \\
q = I(x)
$$
W,H分别为像素格数（横纵）



#### 成像原理

![image-20240426111452711](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426111452711.png)

**漫反射**无法成像

![image-20240426111518621](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426111518621.png)

依靠小孔成像实现

![image-20240426111607412](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426111607412.png)

用𝑐𝑥， 𝑐𝑦表示图像坐标系下的光心  

引入 R， t 表示实际世界坐标和相机中心之间的位姿  

#### 镜头畸变

![image-20240426111747018](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426111747018.png)

![image-20240426111759427](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426111759427.png)



#### 相机标定

相机标定， 借助外部已知尺寸的物体，解算出内参

![image-20240416180059493](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416180059493.png)

- 采用棋盘格作为已知尺寸的物体，利用平面特性方便求解  
- 棋盘格的角点检测相对简单，可靠性高  

#### 外参应用

- 基于指定尺寸平面，可以估计出平面和相机的外参，也就是相机在世界坐标系下的位姿
- 如果在世界坐标系下，增加一个虚拟点，可以计算出在图像中的成像  
