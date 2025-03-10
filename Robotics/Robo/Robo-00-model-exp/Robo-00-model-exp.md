# 机械臂
## Coppeliasim

- [用户手册](https://www.coppeliarobotics.com/helpFiles/index.html)
- [CoppeliaSim用户手册中文翻译版](https://blog.csdn.net/Csdn_Darry/article/details/107142216)
- [API接口](https://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm)
- [如何绘制轨迹曲线](https://www.coppeliarobotics.com/helpFiles/en/graphs.htm)
- [如何搭建一个机械臂（带动力学，有兴趣可以看一下）](https://www.coppeliarobotics.com/helpFiles/en/buildingAModelTutorial.htm)

### 环境配置

打开文件 

- Windows:`C:\Users\<username>\AppData\Roaming\CoppeliaSim\usrset.txt`
- MacOS:`/Users/<username>/.CoppeliaSim/usrset.txt`

将`default Python`项修改为所安装Python的路径（确保与1中的python一致） 注：“\\”为注释，请在其之前输入路径

> 找python路径的方法
> Python: `python的安装路径\python.exe`
> Anaconda: `anaconda的安装路径\envs\env_name\python.exe`


!!! tip "仿真环境验证"
    完成上述仿真环境配置后，进入Coppeliasim软件，右键`new scene`中的`Floor`，选择`Add -> Associated child script -> Non Threaded -> Python`

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250303130523387.png)

    函数`sysCall_init()`中键入代码

    ```python
    floor = sim.getObject(".") # 获取当前场景中的 . 对象，"." 代表的是 当前对象，如果是在主脚本里运行，通常指的是整个场景的地面 (floor)
    print(sim.getObjectPosition(floor, -1)) # 获取 floor 相对于 世界坐标系（-1 代表世界坐标系）的位置信息，返回的是 [x, y, z] 坐标。
    ```

    运行并得到在控制台得到结果

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250303130627705.png)

    为什么 Z 轴值是 `-0.1`？
    在 `CoppeliaSim` 里，默认地面 (Floor) 通常不是在 `z = 0`，而是位于 `z = -0.1`。这可能是**为了避免浮动误差或保证物体接触地面时的稳定性**。

    如果你想让地面在 `z = 0`，可以手动修改地面的 Z 轴位置，例如：

    ```python
    sim.setObjectPosition(floor, -1, [0, 0, 0])
    ```
### 快捷键
- `CTRL+<space>`：开始/停止模拟
- `CTRL+E`：在1）普通，2）对象平移和 3）对象旋转鼠标模式之间切换
- `CTRL+D`：打开对象属性对话框
- `CTRL+G`：打开计算模块对话框
- `CTRL+B`：调整视图以适合选定的对象；如果未选择任何对象，则调整整个场景。 重点需要放在视图上。
- `CTRL+ALT+C`：将焦点放在Lua命令行控制栏上
- `CTRL+L`：清除状态栏（当焦点在Lua命令行控制栏上时）


## 仿真实验1：机械臂正、逆运动学求解

!!! note "实验器材"
    - ZJU-I型桌面机械臂
    - 机器人关节模组
    - CoppeliaSim
    - Python、Matlab、VSCode

### 机械臂几何参数

每一轴的位置、速度、加速度约束（当前状态是各个关节零点）

|  | 关节一 | 关节二 | 关节三 | 关节四 | 关节五 | 关节六 |
| --- | --- | --- | --- | --- | --- | --- |
| 最小关节值 | $-200^\circ$ | $-90^\circ$ | $-120^\circ$ | $-150^\circ$ | $-150^\circ$ | $-180^\circ$ |
| 最大关节值 | $200^\circ$ | $90^\circ$ | $120^\circ$ | $150^\circ$ | $150^\circ$ | $180^\circ$ |

|  | 关节一 | 关节二 | 关节三 | 关节四 | 关节五 | 关节六 |
| --- | --- | --- | --- | --- | --- | --- |
| 关节速度 | $100^\circ/s$ | $100^\circ/s$ | $100^\circ/s$ | $100^\circ/s$ | $100^\circ/s$ | $100^\circ/s$ |
| 关节加速度 | $500^\circ/s^2$ | $500^\circ/s^2$ | $500^\circ/s^2$ | $500^\circ/s^2$ | $500^\circ/s^2$ | $500^\circ/s^2$ |

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250310103313209.png)
> 图源课程实验要求

### 实验要求
1. 写出ZJU-I型桌面机械臂的DH参数；
2. 写出ZJU-I型机械臂的正运动学解（不用给出最终的齐次变换矩阵的具体代数式），并采用$XY'Z'$欧拉角表示末端执行器姿态；
3. 将以下5组关节角参数带入正运动学解，计算机械臂末端Tip点的空间位置，计算末端执行器的姿态，以$XY'Z'$欧拉角表示结果，写出计算过程；
   - 第一组：$\left(\frac{\pi}{6}, \frac{\pi}{6}, 0, \frac{\pi}{3}, 0\right)$
   - 第二组：$\left(\frac{\pi}{6}, \frac{\pi}{6}, \frac{\pi}{3}, 0, \frac{\pi}{6}\right)$
   - 第三组：$\left(\frac{\pi}{2}, 0, \frac{\pi}{2}, \frac{\pi}{3}, \frac{\pi}{6}\right)$
   - 第四组：$\left(-\frac{\pi}{6}, -\frac{\pi}{6}, \frac{\pi}{3}, 0, \frac{\pi}{6}\right)$
   - 第五组：$\left(\frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}\right)$
4. 将以上5组关节角分别输入仿真程序，将仿真得到的末端位姿与第3步得到的计算结果进行比对。

5. 写出ZJU-I型桌面机械臂的逆运动学解析解（可选）；
6. 将如下5组末端位姿参数分别代入逆运动学解（可使用自带的逆运动学求解器进行相关计算），计算对应的5组关节角；
   - 第一组：$(0.117, 0.334, 0.499, -2.019, -0.058, -2.190)$
   - 第二组：$(-0.066, 0.339, 0.444, -2.618, -0.524, -3.141)$
   - 第三组：$(0.3, 0.25, 0.26, -2.64, 0.59, -2.35)$
   - 第四组：$(0.42, 0, 0.36, 3.14, 1, -1.57)$
   - 第五组：$(0.32, -0.25, 0.16, 3, 0.265, -0.84)$
7. 将所求关节角作为参数输入仿真程序，从仿真中得到机械臂末端执行器的空间位置和姿态，与第6步给定的位置和姿态进行比对。


!!! note "报告要求"
    **机械臂正、逆运动学求解**
    1）ZJU-I型机械臂的DH参数<br>
    2）机械臂的正运动学及其仿真结果<br>
    3）机械臂的逆运动学及其仿真结果<br>

    **最终提交文件**，需包括

    1）组号-实验报告`.docx/pdf`（推荐pdf）
    2）组号-代码文件`.rar/zip`：Coppeliasim仿真软件的`.ttt`文件及包含的其他代码文件
    3）组号-仿真结果`.mp4/mov/其他视频文件`格式：机械臂轨迹规划仿真实验的录屏文件（文件大小应小于50Mb，推荐使用`Win+G`中的“捕获”进行录制）

### DH参数



### 正运动学




### 逆运动学







## 仿真实验2 ：机械臂点到点轨迹规划

通过控制机械臂关节运动，将机械臂末端执行器从起点在规定时间内运动到终点

注意各个关节轴的位置、速度、加速度限制，若超出限制将会停止运行！！！

不限制规划方案，但是需要注意，最终的成绩与机械臂运行合理性、关节轴速度和加速度连续性等相关。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250310103409385.png)

要求：
1. 起点位姿$(0.117,0.334,0.499,-2.019,-0.058,-2.190)$
2. 终点位姿$(0.32,-0.25,0.16,3,0.265,-0.84)$
3. 初始速度：0；终点速度：0；运行时间：2秒


!!! note "报告要求"
    **机械臂轨迹规划**，具体需包括

    1）仿真实验整体方案介绍<br>
    2）机械臂的轨迹规划方案<br>
    3）轨迹规划仿真结果（视频）<br>

    **最终提交文件**，需包括

    1）组号-实验报告`.docx/pdf`（推荐pdf）
    2）组号-代码文件`.rar/zip`：Coppeliasim仿真软件的`.ttt`文件及包含的其他代码文件
    3）组号-仿真结果`.mp4/mov/其他视频文件`格式：机械臂轨迹规划仿真实验的录屏文件（文件大小应小于50Mb，推荐使用`Win+G`中的“捕获”进行录制）

## 实物实验1：六自由度机械臂物体抓取与放置实验

1. 编写程序控制ZJU-I型机械臂，实现木块抓取与搬运，具体流程为：
    a) 机械臂从零位置启动，运行至起始区域；
    b) 启动真空吸爪，抓取起始区域内的木块，移动至A点
    $(370，-90，115)$；
    c) 移动过程中控制木块从A点沿直线路径运动至B点
    $(288，-288，115)$；
    d) 控制从B点到达目标区域，目标区域位置为机械臂1号关节旋转角度$90^\circ$所在位置；
    e) 抓取第二个木块放置到目标区域，并堆叠在第一个模块上，二者姿态保持一致；
2. 程序中需要编写正、逆运动学求解代码、轨迹规划代码，要求机械臂无碰撞、所有关节速度平滑；
3. 分组完成实验，每组提交一份实验报告，内容不超过4页；



## Explore
### Pybullet环境配置

查看Matlab支持的Python版本



[Versions of Python Compatible with MATLAB Products by Release - MATLAB & Simulink](https://ww2.mathworks.cn/support/requirements/python-compatibility.html)

[maltab与pybullet联合仿真 - \_夜尘 - 博客园](https://www.cnblogs.com/Techron/p/17180373.html)


[pybullet学习（一）——安装与入门pybullet-CSDN博客](https://blog.csdn.net/bulletstart/article/details/130977713)


[PyBullet笔记（一）pybullet及其依赖项的安装、pybullet初探 - 知乎](https://zhuanlan.zhihu.com/p/347078711)


!!! note "官方笔记"
    https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit?tab=t.0

    [openai/baselines: OpenAI Baselines: high-quality implementations of reinforcement learning algorithms](https://github.com/openai/baselines)

```bash
pip install pybullet
```

由于pybullet中一些开箱即用的模型是通过tensorflow实现的，所以tensorflow也需要装一下：
```bash
pip install tensorflow
```

pybullet的官方也提供了一些好玩的demo，不过这些demo需要额外下载，先进入windows下一个你想要安放这些baselines的目录，然后输入：
```bash
git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .    
```
