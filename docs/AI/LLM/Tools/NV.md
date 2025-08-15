# NVIDIA相关工具

## Nsight System 下载

### 安装
`nsys` 是 NVIDIA Nsight Systems 的命令行工具，可以用于分析 CUDA 应用程序的性能和行为


[Jetson Nano - Nsight Systems target not supported - Nsight Systems / Profiling Embedded Targets - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/jetson-nano-nsight-systems-target-not-supported/256990)

[How to use Nvidia Nsight Systems remote session using SSH - Nsight Systems / Profiling Linux Targets - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/how-to-use-nvidia-nsight-systems-remote-session-using-ssh/222960/6)

[Nsight System经验 | 奔跑的IC](https://zmurder.github.io/CUDA/Nsight/Nsight%20System%E7%BB%8F%E9%AA%8C/)

[The Study of Nsight Systerm – 子暘的blog](https://zhangweihao.cn/the-study-of-nsight-systerm/)


### Nsight System 安装

下载地址为：https://developer.nvidia.com/nswight-systems。

```shell
chmod +x <installer-name>.run
./<installer-name>.run
```

添加 nsys 到系统的 PATH 环境变量中。为了能够在终端中直接使用 nsys 命令，您需要将安装目录中的 bin 文件夹添加到系统的 PATH 环境变量中。可以使用以下命令将 nsys 添加到 PATH 环境变量中：

```shell title="换成实际安装路径"
export PATH="/opt/nvidia/nsight-systems/bin:$PATH"
```


nsys profile --trace=cuda,cudnn,cublas,osrt,nvtx python demo.py


[vLLM性能分析案例 - 知乎](https://zhuanlan.zhihu.com/p/18702718502)

https://developer.nvidia.com/zh-cn/blog/profiling-llm-training-workflows-on-nvidia-grace-hopper/


### 操作
- [Nsight Systems - 油管官方教程](https://www.youtube.com/playlist?list=PL5B692fm6--uxmZ5qUnF-y5xaF8enRZGg)
  - [Nsight Systems Timeline - YouTube](https://www.youtube.com/watch?v=TGChXcFm-Yo)，[如何在 CUDA C/C++ 中重叠数据传输 |NVIDIA 技术博客 --- How to Overlap Data Transfers in CUDA C/C++ | NVIDIA Technical Blog](https://developer.nvidia.com/blog/how-overlap-data-transfers-cuda-cc/)

- zoom in: 
  - 选中区域`shift + z`
  - ctrl+滚轮
- `backspace ` 返回上一个视图


using the overlapping of tasks to improve the performance is called `latency hiding`


- speed of light 
- 计算比率



Nsight Compute

- roofline Analysis
- Memory Chart