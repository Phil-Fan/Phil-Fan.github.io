# https://github.com/TonyCrane/note/tree/master/hooks
import os
import re
import logging

import yaml
from jinja2 import Template

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files

from utils.toc import get_statistics, get_update_time

enabled = True
# os.getenv("TOC", "1") == "1" or os.getenv("FULL", "0") == "true"
logger = logging.getLogger("mkdocs.hooks.toc")

if enabled:
    logger.info("hook - toc is loaded and enabled")
else:
    logger.info("hook - toc is disabled")

HOOKS_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_DIR = os.path.join(HOOKS_DIR, "templates/toc.html")
IGNORE_DIR = os.path.join(HOOKS_DIR, "..", ".ignored-commits")

with open(TEMPLATE_DIR, "r", encoding="utf-8") as file:
    TEMPLATE = file.read()

IGNORE_COMMITS = [
    {},
]

# with open(IGNORE_DIR, "r", encoding="utf-8") as file:
#     IGNORE_COMMITS = [
#         line.strip() for line in file if line.strip() and not line.startswith("#")
#     ]

def on_page_markdown(
    markdown: str, page: Page, config: MkDocsConfig, files: Files, **kwargs
) -> str:
    if not enabled:
        return markdown
    if "{{ BEGIN_TOC }}" not in markdown or "{{ END_TOC }}" not in markdown:
        return markdown
    toc_yml = markdown.split("{{ BEGIN_TOC }}")[1].split("{{ END_TOC }}")[0]
    toc = yaml.load(toc_yml, Loader=yaml.FullLoader)
    toc_items = _get_toc_items(
        toc, os.path.dirname(page.file.abs_src_path), config.use_directory_urls
    )
    toc_html = Template(TEMPLATE).render(items=toc_items)
    markdown = re.sub(
        r"\{\{ BEGIN_TOC \}\}.*\{\{ END_TOC \}\}",
        toc_html,
        markdown,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return markdown


def _to_href(path: str, use_directory_urls: bool) -> str:
    # Keep absolute URLs untouched
    if path.startswith("http://") or path.startswith("https://"):
        return path
    # Preserve in-page anchors
    if path.startswith("#"):
        return path
    # Normalize markdown paths to site URLs
    if path.endswith(".md"):
        if use_directory_urls:
            # index.md -> directory url; other .md -> trailing slash
            if path.endswith("index.md"):
                return path[: -len("index.md")]
            return path[: -len(".md")] + "/"
        else:
            return path[: -len(".md")] + ".html"
    return path


def _get_toc_items(toc: dict, base: str, use_directory_urls: bool) -> list:
    ret = []
    print(toc)
    for i, part in enumerate(toc):
        print(part)
        item = dict()
        item["n"] = i
        title = list(part.keys())[0]
        item["title"] = title
        
        if isinstance(part[title], str):
            # Handle simple key-value pair
            item["link"] = _to_href(part[title], use_directory_urls)
            ret.append(item)
        elif isinstance(part[title], list):
            # Handle nested structure
            details = []
            for d in part[title]:
                if isinstance(d, dict):
                    key = list(d.keys())[0]
                    value = d[key]
                    detail = dict()
                    detail["title"] = key
                    detail["link"] = _to_href(value, use_directory_urls)
                    details.append(detail)
            item["contents"] = details
            ret.append(item)
            
    return ret