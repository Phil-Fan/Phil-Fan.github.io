# 机械臂


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

