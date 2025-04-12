# Diffusion Model


## EXP - Diffusion Policy: Diffusion applied to control

1. **安装 Anaconda**

   网上有很多教程，这里不再赘述。最好在租用服务器时直接选择 Anaconda 环境，这样会方便很多。

2. **在 Anaconda 下安装 Mamba（Mamba 运行效率显著提升）**

   ```bash title="安装 Mamba"
   conda install mamba -n base -c conda-forge
   ```

3. **按照代码中的 README 文件一步一步配置**

   - **安装依赖**

     ```bash title="安装依赖"
     sudo apt install -y libosmesa6-dev libgl1-mesa-glx libglfw3 patchelf
     ```

   - **创建环境，环境名称为 robodiff**（这一步用时较长，需要耐心等待）

     ```bash title="创建 robodiff 环境"
     mamba env create -f conda_environment.yaml
     ```

   - **在主文件夹下，创建 data 文件夹**

     ```bash title="创建 data 文件夹"
     mkdir data && cd data
     ```

   - **在 data 文件夹里下载数据集**

     ```bash title="下载数据集"
     wget https://diffusion-policy.cs.columbia.edu/data/training/pusht.zip
     ```

   - **解压数据集并删除压缩包**

     ```bash title="解压数据集"
     unzip pusht.zip && rm -f pusht.zip
     ```

   - **下载实验相关参数的文件**

     ```bash title="下载实验参数文件"
     wget -O image_pusht_diffusion_policy_cnn.yaml https://diffusion-policy.cs.columbia.edu/data/experiments/image/pusht/diffusion_policy_cnn/config.yaml
     ```

4. **跑一个实例**

   - **进入环境**

     ```bash title="激活环境"
     conda activate robodiff
     ```

   - **下载 wandb**

     ```bash title="安装 wandb"
     pip install wandb
     ```

   - **在 wandb 中创建一个账号，并将 API_Key 复制下来，在命令行中输入指令登录 wandb**

     ```bash title="登录 wandb"
     wandb login
     ```

     回车后，将 API_Key 复制到指定位置，回车，登录。之后的训练数据就会显示在 wandb 中了。wandb 网址如下：Weights & Biases。在 wandb 中，home 中可以找到 API Key。

   - **训练**

     ```bash title="训练指令"
     python train.py --config-dir=. --config-name=image_pusht_diffusion_policy_cnn.yaml training.seed=42 training.device=cuda:0 hydra.run.dir='data/outputs/${now:%Y.%m.%d}/${now:%H.%M.%S}_${name}_${task_name}'
     ```

以上就是关于 diffusion policy 的代码复现全部过程，详细文章及代码请看：[https://diffusion-policy.cs.columbia.edu](https://diffusion-policy.cs.columbia.edu)
