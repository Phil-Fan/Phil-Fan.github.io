# JavaScript
## 历史
JavaScript（简称JS）是由Netscape公司的Brendan Eich在1995年十天内开发出来的一种脚本语言。最初设计用于浏览器端的动态网页内容生成，JavaScript迅速成为Web开发的核心技术之一，与HTML和CSS并列为前端开发的三大支柱。

- **诞生背景**：JavaScript诞生于Web 1.0时代，最初被称为Mocha，后改名为LiveScript，最后才成为JavaScript。
- **发展历程**：从最初的客户端脚本语言，JavaScript逐步演变成一门强大的编程语言，现今不仅用于浏览器端，还在服务器端广泛应用。

- 是编程语言，Web 的核心技术之一
- JavaScript 是遵循 ECMAScript 标准的脚本语言,与 Java 没有任何关系
- 现在也可用于通用编程：Node.js

## 语法
用于实现网页的交互功能，由 <script> 标签引入
```javascript
//变量
var x = 5;
let y = 10;
const z = 15;

//函数
function add(a, b) {
  return a + b;
}
```


```javascript
<script>
console.log('Hello, World!');

fetch('https://api.example.com')
    .then(response => response.json())
    .then(data => document.body.innerHTML = data.message);
</script>
<script async src="my-super-cool-script.js"></script>
```

事件监听
```javascript
document.getElementById("myButton").addEventListener("click", function() {
  alert("Button clicked!");
});
```

## Beyond
- JavaScript 的缺点：性能不足（解释型）、弱类型
- WebAssembly（WASM）：在浏览器中运行的跨平台字节码格式
  * 由 C、C++、Rust 等编译型语言编译生成
  * 可以直接在浏览器中运行，性能接近原生代码
  * 可以与 JavaScript 互操作
  * 适合于需要高性能的应用，如游戏、图像、视频处理等

### TS | TypeScript
TypeScript（简称TS）是由微软开发的一种开源编程语言，是JavaScript的超集，增加了静态类型和类等特性。

**静态类型：** 通过类型检查减少运行时错误，提高代码的可维护性。

```
let message: string = "Hello, TypeScript!";
```
​
**类和接口：** 支持面向对象编程，增强代码结构性。

```
class Person {
  name: string;
  constructor(name: string) {
    this.name = name;
  }
  greet() {
    console.log("Hello, " + this.name);
  }
}

let person = new Person("Alice");
person.greet();

import { add } from './math';
console.log(add(2, 3));
```
​
**模块化：** 支持模块化编程，提高代码复用性和组织性。
```
import { add } from './math';
console.log(add(2, 3));
```