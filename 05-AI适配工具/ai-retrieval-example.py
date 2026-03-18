"""
AI 检索调用示例（本地最小可运行）

用途：
- 将仓库内的 Markdown FAQ 文档加载成“可嵌入”的文本块
- 按 schema 组织成统一结构（见 faq-vector-schema.json）
- 用一个最简“关键词检索”模拟向量检索的调用形态

说明：
- 你可以把 `keyword_search()` 替换为你实际的向量数据库/Embedding 检索实现。
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List


REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class FaqDoc:
    id: str
    title: str
    chip: str
    category: str
    path: str
    content: str
    tags: List[str] | None = None
    metadata: dict | None = None


def iter_md_files() -> Iterable[Path]:
    for folder in [
        REPO_ROOT / "01-芯片基础配置",
        REPO_ROOT / "02-配对与连接",
        REPO_ROOT / "03-协议与数据交互",
        REPO_ROOT / "04-问题排查",
    ]:
        if folder.exists():
            yield from folder.rglob("*.md")


def infer_category(p: Path) -> str:
    name = p.parts[-2]
    mapping = {
        "01-芯片基础配置": "芯片基础配置",
        "02-配对与连接": "配对与连接",
        "03-协议与数据交互": "协议与数据交互",
        "04-问题排查": "问题排查",
        "05-AI适配工具": "AI适配工具",
    }
    return mapping.get(name, "问题排查")


def infer_chip(filename: str) -> str:
    f = filename.lower()
    if f.startswith("ts8001-"):
        return "TS8001"
    if f.startswith("ts8010-"):
        return "TS8010"
    return "TS8001/TS8010"


def infer_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback


def load_docs() -> List[FaqDoc]:
    docs: List[FaqDoc] = []
    for p in iter_md_files():
        content = p.read_text(encoding="utf-8")
        doc_id = p.stem
        title = infer_title(content, fallback=doc_id)
        docs.append(
            FaqDoc(
                id=doc_id,
                title=title,
                chip=infer_chip(p.name),
                category=infer_category(p),
                path=str(p.relative_to(REPO_ROOT)).replace(os.sep, "/"),
                content=content,
                tags=None,
                metadata=None,
            )
        )
    return docs


def keyword_search(docs: List[FaqDoc], query: str, top_k: int = 5) -> List[FaqDoc]:
    q = query.strip().lower()
    scored = []
    for d in docs:
        text = (d.title + "\n" + d.content).lower()
        score = text.count(q) if q else 0
        if score > 0:
            scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:top_k]]


def main() -> None:
    docs = load_docs()
    print(f"Loaded {len(docs)} markdown docs from repo.")

    query = input("Query: ").strip()
    hits = keyword_search(docs, query=query, top_k=5)
    print(f"Hits: {len(hits)}")

    payload = [asdict(d) for d in hits]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

