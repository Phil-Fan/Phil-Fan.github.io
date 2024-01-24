# Git

## 原理

missing semester



## 使用

### 命令合集

```shell
 git init
 git remote -v
 git remote add origin + ssh
 git remote rm origin 

 git pull origin master
 git add .
 git commit -m ""
 git push origin master
 
 # 本地初始化项目
 git config --global user.name "你的名字或昵称"
git config --global user.email "你的邮箱"
```


![3a2a4da685d8aaa34d486ac6](https://gitee.com/philfan/my-images/raw/master/3a2a4da685d8aaa34d486ac6.png)

![a16f42f5af389230d4b27c7c](https://gitee.com/philfan/my-images/raw/master/a16f42f5af389230d4b27c7c.png)

### 参考网址

 [四个命令了解git](https://mp.weixin.qq.com/s/VdeQpFCL3GGsfOKrIRW6Hw)

 [多人协作流程](https://blog.csdn.net/Luhuadeng/article/details/88997404)

[Git操作详解以及在VScode中的使用](https://zhuanlan.zhihu.com/p/276376558)



## 配置

### git的安装



### 创建个人令牌

[github 创建个人令牌](https://blog.csdn.net/qq_46941656/article/details/119737804)  

``` 
Setting 
-> Developer settings
-> Personal access tokens 
-> Generate new token 保存密码到自己可以看到的位置 
```



### 免密登陆

[git 保存密码](https://cloud.tencent.com/developer/article/2207770)   

``` shell
# 记住密码 
git config --global credential.helper store  
# 删除密码 
git config --global --unset credential.helper 
```



### SSH

- 连接虚拟机

[win系统使用vscode连接虚拟机](https://blog.csdn.net/qq_40300094/article/details/114639608)   

```shell
$ ifconfig #记录ip地址 
$ ssh user.name@ip 
```

- 设置ssh免密登录  

在win主机上`ssh-keygen`生成一对公私钥，将公钥发送到服务器的`~/.ssh/authorized_keys`文件下  

在win主机上的ssh配置中加入`IdentityFile`文件，即可实现免密登录  

[理解公钥和私钥](https://zhuanlan.zhihu.com/p/113522792) 

## 问题与解决

###  连接不上 `port 443 Couldn‘t connect to server`
- 方案一：关闭VPN
- 方案二：取消代理
```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

 

### 拒绝连接 `connect to host github.com port 22: Connection refused`

- 使用`github 443` 端口

给`~/.ssh/config`文件里添加如下内容，这样ssh连接GitHub的时候就会使用443端口。

```
Host github.com
  Hostname ssh.github.com
  Port 443
```

- `https`和`git`链接换着试试

```
url = https://github.com/username/repo.git
url = git@github.com:username/repo.git
```

- 换梯子节点，检查DNS污染



###  推送失败 `src refspec master does not match any`

按照下面的顺序执行

```shell
$ git commit -m "init"
$ git remote add origin xxxxxxxx.git
$ git push -u origin master
```



###  远端链接失败 `fatal: Couldn‘t find remote ref master`

````shell
# 检查本地配置
git config user.name/git config --global user.name
git config user.email/git config --gloabl user.email

# 检查仓库配置
git remote -v
git remote rm origin
git remote add origin XXXX
````



###  文件过大 `RPC failed；curl 56 Recv failure: Connection was reset`

```shell
git config --global http.postBuffer 524288000
```

如果设置之后提交还是报错的话，可能是因为某几个文件过大造成的；


这时就需要用到 git-lfs 具体用法见[官网](https://git-lfs.github.com/)

```shell
git lfs install
git lfs track "*.so"
git add .gitattributes
```





### VMware 无法复制问题的解决 

### 安装VMware Tools选项显示灰色的正确解决办法  

1.关闭虚拟机；  

2.在虚拟机设置分别设置CD/DVD、CD/DVD2和软盘为自动检测三个步骤；  

3.再重启虚拟机，灰色字即点亮。 

4.重新安装vmware-tools  

