# Jetson Orin Nano 


## 简介

NVIDIA Jetson Orin Nano 是 NVIDIA 推出的一款小型但功能强大的边缘 AI 和机器人计算设备。它是 Jetson 系列中最新的入门级产品，基于 NVIDIA 的 Ampere 架构。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250318091806079.png)
> 图源 [NVIDIA Jetson Orin Nano 开发板](https://developer.nvidia.com/embedded/jetson-orin-nano-developer-kit)

主要特点：
- 计算性能：高达 40 TOPS 的 AI 性能
- CPU：6核 Arm Cortex-A78AE
- GPU：NVIDIA Ampere 架构 GPU，具有 512 个 NVIDIA CUDA 核心
- 内存：8GB 64位 LPDDR5
- 存储：支持 NVMe SSD
- 功耗：5W-15W，可配置

应用场景：
- 边缘 AI 计算
- 机器人控制
- 计算机视觉
- 自动驾驶
- 智能监控
- IoT 设备

Jetson Orin Nano 是 Jetson Nano 的升级版，算力提升了80倍，高达 40 TOPS（每秒万亿次）的计算性能，为曾经难以企及的复杂 AI 模型铺平了道路

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250318091411215.png)

## 刷机与环境配置

官方教程：[🚀 初始设置指南 - Jetson Orin Nano](https://www.jetson-ai-lab.com/initial_setup_jon.html)

> 参考教程
> [Jetson 开发系列：Orin Nano 开箱！一款强大的嵌入式&物联网开发板\_jetson orin nano算力-CSDN博客](https://blog.csdn.net/u010522887/article/details/142677847)


[SDK Manager | NVIDIA 开发者](https://developer.nvidia.cn/sdk-manager)


```shell title="jetpack jtop installment"
sudo apt update
sudo apt dist-upgrade
sudo reboot
sudo apt install nvidia-jetpack
```


安装jtop，可以用来监控jetson的资源使用情况和查看cuda版本等。

```shell title="jtop usage"
sudo -H pip3 install -U pip
sudo -H pip install jetson-stats
```


```shell title="验证"
nvcc -V
```



!!! question "A module that was compiled using NumPy 1.x cannot be run in NumPy 2.0.0"

    i fix this problem using the experience on [here](https://stackoverflow.com/questions/78641150/a-module-that-was-compiled-using-numpy-1-x-cannot-be-run-in-numpy-2-0-0)

    ```shell
    pip uninstall numpy
    pip install numpy==1.26.4
    ```



[jp6/cu126 index](https://pypi.jetson-ai-lab.dev/jp6/cu126)

[Jetson Zoo - eLinux.org](https://elinux.org/Jetson_Zoo)