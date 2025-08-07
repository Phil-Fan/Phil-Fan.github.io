---
status: new
---

# 07 | LLM 评估与监控

!!! note "正在施工中👷.. "


## Benchmark 基准测试

LLM（Large Language Model）基准测试（benchmarking）是评估大型语言模型性能的关键方法，benchmark_latency和benchmark_serving是用于评估机器学习模型性能的两个重要方面，尤其是在部署和实际应用中。它们的目标是确保模型在不同条件下具有良好的响应时间和服务能力。

### Benchmark Latency

Latency 是指从输入数据发送到模型，直到模型返回预测结果之间所花费的时间。在机器学习模型的评估中，benchmark_latency 主要关注以下方面：

- **Inference Time**: 单次推理所需的时间，包括模型加载、数据预处理、推理过程以及后处理
- **Throughput**: 每秒处理的请求数，通常与延迟成反比关系
- **Consistency**: 在不同负载条件下，延迟是否保持稳定，是否存在明显的抖动或延迟尖峰

### Benchmark Serving

Serving 是指在生产环境中部署和运行模型，以处理实际的用户请求。benchmark_serving 关注模型在生产环境中的整体性能和稳定性，包括：

- **Scalability**: 系统在增加负载时能否有效扩展，保持高性能
- **Reliability**: 系统的可靠性，包括在高负载或异常情况下的稳定性
- **Resource Utilization**: 评估CPU、GPU、内存等资源的使用情况，确保在高效利用资源的同时保持高性能
- **Latency under Load**: 在高并发请求下，系统的延迟表现


### 压力测试核心指标

| 指标类别 | 指标名称 | 含义 | 单位 | 典型阈值 |
|---------|---------|------|------|---------|
| **延迟类** | P50 latency | 50% 请求完成时间 | ms | < 100 ms |
| | P90 latency | 90% 请求完成时间 | ms | < 200 ms |
| | P99 latency | 99% 请求完成时间 | ms | < 500 ms |
| | TTFT (Time To First Token) | 首 token 延迟 | ms | < 50 ms |
| | TPOT (Time Per Output Token) | 每输出 token 延迟 | ms | < 20 ms |
| **吞吐类** | QPS (Queries Per Second) | 每秒查询数 | req/s | 取决于模型规模 |
| | TPS (Tokens Per Second) | 每秒生成 token 数 | tokens/s | 取决于 GPU 数量 |
| | Goodput | 成功请求占比 | % | > 99% |
| **资源类** | GPU 利用率 | GPU 计算单元使用率 | % | 80-95% |
| | GPU 显存占用 | 显存使用比例 | % | < 90% |
| | CPU 利用率 | CPU 计算单元使用率 | % | < 80% |
| | 网络带宽 | 网络传输速率 | Gbps | 视部署规模而定 |
| **稳定性类** | 错误率 | 失败请求占比 | % | < 1% |
| | 超时率 | 超时请求占比 | % | < 0.1% |
| | 重启次数 | 服务重启频率 | 次/小时 | 0 |
| **扩展性类** | 并发用户数 | 同时在线用户数 | 人 | 视业务需求 |
| | 队列长度 | 等待处理请求数 | 个 | < 100 |
| | 自动扩缩容时间 | 弹性伸缩耗时 | s | < 30 s |



## 压测工具

### vLLM 内置压测
LLM 公开了一些指标，可用于监控系统的健康状况。这些指标通过 vLLM OpenAI 兼容 API 服务器上的 `/metrics` 端点公开。


[生产指标 — vLLM 文档](https://docs.vllm.com.cn/en/latest/serving/metrics.html)

vLLM 提供了内置的基准测试工具，用于评估模型性能。

```shell
TORCH_CUDA_ARCH_LIST="8.9"
MODEL_NAME="Qwen/QwQ-32B-AWQ"
NUM_PROMPTS=1000
DATASET_NAME="sharegpt"
DATASET_PATH="/root/autodl-tmp/jacky/benchmark/ShareGPT_V3_unfiltered_cleaned_split.json"
MAX_MODEL_LEN=1024
python3 vllm/benchmarks/benchmark_throughput.py \
  --model "${MODEL_NAME}" \
  --dataset-name "${DATASET_NAME}" \
  --dataset-path "${DATASET_PATH}" \
  --num-prompts "${NUM_PROMPTS}" \
  --max-model-len ${MAX_MODEL_LEN}
```

### SGLang Benchmark

SGLang 框架提供的基准测试工具，用于评估 SGLang 应用的性能表现。


### EvalScope

来自 ModelScope 的评估工具，提供全面的模型评估能力。

### GenAI-Perf

专门为生成式AI设计的性能评估工具。

### 其他压测工具

[FlyAIBox/llm_benchmark](https://github.com/FlyAIBox/llm_benchmark) 是一个专门用于大模型推理压测的开源工具。





## 监控工具

### GPU 监控

#### nvitop

nvitop 是一个实时监控 GPU 各项核心指标的工具，支持终端交互式查看。

**主要功能：**
- 实时 GPU 利用率监控
- 显存占用情况
- GPU 温度监控
- 进程级别的 GPU 使用情况
- 终端交互式界面

#### nvitop-exporter

将 GPU 指标转换为 Prometheus 兼容格式的工具，通过 HTTP 接口暴露数据。

**主要功能：**
- GPU 指标数据转换
- Prometheus 格式输出
- HTTP 接口暴露
- 与监控系统集成


### Prometheus

Prometheus 是一个开源的监控和告警系统，用于数据采集与存储。

**主要功能：**
- 时序数据存储
- 数据查询语言
- 告警规则配置
- 服务发现
- 高可用性支持



## 可视化工具

### Grafana

Grafana 是一个开源的数据可视化和监控平台。

**主要功能：**
- 丰富的图表类型
- 多数据源支持
- 仪表盘定制
- 告警通知
- 用户权限管理

### Streamlit

Streamlit 是一个用于快速构建数据应用的 Python 库。

**主要功能：**
- 快速原型开发
- 交互式数据展示
- 机器学习模型展示
- 实时数据更新

### 夜莺

夜莺是一个开源的监控告警系统，提供完整的监控解决方案。

**主要功能：**
- 数据采集
- 数据存储
- 告警管理
- 可视化展示

### TensorBoard

TensorBoard 是 TensorFlow 的可视化工具，也可用于其他深度学习框架。

**主要功能：**
- 训练过程可视化
- 模型结构展示
- 性能指标跟踪
- 参数分布分析

### WandB (Weights & Biases)

WandB 是一个用于机器学习实验跟踪的平台。

**主要功能：**
- 实验管理
- 模型版本控制
- 性能指标跟踪
- 团队协作

### SwanLab

SwanLab 是一个轻量级的实验跟踪工具。

**主要功能：**
- 实验记录
- 指标可视化
- 模型比较
- 简单易用


## 相关资源


- [基于 nvitop+Prometheus+Grafana 的物理资源与 VLLM 引擎服务监控方案](https://blog.csdn.net/xiangyuanhong08/article/details/148011686)
- [使用 Prometheus、Grafana、Loki 和 Alloy 在 Google GKE 上监控 Streamlit 应用程序](https://medium.com/@omarnour_5895/monitoring-a-streamlit-app-on-gke-with-grafana-loki-alloy-4d1bad572c01)