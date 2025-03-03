# 机械臂
## Coppeliasim

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


## Pybullet环境配置

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

## 真实机械臂控制