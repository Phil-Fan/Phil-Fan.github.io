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

## 实验课简介

从春4-春7周

!!! note "实验器材"
    - ZJU-I型桌面机械臂
    - 机器人关节模组
    - CoppeliaSim
    - Python、Matlab、VSCode

### 代码框架

!!! tip "双击icon可以打开代码"

仿真中单位为米

- Robot中`SuctionCup_end`点展示的为机械臂末端的坐标点（仿真中为Dummy），通过选中坐标点可以在左上角查看位姿信息（其中角度为欧拉角`X-Y’-Z’`）。PS：调用API得到的姿态信息为四元数，请注意转换。
- `Platform1`为搬运起点的平台，其中四个物块的`SuckPoint`为吸盘的吸附中心点；`Platform2`为搬运终点的平台，其中`PlacePoint`为物块放置中心点；`Pond`为染色池，`Start`和`End`分别为起点和终点位置。PS：以上均只对位置进行了规定，但由于误差的存在，建议在规划时留一定的余量。
- 吸盘的吸附条件：吸盘与吸附中心点的Z轴夹角应小于$5^{\circ}$，吸附位置应在吸附中心点为圆心、半径为0.02m的圆内，吸盘离物体的距离不能超过0.005m。
- 在运行过程中、暂停时可以读取机械臂位置、速度、加速度和吸盘开关的状态，如下图所示。PS：停止会直接关闭。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250310144640863.png)
> 图片来源于实验要求

### Robot/Script.py
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250310144840873.png)


- `sysCall_init()` 完成各关节角的计算
- `sysCall_actuation()`中将规划好的关节角通过`move(q, state)`函数传输给机械臂。
- `move(q, state)`：
  - `q`:机械臂各关节角度，数据类型`6*1 ndarray`，**单位rad**；
  - `state`，吸盘开关，数据类型`bool`。
  - 返回值：运行成功与否，数据类型`bool`。

```python title="例程，拿起一个物块，停一下再扔掉" hl_lines="2 3"
if t < 5.2:
    q = trajPlaningDemo(self.q0, self.q1, t, 5) # return the joint angles at time t
    state = False # vacumm gripper is off
    
# vacumm gripper takes effect from t=5.2s to 5.5s    
elif t < 5.5:
    q = self.q1      # keeps the robot still at q1
    state = True  # vacumm gripper is on

# lift a block and move to q2    
elif t < 8.7:
    q = trajPlaningDemo(self.q1, self.q2, t-5.5, 3)
    state = True

# release the vaccum gripper
elif t < 9:
    q = self.q2 
    state = False
else:
    # robot moves from q2 to q0 within 5s
    q = trajPlaningDemo(self.q2, self.q0, t-9, 5)
    state = False
```

| 时间 (秒) | 任务描述 | 夹持器状态 |
|-----------|----------|------------|
| 0 - 5.2 | 机器人从 `q0` 移动到 `q1` | ❌ 关闭 |
| 5.2 - 5.5 | 机器人停留在 `q1`，夹持器启动 | ✅ 开启 |
| 5.5 - 8.7 | 机器人从 `q1` 移动到 `q2`（搬运物体） | ✅ 开启 |
| 8.7 - 9 | 机器人停在 `q2`，夹持器关闭（释放物体） | ❌ 关闭 |
| 9 - 14 | 机器人从 `q2` 移动回 `q0` | ❌ 关闭 |
| > 20 | 停止仿真 | ❌ 关闭 |

### 问题与解决

!!! question "Traceback (most recent call last): UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbb in position 27: invalid start byte"
    检查路径中是否有中文地址，改成英文

!!! question "AttributeError: module 'IK' has no attribute 'IKSolver'"
    在`.py`文件的开头，修改正确的IK文件夹的位置


## 仿真实验1：机械臂正、逆运动学求解



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
   - 第一组：$\left(\frac{\pi}{6}, 0,\frac{\pi}{6}, 0, \frac{\pi}{3}, 0\right)$
   - 第二组：$\left(\frac{\pi}{6}, \frac{\pi}{6}, \frac{\pi}{3}, 0,\frac{\pi}{3},  \frac{\pi}{6}\right)$
   - 第三组：$\left(\frac{\pi}{2}, 0, \frac{\pi}{2}, -\frac{\pi}{3}, \frac{\pi}{3}, \frac{\pi}{6}\right)$
   - 第四组：$\left(-\frac{\pi}{6}, -\frac{\pi}{6}, -\frac{\pi}{3}, 0, \frac{\pi}{12}, \frac{\pi}{2}\right)$
   - 第五组：$\left(\frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}, \frac{\pi}{12}\right)$
4. 将以上5组关节角分别输入仿真程序，将仿真得到的末端位姿与第3步得到的计算结果进行比对。
5. 写出ZJU-I型桌面机械臂的逆运动学解析解（可选）；
6. 将如下5组末端位姿参数分别代入逆运动学解（可使用自带的逆运动学求解器进行相关计算），计算对应的5组关节角；
   - 第一组：$(0.117,0.334,0.499,-2.019,-0.058, -2.190)$
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

||$\alpha$|$a$|$d$|$\theta$|
|---|---|---|---|---|
|1|0|0|0.23|$\theta_1$|
|2|$-\pi/2$|0|-0.054|$\theta_2-\pi/2$|
|3|0|0.185|0|$\theta_3$|
|4|0|0.170|0.077|$\theta_4+\pi/2$|
|5|$\pi/2$|0|0.077|$\theta_5+\pi/2$|
|6|$\pi/2$|0|0.0855|$\theta_6$|


### 正运动学

!!! note "任务在要求干什么"
    1. 在仿真软件中，输入要求的关节角，从起始位置运动到这个要求的位置
    2. 通过手算/matlab/python，计算出末端执行器最后的变换矩阵
    3. 将计算出的末端执行器的位置和姿态与仿真软件中的结果进行比对


**仿真软件执行**

```python title="仿真软件当中执行的代码"
def sysCall_actuation():
    q0 = np.zeros(6) # initialize q0 with all zeros
    q1 = np.array([np.pi/6, 0, np.pi/6, 0, np.pi/3, 0])
    q2 = np.array([np.pi/6, np.pi/6, np.pi/3, 0, np.pi/3, np.pi/6])
    q3 = np.array([np.pi/2, 0, np.pi/2, -np.pi/3, np.pi/3, np.pi/6])
    q4 = np.array([-np.pi/6, -np.pi/6, -np.pi/3, 0, np.pi/12, np.pi/2])
    q5 = np.array([np.pi/12, np.pi/12, np.pi/12, np.pi/12, np.pi/12, np.pi/12])

    t = sim.getSimulationTime()
    q = trajPlaningDemo(q0, q1, t, 2) # 修改这里改成不同的点
    print(sim.getObjectPosition(sim.getObject('/Robot/SuctionCup/SuctionCup_end'))+sim.getObjectOrientation(sim.getObject('/Robot/SuctionCup/SuctionCup_end'))) # 输出位置信息
    a = move(q,0)
```


**解算变换矩阵，计算末端参数**


需要特别注意的点：

- 注意DH参数表当中的单位，图片中的单位是毫米，软件当中是米
- 注意$\theta$的初始值，需要保证$\theta_i = 0$时候，机械臂初始位姿正确($\pm\frac{\pi}{2}$的原因)
- 需要特别注意最后的欧拉角表示是XYZ表示方法，所以由旋转矩阵计算欧拉角的时候需要注意更换一下公式；

```Matlab title="使用Matlab计算变换矩阵"
calculate_XYZ_euler_angles([pi/6, 0, pi/6, 0, pi/3, 0],1);
calculate_XYZ_euler_angles([pi/6, pi/6, pi/3, 0, pi/3, pi/6],2);
calculate_XYZ_euler_angles([pi/2, 0, pi/2, -pi/3, pi/3, pi/6],3);
calculate_XYZ_euler_angles([-pi/6, -pi/6, -pi/3, 0, pi/12, pi/2],4);
calculate_XYZ_euler_angles([pi/12, pi/12, pi/12, pi/12, pi/12, pi/12],5);


function calculate_XYZ_euler_angles(theta_values,i)
    fprintf("%d",i);
    % 基础DH参数表
    DH_params_base = [
        0, 0, 0.23, 0;
        -pi/2, 0, -0.054, -pi/2;
        0, 0.185, 0, 0;
        0, 0.170, 0.077, pi/2;
        pi/2, 0, 0.077, pi/2;
        pi/2, 0, 0.0855, 0
    ];

    % 创建完整的DH参数表
    DH_params = DH_params_base;
    for i = 1:length(theta_values)
        DH_params(i, 4) = theta_values(i) + DH_params_base(i, 4);  % 添加theta值
    end

    % 计算最终变换矩阵
    T_final = compute_DH(DH_params);
    fprintf('Position\n');
    disp(T_final(1:3,4));
    
    % 需要特别注意这里是XYZ方法
    R = T_final(1:3, 1:3);

    beta_calc = asin( R(1, 3));
    alpha_calc = atan2(-R(2, 3), R(3, 3));
    gamma_calc = atan2(-R(1, 2), R(1, 1));

    euler_angles_deg = rad2deg([alpha_calc, beta_calc, gamma_calc]); % 转换为弧度
    fprintf('Angle\n');
    disp(euler_angles_deg);
end
```

```matlab title="计算变换矩阵"
function T_final = compute_DH(DH_params)
    n = size(DH_params, 1);  % Number of joints
    T_final = eye(4);
  
    for i = 1:n
        theta_i = DH_params(i, 4);
        d_i = DH_params(i, 3);
        a_i_minus_1 = DH_params(i, 2);
        alpha_i_minus_1 = DH_params(i, 1);
      
        % 计算每个关节的变换矩阵 MDH方法
        T_i = [
            cos(theta_i), -sin(theta_i), 0, a_i_minus_1;
            sin(theta_i) * cos(alpha_i_minus_1), cos(theta_i) * cos(alpha_i_minus_1), -sin(alpha_i_minus_1), -sin(alpha_i_minus_1) * d_i;
            sin(theta_i) * sin(alpha_i_minus_1), cos(theta_i) * sin(alpha_i_minus_1), cos(alpha_i_minus_1), cos(alpha_i_minus_1) * d_i;
            0, 0, 0, 1
        ];
      
        T_final = T_final * T_i;
    end
  
    % 打印最终变换矩阵
    fprintf('Final Transformation Matrix T = \n');
    disp(T_final);
end
```

**对比得到结果**

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250314104911633.png)

### 逆运动学

这里使用`IK`库即可求解基础解

但是需要注意的是，关节角度有限制，所以需要将不符合关节角度限制的解去除。这里使用了`np.all`函数加上逻辑表达式进行判断，简化了逻辑判断

步骤：

1. 使用逆运动学求解器得到解（可能有多个，按照要求选择一个）
2. 将解带入正运动学
3. 观察末端坐标和给定坐标是否一致


```python title="逆运动学求解与验证" hl_lines="21 29" linenums="1"
def sysCall_init():
    sim = require('sim')
    # initialization the simulation
    doSomeInit()    # must have   

    angles_array = np.array([
        [0.117, 0.334, 0.499, -2.019, -0.058, -2.190],
        [-0.066, 0.339, 0.444, -2.618, -0.524, -3.141],
        [0.3, 0.25, 0.26, -2.64, 0.59, -2.35],
        [0.42, 0, 0.36, 3.14, 1, -1.57],
        [0.32, -0.25, 0.16, 3, 0.265, -0.84]
    ])
    
    iks = IK.IKSolver()
    i = 2 # 手动从0-4
    angles = iks.solve(angles_array[i])
    
    min_vals = np.radians([-200, -90, -120, -150, -150, -180])
    max_vals = np.radians([200, 90, 120, 150, 150, 180])

    valid_columns = ((min_vals[:, None] <= angles) & (angles <= max_vals[:, None])).all(axis=0) # 验证是否在范围内
    valid_angles = angles[:, valid_columns].transpose() # 把符合条件的列提取出来
    print(valid_angles)
    global test_example
    test_example = valid_angles[0] # 从符合的样例当中抽选一个
    
    
def sysCall_actuation():
    t = sim.getSimulationTime()
    q = trajPlaningDemo(q0, test_example, t, 2)
    a = move(q,0)
    if(t>2.5):
        print(sim.getObjectPosition(sim.getObject('/Robot/SuctionCup/SuctionCup_end'))+sim.getObjectOrientation(sim.getObject('/Robot/SuctionCup/SuctionCup_end')))
        sim.pauseSimulation() # 暂停,也可以使用stopSimulation()
```

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250314102228374.png)

可以看到红框的部分是一致的，可以验证了逆运动学的正确性

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

    1）组号-实验报告`.docx/pdf`（推荐pdf）<br>
    2）组号-代码文件`.rar/zip`：Coppeliasim仿真软件的`.ttt`文件及包含的其他代码文件<br>
    3）组号-仿真结果`.mp4/mov/其他视频文件`格式：机械臂轨迹规划仿真实验的录屏文件（文件大小应小于50Mb，推荐使用`Win+G`中的“捕获”进行录制）<br>

## 实物实验1：六自由度机械臂物体抓取与放置实验

1. 编写程序控制ZJU-I型机械臂，实现木块抓取与搬运，具体流程为：
   - 机械臂从零位置启动，运行至起始区域；
   - 启动真空吸爪，抓取起始区域内的木块，移动至A点$(370,-90,115)$；
   - 移动过程中控制木块从A点沿直线路径运动至B点$(288,-288,115)$；
   - 控制从B点到达目标区域，目标区域位置为机械臂1号关节旋转角度$90^\circ$所在位置；
   - 抓取第二个木块放置到目标区域，并堆叠在第一个模块上，二者姿态保持一致；
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
