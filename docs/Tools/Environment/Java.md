# Java

## 简介

## 安装

在下面的网址进行下载

https://www.oracle.com/java/technologies/downloads/


```shell title="解压"
sudo tar -xvzf yourfile.tar.gz -C /usr/lib/jvm/
```

```shell title="更改环境变量"
export JAVA_HOME=/usr/lib/jvm/jdk-21.0.8
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

```shell title="验证安装"
$ java --version


java 21.0.8 2025-07-15 LTS
Java(TM) SE Runtime Environment (build 21.0.8+12-LTS-250)
Java HotSpot(TM) 64-Bit Server VM (build 21.0.8+12-LTS-250, mixed mode, sharing)
```





## 使用
### `.jar`文件打开方式

1.双击打开

2. 命令行打开x

```shell
java -jar xxx.jar
```

```shell title="后台执行"
java -jar xxx.jar &
```

```shell title="不挂断执行"
nohup java -jar test_jar-1.0-SNAPSHOT.jar &   
```  

nohup 意思是不挂断运行命令，当账户退出或终端关闭时，程序仍然运行。

当用 nohup 命令运行jar包时，缺省情况下该应用的所有输出被重定向到nohup.out的文件中，除非另外指定了输出文件。