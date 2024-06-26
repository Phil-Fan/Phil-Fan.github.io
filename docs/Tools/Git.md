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


![3a2a4da685d8aaa34d486ac6](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/3a2a4da685d8aaa34d486ac6.png)

```shell
# 创建分支、更改
git checkout -b <branch_name>
git branch -a
git branch -d <branch_name> //删除分支
```





![a16f42f5af389230d4b27c7c](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/a16f42f5af389230d4b27c7c.png)

### `git commit`规范

为了方便使用，我们避免了过于复杂的规定，格式较为简单且不限制中英文：

```
<type>(<scope>): <subject>
// 注意冒号 : 后有空格
// 如 feat(miniprogram): 增加了小程序模板消息相关功能
```

**scope选填**表示commit的作用范围，如数据层、视图层，也可以是目录名称 

**subject必填**用于对commit进行简短的描述

 **type必填**表示提交类型，值有以下几种：

- feat - 新功能 feature
- fix - 修复 bug
- docs - 文档注释
- style - 代码格式(不影响代码运行的变动)
- refactor - 重构、优化(既不增加新功能，也不是修复bug)
- perf - 性能优化
- test - 增加测试
- chore - 构建过程或辅助工具的变动
- revert - 回退
- build - 打包

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

