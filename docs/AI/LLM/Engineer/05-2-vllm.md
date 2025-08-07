---
status: new
comments: True
--- 

# vLLM
!!! note "正在施工中👷.. "

[vLLM - vLLM 文档](https://docs.vllm.com.cn/en/latest/index.html)

## 安装

<!-- termynal -->

```shell title="安装"
> uv venv --python 3.12 --seed
> source .venv/bin/activate
> uv pip install vllm --torch-backend=auto
---> 100%
Installed
```


## 使用







## tricks

### LMcache
[LMCache - vLLM --- LMCache - vLLM](https://docs.vllm.ai/en/stable/examples/others/lmcache.html#1-disaggregated-prefill-in-vllm-v1)


<!-- termynal -->

```shell
> uv venv --python 3.12 --seed
> source .venv/bin/activate
> uv pip install vllm --torch-backend=auto
---> 100%
Installed
```

<br>

<!-- termynal -->


```shell
> uv pip install lmcache
> uv pip install nixl
> uv pip install vllm
> uv pip install pandas
> uv pip install datasets
---> 100%
Installed
```

```shell
cd vllm/examples/others/lmcache/disagg_prefill_lmcache_v1
```