window.EXCALIDRAW_ASSET_PATH = "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/";
import { exportToSvg } from "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/dev/index.js";

class ExcalidrawRenderer extends HTMLElement {
  constructor() {
    super();
    const body = document.body;
    this.defaultColorTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? "dark" : "light";
    this.theme = body.getAttribute("data-md-color-media")
      ? "material"
      : "mkdocs";
    this.initTheme();
  }

  initTheme() {
    if (this.theme == "material") {
      const body = document.body;
      const isLightTheme =
        body.getAttribute("data-md-color-media") ===
        "(prefers-color-scheme: light)";
      this.mode = isLightTheme ? "light" : "dark";
      this.observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.attributeName === "data-md-color-media") {
            if (body.getAttribute("data-md-color-media") === "(prefers-color-scheme: dark)" ) {
                this.mode = "dark";
            }
            else if (body.getAttribute("data-md-color-media") === "(prefers-color-scheme: light)" ) {
                this.mode = "light";
            }
            else {
                this.mode = this.defaultColorTheme;
            }
            this.connectedCallback();
          }
        });
      });
      this.observer.observe(body, { attributes: true , attributeFilter: ['data-md-color-media']});
    }
    if (this.theme == "mkdocs") {
      const doc = document.documentElement;
      const isLightTheme = doc.getAttribute("data-bs-theme") === "light";
      this.mode = isLightTheme ? "light" : "dark";
      this.observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
          if (mutation.attributeName === "data-bs-theme") {
            if (doc.getAttribute("data-bs-theme") === "dark" ) {
                this.mode = "dark";
            }
            else if (doc.getAttribute("data-bs-theme") === "light" ) {
                this.mode = "light";
            }
            this.connectedCallback();
          }
        });
      });
      this.observer.observe(document.documentElement, { attributes: true});
    }
  }

  handleTheme(data) {
    data.appState.exportWithDarkMode = this.mode == "dark";
    data.exportPadding = 20;
    data.appState.exportEmbedScene = true;
    return data;
  }

  connectedCallback() {
    const src = this.getAttribute("src");
    fetch(src)
      .then((res) => res.json())
      .then((data) => exportToSvg(this.handleTheme(data)))
      .then((res) => {
        this.innerHTML = `<div style="display:flex;flex-direction: column;align-items: center"></div>`;
        const div = this.querySelector("div");
        div.appendChild(res);
      })
      .catch((e) => {
        this.innerHTML = `<div style="display:flex;flex-direction: column;align-items: center;"><p>could not load diagram : ${e}</p></div>`;
      });
  }
}
customElements.define("excalidraw-renderer", ExcalidrawRenderer);
