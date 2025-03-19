# exp



[Hugging Face Forums - Hugging Face Community Discussion](https://discuss.huggingface.co/)


[OSError: We couldn‘t connect to ‘https://huggingface.co‘ to load this file, couldn‘t find it(亲测有效)\_checkout your internet connection or see how to ru-CSDN博客](https://blog.csdn.net/l8947943/article/details/143099409)


1. 科学上网，访问该网址
通过全局代理的方式，实现模型的下载。

2. 使用镜像网址
国内huggingface镜像地址：https://hf-mirror.com/
往下翻，直接可看到使用教程。主要有四种解决方式。最直接的方式就是一个个下载使用。

3. 在代码中增加设置
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
