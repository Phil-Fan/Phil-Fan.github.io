# 环境配置与工具使用记录


## huggingface

[Hugging Face Forums - Hugging Face Community Discussion](https://discuss.huggingface.co/)


[OSError: We couldn‘t connect to ‘https://huggingface.co‘ to load this file, couldn‘t find it(亲测有效)\_checkout your internet connection or see how to ru-CSDN博客](https://blog.csdn.net/l8947943/article/details/143099409)



1. 科学上网，访问该网址
通过全局代理的方式，实现模型的下载。

1. 使用镜像网址
国内huggingface镜像地址：https://hf-mirror.com/
往下翻，直接可看到使用教程。主要有四种解决方式。最直接的方式就是一个个下载使用。

1. 在代码中增加设置
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'



## Attention is All You Need 论文复现

选择[hyunwoongko/transformer: Transformer](https://github.com/hyunwoongko/transformer): PyTorch Implementation of "Attention Is All You Need"进行复现


这个库并没有提供`requirements.txt`，所以需要手动安装，所以会遇到一些奇怪的问题，这里放一下我的解决方案

### 问题1 conda环境问题

- [miniconda安装](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda)

```shell title="conda换源"
conda config --add channels conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/
conda config --set show_channel_urls yes
```

```shell title="创建环境"
conda create -n transformer python=3.10
```

```shell title="激活环境"
conda activate transformer
```

```shell title="安装torchtext"
conda install torchtext==0.13.1
```

```shell title="安装torchdata"
conda install torchdata==0.4.1
```

> [艰辛的torchtext安装旅程 - 知乎](https://zhuanlan.zhihu.com/p/598841083)


### 问题2 mkl降级
[解决lib/python3.7/site-packages/torch/lib/libtorch_cpu.so: undefined symbol: iJIT_NotifyEvent_python_皮卡兔子屋-2048 AI社区](https://2048.csdn.net/682d3789606a8318e85865cc.html?dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTk4OTc1LCJleHAiOjE3NTIyNDk0OTYsImlhdCI6MTc1MTY0NDY5NiwidXNlcm5hbWUiOiJQaGxpRmFuIn0.1FEb7DOwlbsLHbG-UjecQRWeRotMNeiLvlZ3V2dUdW4)

遇到了`/site-packages/torch/lib/libtorch_cpu.so: undefined symbol: iJIT_NotifyEvent`

对mkl进行降级

```shell title="mkl"
conda install mkl=2024.0
```

### 问题3 libfii库出错
```
ImportError: /usr/lib/x86_64-linux-gnu/libp11-kit.so.0: undefined symbol: ffi_type_pointer, version LIBFFI_BASE_7.0
```
[Conda虚拟环境下libp11-kit.so.0: undefined symbol: ffi_type_pointer...问题解决-CSDN博客](https://blog.csdn.net/qq_38606680/article/details/129118491)

```shell title="libffi"
ls -l | grep libffi
mv libffi.so.7 libffi_bak.so.7
sudo ln -s /lib/x86_64-linux-gnu/libffi.so.7.1.0 libffi.so.7
ln -s /lib/x86_64-linux-gnu/libffi.so.7.1.0 libffi.so.7
ldconfig
```

### 问题4 datasets库出错
`ImportError: cannot import name 'load_dataset' from 'datasets' (unknown location)`

```shell title="datasets"
pip install datasets
# 或者在 conda 环境中
conda install -c huggingface datasets
```

### 问题5 torchtext库出错
’No module named ‘torchtext.legacy’

问题出现原因：
1. torchtext is not compatible with new versions of Numpy
2. torchtext current version don't have "from torchtext.legacy.data import Field, BucketIterator"

解决方法：
修改代码，参照[Fixed 'data_loader.py' by Faizanfarhad · Pull Request #35 · hyunwoongko/transformer](https://github.com/hyunwoongko/transformer/pull/35)

### 问题6 spacy库安装


`OSError: [E050] Can't find model 'de_core_news_sm'. It doesn't seem to be a Python package or a valid path to a data directory.`

```shell title="spacy"
pip install spacy
python -m spacy download de_core_news_sm
python -m spacy download en_core_web_sm
```



```shell title="spacy"
pip install -U spacy==3.6.0
python -m spacy download en_core_web_sm
python -m spacy download zh_core_web_sm
python -m spacy download de_core_news_sm
```

```shell title="如果网络有问题，可以直接下载后本地安装"
wget https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.6.0/de_core_news_sm-3.6.0-py3-none-any.whl
wget https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl
wget https://github.com/explosion/spacy-models/releases/download/zh_core_web_sm-3.6.0/zh_core_web_sm-3.6.0-py3-none-any.whl
pip install zh_core_web_sm-3.6.0-py3-none-any.whl de_core_news_sm-3.6.0-py3-none-any.whl en_core_web_sm-3.6.0-py3-none-any.whl
```

```shell title="numpy降版本"
pip install numpy==1.26.4
```


### 问题7 Multi30k数据集下载
`Could not get the file at http://www.quest.dcs.shef.ac.uk/wmt16_files_mmt/training.tar.gz. [RequestException] None.`

```shell title="wmt16_files_mmt"
wget http://www.quest.dcs.shef.ac.uk/wmt16_files_mmt/training.tar.gz
```

https://github.com/neychev/small_DL_repo/tree/master/datasets/Multi30k

并将三个文件放在`/root/.cache/torch/text/datasets/Multi30k`（本目录根据个人有所变化）

但是这一招对我并不管用。

所以我直接修改了`data_loader.py`，使用本地数据集进行加载

### 训练结果

这里使用的是Multi30K数据集

en2de训练结果

![image-20250706135450331](assets/00-Settings.assets/image-20250706135450331.png)

de2en训练结果

![image-20250706135404376](assets/00-Settings.assets/image-20250706135404376.png)



## llama-factory 使用记录

!!! note "Llama-factory"
    Llama-factory 是一个用于大规模语言模型（LLM）训练和推理的框架。它提供了一套工具和接口，简化了从数据准备到模型部署的整个流程。Llama-factory 支持多种模型架构和数据集，允许用户根据自己的需求进行定制和扩展。通过集成的 WebUI，用户可以方便地管理模型训练过程，调整参数，并实时监控训练进度和性能指标。此外，Llama-factory 还支持分布式训练和推理，能够有效利用多台机器的计算资源，提高模型的训练效率和推理速度。

### 安装与使用

- 中文教程[安装 - LLaMA Factory](https://llamafactory.readthedocs.io/zh-cn/latest/getting_started/installation.html)
- [LLaMA-Factory 微调教程】LoRA 微调 改变大模型的自我认知 - 知乎](https://zhuanlan.zhihu.com/p/24909312513)

这里使用AutoDL上的社区镜像

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112920092478120&bvid=BV1a3aQeuEou&cid=500001641377964&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>



### 实战记录 —— 微调qwen实现Multi30K下英译德翻译模型


使用的是Multi30K数据集，下载地址：https://github.com/neychev/small_DL_repo/tree/master/datasets/Multi30k


#### 下载模型

下载`Qwen2.5-7B-Instruct`模型，放在`/root/Qwen2.5-7B-Instruct`下

#### 准备数据

根据sft的格式，整理数据，按照instruction, input, output格式


```json title="整理数据，按照instruction, input, output格式"
{
    "instruction": "Translate the following English text to German.", 
    "input": "Two young, White males are outside near many bushes.", 
    "output": "Zwei junge weiße Männer sind im Freien in der Nähe vieler Büsche."
}
```

### 开启webui

开启webui之后，操作比较简单，只需要选择对应的模型，修改参数，填写对应路径，即可进行训练
![webui](assets/exp.assets/webui.png)




#### 进行训练

- PEFT 0.12.0
- Transformers 4.45.2
- Pytorch 2.4.1+cu121
- Datasets 2.21.0
- Tokenizers 0.20.1

可以中途切断，loss不需要太低

![loss](assets/exp.assets/loss.png)

```shell title="训练命令 基本是默认的参数"
llamafactory-cli train \
    --stage sft \
    --do_train True \
    --model_name_or_path /root/LLaMA-Factory/src/output/en2de \
    --preprocessing_num_workers 16 \
    --finetuning_type lora \
    --template qwen \
    --flash_attn auto \
    --dataset_dir /root/LLaMA-Factory/data \
    --dataset 你的数据集 \
    --cutoff_len 1024 \
    --learning_rate 5e-05 \
    --num_train_epochs 6.0 \
    --max_samples 100000 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 5 \
    --save_steps 100 \
    --warmup_steps 0 \
    --optim adamw_torch \
    --packing False \
    --report_to none \
    --output_dir saves/Qwen2.5-7B-Instruct/lora/train_2025-07-14-22-51-16 \
    --bf16 True \
    --plot_loss True \
    --ddp_timeout 180000000 \
    --include_num_input_tokens_seen True \
    --lora_rank 8 \
    --lora_alpha 32 \
    --lora_dropout 0 \
    --loraplus_lr_ratio 16 \
    --lora_target all 
```


#### API推理

在服务器上执行

```shell title="api.sh"
source activate llama
cd /root/LLaMA-Factory

CUDA_VISIBLE_DEVICES=0 API_PORT=6006 python src/api.py \
    --model_name_or_path /root/LLaMA-Factory/src/output/en2de \
    --template qwen \
```


相当于把这项服务部署到了服务器的端口上，然后通过openai的api进行调用，就可以实现推理 

```python title="api.py"
import openai
import sys

api_key = "EMPTY"
openai.api_base = "http://localhost:6006/v1"


def chat_with_gpt3_5(messages):
    response = openai.ChatCompletion.create(
        model="xxx",
        messages=messages,
        api_key=api_key,
        stream=True  # 启用流式输出
    )

    full_response = ""
    for chunk in response:
        if 'choices' in chunk and len(chunk['choices']) > 0:
            content = chunk['choices'][0].get('delta', {}).get('content', '')
            if content:
                print(content, end='', flush=True)
                full_response += content
    print() 
    return full_response

conversation = [
    {"role": "system", "content": "你是一个聪明的AI"}
]

while True:

    user_input = input("You: ")

    if user_input.lower() == '退出':
        print("Assistant: 再见！")
        break

    conversation.append({"role": "user", "content": user_input})

    print("Assistant: ", end='', flush=True)
    assistant_message = chat_with_gpt3_5(conversation)

    conversation.append({"role": "assistant", "content": assistant_message})
```

则可以在本地浏览器访问`http://localhost:6006`，进行推理，也可以通过api进行调用

下面的代码中我测试了英译德的测试集1000个样本，达到了44.45的bleu分数


[:fontawesome-solid-code:   inference.py](./assets/exp.assets/inference.py){: .md-button .md-button--primary }  

[:fontawesome-solid-code:   bleu.py](./assets/exp.assets/bleu.py){: .md-button .md-button--primary } 


```text title="部分翻译结果"
Original English: 2 blond girls are sitting on a ledge in a crowded plaza.
Translation: 2 blonde Mädchen sitzen auf einer Fassade in einem überfüllten Platz.
Reference German: 2 blonde Mädchen sitzen auf einem Absatz auf einem belebten Platz.
BLEU score: 66.23282548391518

Original English: A child is splashing in the water
Translation: Ein Kind macht im Wasser Platsch.
Reference German: Ein Kind planscht im Wasser.
BLEU score: 66.64762996818769

Original English: Three people sit at a picnic table outside of a building painted like a union jack.
Translation: Drei Personen sitzen an einem Picknicktisch vor einem Gebäude, das wie ein Union Jack gemalt ist.
Reference German: Drei Leute sitzen an einem Picknicktisch vor einem Gebäude, das wie der Union Jack bemalt ist.
BLEU score: 85.15116314550686
```


```shell title="翻译结果"
Translation English to German and calculating BLEU scores...
100%|█████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [09:52<00:00,  1.69it/s]
Average BLEU score for DE to EN: 44.44732087434253
```



### 问题解决


1. 模型问题，下载模型
- 如果下载出现问题，会报错
```
safetensors_rust.SafetensorError: Error while deserializing header: MetadataIncompleteBuffer
```

2. 模版问题：使用`llama3`模版：可以在   `template.py` 中添加自己的对话模板。
3. lora问题

```
ValueError: Target modules {'c_attn'} not found in the base model. Please check the target modules and try again.
```

改成`q_proj,v_proj`

```
--lora_target q_proj,v_proj
```


