# IOS开发

!!! note "记录一下学习IOS开发的尝试"

## 安装

## 注册开发者账号


## 第一个环境构建


1. 

bundle indentifier 随便写一个

如果是用的别人的项目，关掉自动


Unable to read contents of XCFileList '/Target Support Files/Pods-**/Pods-**-frameworks-Debug-output-files.xcfilelist

```
sudo gem update cocoapods --pre
pod update
```

```shell title="在xcode当中重新建立"
clean
build
```

## 如何连接手机
使用usb线连接电脑和手机

在手机“通用 - vpn与设备管理”处，信任开发者APP


## 如何发布内测


### 使用模拟器



```shell title="打开模拟器"
xcrun simctl list devices
xcrun simctl create "iPhone 15" "iPhone 15" "iOS18.5"
xcrun simctl boot 36291DE5-5BCF-4C05-A4E2-B1AE812D35C2
```
```
open -a Simulator
```