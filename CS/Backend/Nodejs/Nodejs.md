# NodeJS

Node.js是由Ryan Dahl在2009年开发的一个开源、跨平台的JavaScript运行时环境，基于Chrome的V8引擎构建。Node.js的出现使得JavaScript可以用于服务器端开发。

- **起源**：Node.js诞生于对高性能、非阻塞I/O模型的需求。
- **发展**：Node.js迅速发展，成为构建高性能、可扩展网络应用的首选平台。

**Node.js的基本使用方法与应用场景**

Node.js通过事件驱动、非阻塞I/O模型，使其在处理大量并发请求时具有显著优势。

## 基本使用
```javascript
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at <http://$>{hostname}:${port}/`);
});
```

创建简单服务器
```javascript
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at <http://$>{hostname}:${port}/`);
});
```