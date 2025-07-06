# 重点问题讨论

## Layer Norm

- GPT3：采用了Post-Layer Normalization（后标准化）的结构，即先进行自注意力或前馈神经网络的计算，然后进行Layer Normalization。这种结构有助于稳定训练过程，提高模型性能。
- LLAMA：采用了Pre-Layer Normalization（前标准化）的结构，即先进行Layer Normalization，然后进行自注意力或前馈神经网络的计算。这种结构有助于提高模型的泛化能力和鲁棒性。
- ChatGLM：采用了Post-Layer Normalization的结构，类似于GPT3。这种结构可以提高模型的性能和稳定性。

## 激活函数

- ReLU（Rectified Linear Unit）：一种简单的激活函数，可以解决梯度消失问题，加快训练速度。
- GeLU（Gaussian Error Linear Unit）：一种改进的ReLU函数，可以提供更好的性能和泛化能力。
- Swish：一种自门控激活函数，可以提供非线性变换，并具有平滑和非单调的特性。

## FFN

