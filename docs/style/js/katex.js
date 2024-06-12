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