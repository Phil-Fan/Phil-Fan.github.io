# Server

!!! note "备忘记录一些实验室服务器和云服务器的操作，以linux为主"




## 登录

```shell
ssh name@ip
```

```shell title="带端口登录"
ssh -p <port> name@ip
```

```shell title="退出登录"
exit
```

### 免密登录
```shell title="进入.ssh目录"
cd .ssh
```

```shell title="生成密钥对"
ssh-keygen -t rsa
```
会在`.ssh`目录下生成`id_rsa.pub`和 `id_rsa`两个文件

```shell title="把生成的公钥上传到服务器"
ssh-copy-id -p 10086 name@ip
```
会在服务器端的`.ssh`目录下有`authorized_keys`文件，和`id_rsa.pub`的内容是一样的


```shell title="免密设置好以后可以直接登录"
ssh <alias>
```

!!! note "免密登录的操作是针对用户的，切换其他用户就不可以了"
    可以结合公私钥文件进行理解
### 其他连接方法
- Xshell
- PuTTY

## 任务运行

### 使用 `nohup` 后台运行任务

`nohup` 命令用于以忽略挂起信号的方式运行另一个命令。这在后台运行进程时特别有用，即使终端会话关闭，进程仍然会继续运行。


1. **使用 `nohup` 运行命令：**

   要使用 `nohup` 在后台运行命令，可以使用以下语法：

   ```bash
   nohup command &
   ```

   - `command`: 您要运行的命令。
   - `&`: 这个符号用于在后台运行命令。

2. **输出重定向：**

   默认情况下，`nohup` 将输出重定向到当前目录中的一个名为 `nohup.out` 的文件。如果您想为输出指定一个不同的文件，可以使用：

   ```bash
   nohup command > output.log 2>&1 &
   ```

   - `> output.log`: 将标准输出重定向到 `output.log`。
   - `2>&1`: 将标准错误重定向到与标准输出相同的文件。

3. **检查正在运行的进程：**

   要检查正在运行的后台进程列表，可以使用：

   ```bash
   jobs
   ```

4. **将后台进程带到前台：**

   如果需要将后台进程带到前台，请使用：

   ```bash
   fg %job_number
   ```

   - `%job_number`: 进程的作业号，可以使用 `jobs` 命令找到。

5. **终止后台进程：**

   要终止后台进程，可以使用带有进程 ID (PID) 的 `kill` 命令：

   ```bash
   kill -9 PID
   ```

   - `PID`: 您要终止的任务的进程 ID。

### 使用 `Screen` 持续运行任务

1. 安装 Screen
   ```bash
   sudo apt-get install screen
   ```

2. 创建 Screen 窗口
   ```bash
   screen -S <name>
   ```
   - `<name>` 可以设置为 `ssh`、`ftp` 等，用于标识该 Screen 窗口的用途。

3. 启动项目
   - 执行 `screen -S <name>` 后，系统会跳入新窗口，在此窗口中启动项目。

4. 退出并保存
   - 完全退出：`exit`（不会保存 session）。
   - 分离窗口：按 `CTRL-a` 然后按 `d`，可以退出 SSH 登录而不影响 Screen 程序的执行。

5. 常用命令
   - 查看 Screen 进程：
     ```bash
     screen -ls
     ```
   - 进入 Screen 进程：
     - 如果只有一个 Screen 进程：
       ```bash
       screen -r -d
       ```
     - 如果有多个 Screen 进程，通过 PID 进入：
       ```bash
       screen -r -d <PID>
       ```
       示例：
       ```bash
       screen -r -d 1805
       ```


## 远程连接

### pycharm 远程开发

[Pycharm远程连接服务器并运行代码（详细！）\_pycharm将代码同步到远程服务器-CSDN博客](https://blog.csdn.net/cutefery/article/details/113918510)

**1. 设置Connection**

Tools->Deployment->Configuration

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/fac49e9753f2ab5a3c262724b13ace42.png)



**2. 建立Mapping**

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/5ada3773c2ea98000fdf257681baa67f.png)

**3. 实现代码自动上传**

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/642e7fe6b4c620483aed45e51615ca92.png)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/eba75696543b972e5fc6289fe9648940.png)

**4. 设置Python Interpreter**

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1e5ffb013eb5acda4148f924aafe9f3b.png)

### vscode

使用vscode连接以后，可以将文件直接拖拽传递

### 报错



[我只教一次！vscode remote-ssh 连接失败的基本原理和优雅的解决方案 - 知乎](https://zhuanlan.zhihu.com/p/671718415)

[【VScode远程连接报错】Failed to parse remote port from server output\_vscode failed to parse remote port from server out-CSDN博客](https://blog.csdn.net/qq_38667212/article/details/140462083)

[VSCode 连不上远程服务器问题及解决办法集合\_vscode 无法连接远程服务器-CSDN博客](https://blog.csdn.net/White_lies/article/details/124093530)


[blog.csdn.net/why1249777255/article/details/134296929](https://blog.csdn.net/why1249777255/article/details/134296929)


[blog.csdn.net/why1249777255/article/details/134296929](https://blog.csdn.net/why1249777255/article/details/134296929)
1. 到本地删除.ssh下known_hosts

```shell
C:\Users\username\.ssh\
```
补充：如果known hosts文件中有其他信息，不要直接删除文件，直接删掉服务器信息即可

2. 首先 kill 掉服务器端的VS code 服务，然后在服务器端删除vscode连接的相关记录

```
/home/username/.vscode-server/
```

3. 重新回到Vscode连接

还可以尝试把.ssh\ss


### 其他工具

- scp(linux to linux)
- wget



## 运维工具
### 宝塔面板



### 1Panel
[1Panel 文档](https://1panel.cn/docs/installation/online_installation/)

```shell title="安装1Panel,ubuntu"
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh
```

配置镜像加速选择`y`

使用`1pcl`命令行工具进行管理，[命令行工具 - 1Panel 文档](https://1panel.cn/docs/installation/cli/)

!!! note "如果使用的是云服务器，需要配置安全组规则"
    在安全组当中，选择添加规则

    - 目的：`20410/20410`
    - 源：`0.0.0.0/0`

    然后点保存即可，不需要重启云服务器，保存后自动生效。

## 显卡相关
### 环境配置

```shell
conda create -n <>_py<version> python=<version>

conda activate <name>
```

```shell title="pytorch安装"
pip install torch torchaudio torchvision
```

```shell title="安装一些常用库"
pip install scipy seaborn tqdm jupyter pandas matplotlib opencv-python
```


```shell title="其他库"
pip install d2l
```


```python title="测试环境配置代码"
import torch
print("PyTorch Version:", torch.__version__)

if torch.cuda.is_available(): # 检查 CUDA 是否可用
    print("CUDA is available.")
    num_gpus = torch.cuda.device_count() # 获取显卡总数
    print(f"Number of GPUs: {num_gpus}")
    if num_gpus >= 1:
        device = torch.device(f"cuda:{num_gpus - 1}") # 指定使用最后一块显卡
        print(f"Using GPU: {torch.cuda.get_device_name(device)}")
        tensor = torch.rand(3, 3).to(device) # 在指定显卡上创建一个简单的张量计算
        print("Tensor on GPU:\n", tensor)
    else:
        print("No GPUs available.")
else:
    print("CUDA is not available.")
```

```shell title="示例输出"
PyTorch Version: 2.4.1+cu121
CUDA is available.
Number of GPUs: 6
Using GPU: NVIDIA GeForce RTX 3090
Tensor on GPU:
 tensor([[0.9610, 0.1389, 0.1536],
        [0.7481, 0.7573, 0.2097],
        [0.2123, 0.6865, 0.0611]], device='cuda:5')
```


### 查看GPU
```shell title=""
gpustat
```

```shell title="查看空闲状态"
nvidia-msi
```

```shell title="自动实时刷新GPU的使用情况"
nvidia-smi -l
```

??? note "各参数含义"
    - `GPU`：显卡编号，从0开始。
    - `Fan`：风扇转速，在0~100%之间变动。这个速度是计算机期望的风扇转速，实际情况下如果风扇堵转，可能就不会显示具体转速值。有的设备不会返回转速，因为它不依赖风扇冷却，而是通过其他外设保持低温，比如我们实验室的服务器是常年放在空掉房间里面的。
    - `Name`：显卡名，以上都是Tesla。
    - `Temp`：显卡内部的温度，以上分别是54、49、46、50、39摄氏度。
    - `Perf`：性能状态，从P0到P12，P0性能最大，P12最小 。
    - `Persistence-M`：持续模式的状态开关，持续模式虽然耗能大，但是在新的GPU应用启动时，花费的时间更少。以上都是Off的状态。
    - `Pwr`：能耗表示。
    - `Bus-Id`：涉及GPU总线的相关信息。
    - `Disp.A`：是Display Active的意思，表示GPU的显示是否初始化。
    - `Memory-Usage`：显存的使用率。
    - `GPU-Util`：GPU的利用率。
    - `Compute M.`：计算模式。

为什么`Volatile GPU-Util`列显示第二个卡占用为0，明明这个卡的内存已经用了。这个深度学习调用有关，实际上这时GPU正在等待CPU的处理，而CPU的处理结果有时候很慢，所以GPU在等。可以将`num_workers=4`或8或16（再多不推荐可能变慢，因为通信需要成本），分配多个子线程，且设置`pin_memory=True`，直接映射数据到GPU的专用内存，减少数据传输时间，提高GPU利用率。

### 查看内存
```shell title="查看内存"
free -m 
```


```shell title="windows查看内存占用情况"
tasklist
```
### 查看CPU
```shell title="查看CPU使用情况"
top
```
在命令行输入`top`就可以实现对服务器进程的监控，此时可以看到多个用户的进程，以及PID，如果遇到有进程卡在了里面可以采用kill + PID的方式结束进程。如下图所示：


```shell title="另外的指令"
htop
```
htop能够更直观的显示活跃进程，单个进程或多个线程的具体内存1和CPU的占用情况，并且会报告当前所有服务器用户的内存使用状况，并且有更多的F-系列的直接命令可供使用。






### 查看用户
```shell
ps -f -p PID号
```
### 指定GPU

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
```
```python title="设置定量的GPU使用量"
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 占用GPU90%的显存
session = tf.Session(config=config)
```



```python title="设置最小的GPU使用量"
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
```
### 显卡简介

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121100854.png)

显卡由 **显卡核心（GPU） 、电路板（PCB）、显存、金手指、供电 & 显示接口以及散热**等构成。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121100941.png)

显卡核心里主要由运算单元 cuda core，控制单元，缓存单元等构成。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121101011.png)
显存，类似于系统的内存，但它是显卡专用的内存。显存主要用来缓存 GPU 处理过的或者即将提取的渲染数据。显存主要包括容量、频率和位宽这三个参数。容量就是显存的大小，一般来说，显存越大能存储的数据越多，对于部分场景很有用


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121101048.png)


输出部分就是显卡挡板处的接口，有：VGA、DVI、HDMI、DP、USB-C（包括雷电 3）

显卡和显示器之间的接口，共有VGA、HDMI、DVI、DP以及USB-C（包括雷电3）等。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121101127.png)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121101207.png)

开放式风扇是直接吹显卡（鳍片）来提供散热，使用场景比较广泛，有无风道都能用，而且相较而言更静音。涡轮风扇散热则是靠吸入风量横吹核心（鳍片），与开放式相比，对整机内部其它硬件影响不大，比较适合有平行风道，而且工作温度不高的显卡。但估计以后公版也会多采用开放式而放弃涡轮。
### 显卡分类

显卡根据不同的位置，有**集显、核显和独显**的区别
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241121101331.png)

- **集显** 集成在主板北桥芯片的显示芯片，有些共享系统内存，有些自带内存。 现在少见了，常有人把核心显卡当作集成显卡，再过些年这么叫也可能是对的了。
- **核显**  集成在核心（CPU内）中的显卡，共享系统内存资源。
- **独显** 将显示芯片及相关器件制作成一个独立于电脑主板的板卡，成为专业的图像处理硬件设备。


英伟达 Geforce 共有 GT、 GTX、RTX 和 TITAN 四个系列，

（这时可能会有没看前面的脑子瓦特的就会跳出来说明明还有 quadro 系列）

GT 代表 GeForce Technology ，比较适合家用入门级，影音和小游戏都能满足。

GTX 代表更高级的游戏独显，后来随着技术进步，出现了光线追踪 （Ray Tracing），于是命名也增加了一个 RTX，因为是最先进的技术，再低端也是很昂贵，所以 RTX 都是从 -60 结尾往上走，价格也比以往 GTX 的更贵。而 TITAN 就是英伟达 GeForce 的看家显卡，霸主的存在。


> [【显卡科普】小白必看的入门显卡科普，关于显卡的原理、结构、作用 - 知乎](https://zhuanlan.zhihu.com/p/156083352)



## 进程管理

### 查看进程
- **查看所有进程：**
  ```bash
  ps -aux
  ```
  列出所有正在运行的进程。


- **查看特定用户的进程：**
  ```bash
  ps -u username
  ```
  列出特定用户的所有进程。

### 终止进程

- **通过 PID 终止进程：**
  ```bash
  kill -9 PID
  ```
  强制终止指定 PID 的进程。

```shell title="windows杀死无效进程"
taskkill /PID 进程号 -F -T  
```
但是感觉任务管理器更方便一点... :laughing:



- **通过进程名终止进程：**
  ```bash
  pkill process_name
  ```
  终止所有匹配指定进程名的进程。
## Aliyun
### 无影云电脑


### ECS


#### 上传文件

使用workbench，在文件一栏中选择"打开新文件树"

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241118233039.png)



### OSS

图床

### 开发票

个人用户抬头只能是个人

## AutoDL

```shell title="创建虚拟环境"
conda create -n tf python=3.7           # 构建一个虚拟环境，名为：tf
conda init bash && source /root/.bashrc # 更新bashrc中的环境变量
conda activate tf                       # 切换到创建的虚拟环境：tf
```
### 无法加载Hugging Face

=== "实测成功的方法"

    ```python title="在代码头部加入"
    import os
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    ```

    ```shell title="在终端中执行"
    pip install -U huggingface_hub
    export HF_ENDPOINT=https://hf-mirror.com
    source ~/.bashrc
    ```
    
    (优点是不需要改代码，非常简单易操作。缺点就是镜像网站下载较慢)

=== "另外的方法"

    ```python title="在代码头部加入"
    import subprocess
    import os
    
    result = subprocess.run('bash -c "source /etc/network_turbo && env | grep proxy"', shell=True, capture_output=True, text=True)
    output = result.stdout
    for line in output.splitlines():
        if '=' in line:
            var, value = line.split('=', 1)
            os.environ[var] = value
    ```
    如果启用学术资源加速后遇到SSL证书验证错误，可以禁用证书验证，在程序开头再添加以下代码
    ```python
    import os
    os.environ['CURL_CA_BUNDLE'] = ''
    ```
