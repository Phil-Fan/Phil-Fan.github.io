## Background and Problem Statement

In this paper, I have learned the workflow for addressing an AML (Adversarial Machine Learning) problem. Throughout the process of studying the paper, I also supplemented my foundational knowledge regarding academic papers.

### Black Box Attacks

**White-box attack:**
- Attackers possess complete knowledge of the machine learning (ML) model.

**Black-box attack:**
- Attackers lack access to the ML model's parameters, gradients, and architecture.
- They may know the ML algorithm used.

**Zero-Query:** No access to query samples or query results.

For black-box models, two aspects need consideration:

1. **Surrogate Model:** When attacking a black-box model provided by a platform, a viable approach is to train a local model with a similar decision boundary to the target model. White-box attacks are then conducted on the local model to generate adversarial samples, which are used to attack the target model leveraging transferability. This locally deployed model is known as the surrogate model.

2. **Transferability:** The assumption that adversarial samples are transferable implies that if an adversarial sample successfully attacks one model, it is likely to succeed against another similar model.

### Automatic Speech Recognition (ASR) Systems

ASR systems focus on whether speech is heard clearly rather than understood. Current intelligent speech recognition systems primarily utilize deep learning models based on Transformer or convolutional neural networks (CNNs).

### End-to-End Models

End-to-end models directly process raw data to produce output, whereas non-end-to-end models require preprocessed data as input.

## Existing Challenges

The target model is a black box, with no access to its structure, parameters, or training data. When using the target model for image classification, typically only a single label is provided without accuracy information. Additionally, API query limits impose cost constraints and potential detection by platform anomaly programs.

Speech systems must handle temporal information changes, which is more complex than image classification. Audio sampling rates are usually high (e.g., 16kHz, implying 16,000 samples per second), whereas images have only hundreds or thousands of pixels (e.g., 28×28 for MNIST and 32×32 for CIFAR-10). Consequently, creating adversarial audio is more challenging than images because adding small noise to audio is less likely to affect local features. The resulting changes should be minimally perceptible to users.

Previous works on black-box adversarial attacks against ASR systems do not require internal knowledge of the target ASR system but assume the attacker can interact with it. In contrast, this paper considers a more realistic and challenging scenario where the attacker cannot query the target ASR system during adversarial example generation.
## Solution Approach

### Multiple Surrogate Models

. In the paper, author investigate modern ASR systems and categorize them into two main types: CNN-based and Transformer-based. While CNNs are better at capturing local features, Transformers excel at capturing global contexts. An intuitive approach involves using both CNNs and Transformers.

### Initialization

Initially, Text-to-Speech (TTS) methods generate perturbation \( x_t \), followed by scaling applied to \( x \) and \( x_t \). An adaptive search algorithm finds the smallest scaling factor \( \mu \), and \( \delta \) is initialized using the scaled target command audio \( \mu \cdot x_t \), ensuring the initial adversarial example is recognized by all surrogate ASRs as the target command.

### Ensemble Optimization

After perturbation initialization, ZQ-Attack employs a sequential ensemble optimization algorithm to collaboratively optimize adversarial perturbations across an ordered set of surrogate ASRs. This algorithm includes an inner and outer loop. In each iteration, the ordered set of surrogate ASRs is randomly shuffled in the outer loop.

Considering the influence between each surrogate ASR, the update formula is:

\[
\delta = \eta \cdot \frac{1}{K} \sum_{j=1}^{K} \delta_j + (1 - \eta) \cdot \delta_0,
\]

where \( \eta \) adjusts the impact of \( \delta_0 \) in each round.

The sequential ensemble optimization occurs within the inner loop, integrating collaborative information from all preceding surrogate ASRs in the ordered set to facilitate collaborative optimization.

The clipping function ensures adaptive perturbation limits based on audio volume, reducing perceptible interference:

\[
\text{clip}_\epsilon(\delta, x) = \max(\min(\delta, \epsilon \cdot |x|), -\epsilon \cdot |x|).
\]

The gradient update formula incorporates Gaussian perturbations:

\[
\delta_j = \delta_0 - \alpha \cdot \frac{1}{j} \sum_{\delta' \in \Delta_j} \nabla_{\delta'} \mathcal{L}(x, \delta' + \sigma, t, f_j).
\]

### Loss Function

The loss function considers three factors: adversarial attack effectiveness, imperceptibility (measured by a novel metric), and feature extraction (using \( L_2 \) norm).

## Experimental Validation

### Experimental Design

Extensive experiments were conducted under two settings: online speech recognition services, commercial IVC devices, and open-source ASR systems. ZQ-Attack generated audio adversarial examples to attack various ASR systems in each setting.

### Results

- **Online Speech Recognition Services:** ZQ-Attack achieved a 100% success rate across 4 different services with an average Signal-to-Noise Ratio (SNR) of 21.91dB.
- **Commercial IVC Devices:** ZQ-Attack achieved a 100% success rate across 2 different devices with an average SNR of 15.77dB.
- **Open-Source ASR Systems:** ZQ-Attack achieved a 100% success rate across 16 different ASR systems with an average SNR of 19.67dB.

These results demonstrate that ZQ-Attack can generate audio adversarial examples with high transferability and success rates against various ASR systems.

### Limitations

- **Computational Cost:** ZQ-Attack requires optimizing adversarial perturbations across multiple surrogate models, potentially leading to high computational costs.
- **Imperceptibility:** While ZQ-Attack exhibits good imperceptibility in over-the-line settings, it may still be detectable by humans in over-the-air settings.

## Insights Gained

Through this process, I have adopted fundamental methods for reading academic papers, including using tools like Zotero and gathering information from platforms such as Google Scholar and Arxiv. I've also realized that most cutting-edge research and information are in English, as few theses are available in Chinese, and there is limited sharing of up-to-date information on Chinese internet platforms. This opportunity to learn and engage with English academic papers has been invaluable.

This paper demonstrates generating highly transferable audio adversarial examples to attack various ASR systems in a zero-query black-box setting, providing new insights for other types of black-box attacks. The proposed sequential ensemble optimization algorithm can be applied to other ensemble models to enhance their performance and robustness.