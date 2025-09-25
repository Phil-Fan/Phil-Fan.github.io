#

## 下载


## 文档

[File Browser](https://filebrowser.org/index.html)

github[filebrowser/filebrowser: 📂 Web File Browser](https://github.com/filebrowser/filebrowser)
[filebrowser-docs/cli at master · maxant/filebrowser-docs](https://github.com/maxant/filebrowser-docs/tree/master/cli)



## 配置
[Filebrowser 部署 | gobai's notes](https://blog.gocn.top/posts/filebrowser/)
```json
{
  "port": 8080,
  "baseURL": "",
  "address": "0.0.0.0",

  "log": "/var/lib/filebrowser/filebrowser/filebrowser.log",
  "database": "/var/lib/filebrowser/filebrowser/filebrowser.db",
  
  "root": "/var/lib/filebrowser/EE_files",
  "allowCommands": true,
  "commands": [
    "ls",
    "df"
  ],
  "enableNewUser": false,
  "shell": "/bin/zsh",
  "locale": "zh-cn"
}
```


### 配置服务

```
[Unit]
Description=File Browser Service
After=network.target

[Service]
# 使用 filebrowser 用户运行
User=filebrowser
Group=filebrowser

# File Browser 可执行文件和配置文件
ExecStart=/path/to/filebrowser -c /etc/filebrowser/.filebrowser.json

# 自动重启策略
Restart=on-failure

# 工作目录（你的文件根目录）
WorkingDirectory=/path/to/dict/

# 输出日志到 systemd journal
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

```shell
sudo systemctl daemon-reload
sudo systemctl enable filebrowser
sudo systemctl restart filebrowser
sudo systemctl status filebrowser
```

## 访问

可以使用url进行访问，但需要配置服务

## Custom

[免费Favicon图标生成器 - 在线制作ICO、PNG、SVG网站图标 | Favicon.im](https://favicon.im/zh/generator)