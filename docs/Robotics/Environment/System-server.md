# 服务器


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



## 显卡相关

### 查看空闲

```shell title="查看空闲状态"
nvidia-msi
```


## Aliyun
### 无影云电脑


### ECS


#### 上传文件

使用workbench，在文件一栏中选择“打开新文件树”

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241118233039.png)



### OSS

图床

### 开发票

个人用户抬头只能是个人

