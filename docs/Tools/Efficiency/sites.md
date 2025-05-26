# AI产品整理与使用

!!! Where to find good AI tools?
    [Product Hunt – The best new products in tech.](https://www.producthunt.com/)




## AI4sci
### LLM + 科研

人工智能的一个重大挑战是开发能够进行科学研究和发现新知识的智能体。尽管前沿模型已经被用于辅助人类科学家，例如用于头脑风暴或编写代码，但它们仍然需要大量的人工监督或被严格限制在特定任务上。

“AI科学家”，这是第一个全面的系统，能够实现完全自动化的科学发现，使基础模型（如大型语言模型，LLMs）能够独立进行研究。

[SakanaAI/AI-Scientist: The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery 🧑‍🔬](https://github.com/SakanaAI/AI-Scientist?tab=readme-ov-file)

- 全自动化研究流程：AI Scientist能独立完成科学研究的全过程，从构思、编码、实验到撰写论文，实现研究流程的端到端自动化。
- 多领域应用能力：系统不仅限于单一领域，而是能跨足机器学习的不同子领域，如扩散模型、变换器模型以及学习动力学等，显示出广泛的适用性。
- 高效的计算效率：AI Scientist在生成每篇论文时的成本极低，大约只需15美元，显著降低了科学研究的经济门槛，有助于推动研究的民主化。
- 创新的同行评审机制：引入了自动化的同行评审过程，能以接近人类的准确性评估生成的论文，为研究质量提供了保障。
- 迭代知识积累：通过开放式循环，AI Scientist能将先前的想法和反馈用于改进后续的研究方向，模拟了人类科学社区的迭代发展过程。

<iframe src="https://github.com/SakanaAI/AI-Scientist/blob/main/example_papers/adaptive_dual_scale_denoising.pdf" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/anim-ai-scientist.gif)

#### Setting Up the Templates
This section provides instructions for setting up each of the three templates used in our paper. Before running The AI Scientist experiments, please ensure you have completed the setup steps for the templates you are interested in.

=== "NanoGPT Template"
    Description: This template investigates transformer-based autoregressive next-token prediction tasks.

    Setup Steps:
    ```python title="install data"
    python data/enwik8/prepare.py
    python data/shakespeare_char/prepare.py
    python data/text8/prepare.py
    ```

    Create baseline runs (machine dependent):

    ```bash title="Set up NanoGPT baseline run"
    # NOTE: YOU MUST FIRST RUN THE PREPARE SCRIPTS ABOVE!
    cd templates/nanoGPT
    python experiment.py --out_dir run_0
    python plot.py
    ```
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202200152.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241203003647.png)


=== "2D Diffusion Template"
    Description: This template studies improving the performance of diffusion generative models on low-dimensional datasets.

    ```bash title="Set up 2D Diffusion"
    git clone https://github.com/gregversteeg/NPEET.git
    cd NPEET
    pip install .
    pip install scikit-learn
    ```

    === "Set up 2D Diffusion baseline run" 
    ```bash title="Set up 2D Diffusion baseline run"
    cd templates/2d_diffusion
    python experiment.py --out_dir run_0
    python plot.py
    ```

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241203004920.png)

=== "Grokking Template"
    Description: This template investigates questions about generalization and learning speed in deep neural networks.

    ```bash title="Set up Grokking"
    pip install einops
    ```
    
    ```bash title="Set up Grokking baseline run"
    cd templates/grokking
    python experiment.py --out_dir run_0
    python plot.py
    ```



#### Run AI Scientist Paper Generation Experiments


Note: Please ensure the setup steps above are completed before running these experiments.



```bash
conda activate ai_scientist
# Run the paper generation.
python launch_scientist.py --model "gpt-4o-2024-05-13" --experiment nanoGPT_lite --num-ideas 2
python launch_scientist.py --model "claude-3-5-sonnet-20241022" --experiment nanoGPT_lite --num-ideas 2
If you have more than one GPU, use the --parallel option to parallelize ideas across multiple GPUs.
```




#### Getting an LLM-Generated Paper Review

```python
import openai
from ai_scientist.perform_review import load_paper, perform_review

client = openai.OpenAI()
model = "gpt-4o-2024-05-13"

# Load paper from PDF file (raw text)
paper_txt = load_paper("report.pdf")

# Get the review dictionary
review = perform_review(
    paper_txt,
    model,
    client,
    num_reflections=5,
    num_fs_examples=1,
    num_reviews_ensemble=5,
    temperature=0.1,
)

# Inspect review results
review["Overall"]    # Overall score (1-10)
review["Decision"]   # 'Accept' or 'Reject'
review["Weaknesses"] # List of weaknesses (strings)
```
### 长上下文 大模型

[CraftJarvis/RAT: Implementation of "RAT: Retrieval Augmented Thoughts Elicit Context-Aware Reasoning in Long-Horizon Generation".](https://github.com/CraftJarvis/RAT)

<iframe src="https://arxiv.org/pdf/2403.05313" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>

## 常用Prompt

### OCR公式


### 扩写

#### 扩充关键词
如果在写作过程中只有简单的思路或者只有简单N个关键字，可以使用ChatGPT帮你扩充思路
```
As a top expert in the [specific field], please elaborate and explain the related viewpoints and concepts based on the ideas I provide.

提示：你作为[某某专业]领域的顶尖专家，请根据我提供的思路，详细展开并解释相关观点和观念。
```

#### 扩充内容
```
Please refer broadly to similar papers in the [specific field], and help me add three subheadings under the main heading of "Research Background and Significance". Also, write the main content for these three subheadings. 提示：请广泛参考[某某领域]同类论文，帮我在【研究背景和意义】这一级目录下面，再增加三个子目录，并写出三个子目录的主要内容。
```



## cursor

https://i-blog.csdnimg.cn/direct/b4dfeec741cd4832a8038883ee85cded.png

## AI+日程管理：Dola 智能助手
[Dola - AI 日历助手](https://heydola.com/zh)

可以使用订阅连接集成到你的日历当中

- 支持语音输入
- 支持中文
- 支持推文转发总结


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202192248.png)

## LLM 平台

### 硅基流动
第一步：注册账号，绑定手机号
[SiliconFlow, Accelerate AGI to Benefit Humanity](https://siliconflow.cn/zh-cn/?ref=aishenqi.net)
第二步：逛模型广场

[Cherry Studio 下载页面](https://cherry-ai.com/download)

### 豆包

#### 搭建你的第一个Agent


### Kimi K0-math

在中考、高考、考研以及包含入门竞赛题的 MATH 等 4 个数学基准测试中，k0-math 超过了 o1-mini 和 o1-preview。


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202194406.png)



![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202194530.png)


接下来给它上点强度，2022 年全国新课标 1 卷的单选压轴题： 

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202194618.png)

这道题乍一看挺难，实则一点也不容易。
虽然是一道立体几何，但想要做对需要绕好几个弯。首先要将正四棱锥的体积表示为关于高（或侧棱长）的函数，接着对这个函数求导才能得到答案。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202194651.png)


弱智吧测试

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202194741.png)

> 当被问及“长文本是登月的第一步，数学模型和深度推理是第几步”。
> 杨植麟回答：“就是第二步。”

### ChatGPT
#### 常见问题


#### 使用

#### API调用

### Claude


### Perplexity


## 其他好玩的网站

### 信息检索
[中国个人信息生成器](http://fangjiayun.net/apps/random-userinfo.html)

[Generate a Random Name - Fake Name Generator](https://www.fakenamegenerator.com/)

[thispersondoesnotexist.com (1024×1024)](https://thispersondoesnotexist.com/)

