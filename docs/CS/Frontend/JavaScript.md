# JavaScript
- 是编程语言，Web 的核心技术之一
- JavaScript 是遵循 ECMAScript 标准的脚本语言,与 Java 没有任何关系
- 现在也可用于通用编程：Node.js


用于实现网页的交互功能，由 <script> 标签引入
```javascript
<script>
console.log('Hello, World!');

fetch('https://api.example.com')
    .then(response => response.json())
    .then(data => document.body.innerHTML = data.message);
</script>
<script async src="my-super-cool-script.js"></script>
```

## Beyond
- JavaScript 的缺点：性能不足（解释型）、弱类型
- WebAssembly（WASM）：在浏览器中运行的跨平台字节码格式
  * 由 C、C++、Rust 等编译型语言编译生成
  * 可以直接在浏览器中运行，性能接近原生代码
  * 可以与 JavaScript 互操作
  * 适合于需要高性能的应用，如游戏、图像、视频处理等