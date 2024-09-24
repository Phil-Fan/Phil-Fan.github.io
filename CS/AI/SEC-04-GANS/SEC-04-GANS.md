# GANS
Generative adversarial networks
[理解生成对抗网络(GANs) - 知乎](https://zhuanlan.zhihu.com/p/97015788)

[一文看尽深度学习中的生成对抗（GAN）网络\_energy-basedgan-CSDN博客](https://blog.csdn.net/qq_23981335/article/details/118332773)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240924092601.png)

[图解 生成对抗网络GAN 原理 超详解\_gan原理图-CSDN博客](https://blog.csdn.net/DFCED/article/details/105175097)


## origin GANs


## Variants

### Wasserstein GANs
Critics: the discriminator is called a critic,it tells how real the data is
### Conditional GANs | cGANs


### cycle GANs

replace the main object but keep the main features
### StyleGANs

seperate different style of the images

## Challenges
- Vanishing gradients: the generator gradients vanish, making it impossible to train the generator
- Mode collapse: the generator collapses to a single point in the data space(一张图片效果好就一直生成)
- Convergence

## GANs base