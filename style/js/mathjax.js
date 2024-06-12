// window.MathJax = {
//     tex: {
//       inlineMath: [["\\(", "\\)"]],
//       displayMath: [["\\[", "\\]"]],
//       processEscapes: true,
//       processEnvironments: true
//     },
//     options: {
//       ignoreHtmlClass: ".*|",
//       processHtmlClass: "arithmatex"
//     }
//   };
  
//   document$.subscribe(() => { 
//     MathJax.typesetPromise()
//   })
document$.subscribe(({ body }) => { 
  renderMathInElement(body, {
    delimiters: [
      { left: "$$",  right: "$$",  display: true },
      { left: "$",   right: "$",   display: true },
      { left: "\\(", right: "\\)", display: true },
      { left: "\\[", right: "\\]", display: true }
    ],
  })
})