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

## OCR公式


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

[Cursor - The AI Code Editor](https://www.cursor.com/)

### 快捷键
`Tab`：自动填充

### `Ctrl+K` | 编辑代码

### `Ctrl+L` | 代码问答

回答用户关于代码和整个项目的问题，也可以编辑代码（功能最全面）


<iframe width="560" height="315" src="https://www.youtube.com/embed/QadMS2eKvKM?si=2Oy0HWInK3S3xlS0" title="YouTube video player" frameborder="0" allow="accelerometer;  clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[使用 Cursor 的基本功能全教程（快捷键及其他功能）\_cursor快捷键-CSDN博客](https://blog.csdn.net/zhouzongxin94/article/details/142550632)

[全网最全面详细的Cursor使用教程，让开发变成聊天一样容易-CSDN博客](https://blog.csdn.net/m0_68116052/article/details/142832657)

### `Ctrl+i` | 全项目开发
编辑整个项目代码（跨文件编辑代码）


### `@` | 上下文标记

#### `@Files`
传递指定代码文件的上下文

当你在对话框中输入 `@Files` 注记时，Cursor 会自动弹出你代码仓库的检索列表。你可以输入想要导入上下文的文件名，按下确认键后，相应文件的内容将自动注入到上下文中。



#### `@Code` 
提供更精确的代码片段。使用 `@` 注记的方式类似，都会弹出相应的检索框。你只需输入关键词，然后在索引列表中选择所需的代码块即可。

代码块的识别由你开发环境的 LSP（语言服务器协议）决定，通常情况下识别的准确性较高。



#### `@Docs` 可以从函数或库的官方文档中获取上下文。

目前，它仅能从可访问的在线文档中提取信息。因此，除非你能够提供一个在线地址，否则自己编写的类似 JSDoc 的文档信息是无法被使用的。我个人认为这个功能的适用性有限。



#### `@Web`：从搜索引擎获取上下文
`@Web` 注记类似于一种方法，它会默认先将你的提问发送到搜索引擎，然后从搜索结果中提取上下文供 LLM 使用。然而，由于 Cursor 官方并未公开具体的实现细节，且其功能尚未完全优化，实际使用效果时好时坏。




#### `@Folders`：传递文件目录信息的上下文
`@Folders` 注记可以提供与文件目录相关的信息。如果你遇到路径相关的问题，可以考虑使用这个注记向大模型寻求解决方案。



#### `@Chat`：仅在文件内的代码生成窗口使用
`@Chat` 注记只能在文件内的代码生成窗口（通过 `CTRL + K` 打开的窗口）中使用。它能够将你在右侧打开的对话窗口中的对话内容作为上下文传递给大模型。



#### `@Definitions`：仅在文件内的代码生成窗口使用
与 `@Chat` 注记类似，`@Definitions` 注记也只能在文件内的代码生成窗口中使用。它会将光标所在行代码涉及的变量和类型的相关定义作为上下文传递给大模型，功能类似于 `@Code` 注记。



#### `@Git`：仅在对话窗口使用

对话窗口是指通过 `CTRL + L` 和 `CTRL + I` 打开的窗口。`@Git` 注记能够将你当前 Git 仓库的 commit 历史作为上下文传递给大模型。

这个注记特别适合在代码协作时查看历史记录或进行责任确认时使用。



### 外部知识库



### system prompt

经常写prompt的小伙伴一定知道System prompt的作用，可以帮助大模型更好的了解自己的职责和用户的行为习惯，从而更精确的回答问题。在设置中添加Rules for AI添加System prompt

```
# Role
你是一名极其优秀具有20年经验的产品经理和精通所有编程语言的工程师。与你交流的用户是不懂代码的初中生，不善于表达产品和代码需求。你的工作对用户来说非常重要，完成后将获得10000美元奖励。

# Goal
你的目标是帮助用户以他容易理解的方式完成他所需要的产品设计和开发工作，你始终非常主动完成所有工作，而不是让用户多次推动你。

在理解用户的产品需求、编写代码、解决代码问题时，你始终遵循以下原则：

## 第一步
- 当用户向你提出任何需求时，你首先应该浏览根目录下的readme.md文件和所有代码文档，理解这个项目的目标、架构、实现方式等。如果还没有readme文件，你应该创建，这个文件将作为用户使用你提供的所有功能的说明书，以及你对项目内容的规划。因此你需要在readme.md文件中清晰描述所有功能的用途、使用方法、参数说明、返回值说明等，确保用户可以轻松理解和使用这些功能。

## 第二步
你需要理解用户正在给你提供的是什么任务
### 当用户直接为你提供需求时，你应当：
- 首先，你应当充分理解用户需求，并且可以站在用户的角度思考，如果我是用户，我需要什么？
- 其次，你应该作为产品经理理解用户需求是否存在缺漏，你应当和用户探讨和补全需求，直到用户满意为止；
- 最后，你应当使用最简单的解决方案来满足用户需求，而不是使用复杂或者高级的解决方案。

### 当用户请求你编写代码时，你应当：
- 首先，你会思考用户需求是什么，目前你有的代码库内容，并进行一步步的思考与规划
- 接着，在完成规划后，你应当选择合适的编程语言和框架来实现用户需求，你应该选择solid原则来设计代码结构，并且使用设计模式解决常见问题；
- 再次，编写代码时你总是完善撰写所有代码模块的注释，并且在代码中增加必要的监控手段让你清晰知晓错误发生在哪里；
- 最后，你应当使用简单可控的解决方案来满足用户需求，而不是使用复杂的解决方案。

### 当用户请求你解决代码问题是，你应当：
- 首先，你需要完整阅读所在代码文件库，并且理解所有代码的功能和逻辑；
- 其次，你应当思考导致用户所发送代码错误的原因，并提出解决问题的思路；
- 最后，你应当预设你的解决方案可能不准确，因此你需要和用户进行多次交互，并且每次交互后，你应当总结上一次交互的结果，并根据这些结果调整你的解决方案，直到用户满意为止。

## 第三步
在完成用户要求的任务后，你应该对改成任务完成的步骤进行反思，思考项目可能存在的问题和改进方式，并更新在readme.md文件中
```


### example
[关于Cursor使用的小白第一视角\_cursor教程-CSDN博客](https://blog.csdn.net/a23_23/article/details/142457540)


## AI+日程管理：Dola 智能助手
[Dola - AI 日历助手](https://heydola.com/zh)

可以使用订阅连接集成到你的日历当中

- 支持语音输入
- 支持中文
- 支持推文转发总结


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241202192248.png)

## LLM 平台
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

