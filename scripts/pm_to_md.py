#!/usr/bin/env python3
"""Print a Heptabase note card as plain markdown.

`heptabase note read <cardId>` returns ProseMirror JSON; this turns it into readable text so you can
reuse his drafts or diff his edits against what you wrote.

  heptabase note read <cardId> | python3 pm_to_md.py
  python3 pm_to_md.py <cardId>            # runs `heptabase note read` for you
"""
from __future__ import annotations

import json
import subprocess
import sys

LISTS = {"bullet_list", "bulletList", "ordered_list", "orderedList"}
ITEMS = {"list_item", "listItem", "bullet_list_item", "numbered_list_item", "todo_list_item"}


def inline(node: dict) -> str:
    if node.get("type") == "text":
        text = node.get("text", "")
        for mark in node.get("marks") or []:
            kind = mark.get("type")
            if kind in ("strong", "bold") and text.strip():
                text = f"**{text}**"
            elif kind in ("em", "italic") and text.strip():
                text = f"*{text}*"
            elif kind == "code":
                text = f"`{text}`"
            elif kind == "link" and mark.get("attrs", {}).get("href"):
                text = f"[{text}]({mark['attrs']['href']})"
        return text
    if node.get("type") in ("hard_break", "hardBreak"):
        return "\n"
    return "".join(inline(c) for c in node.get("content") or [])


def block(node: dict, indent: str = "") -> str:
    t = node.get("type")
    kids = node.get("content") or []
    if t == "heading":
        return "#" * node.get("attrs", {}).get("level", 2) + " " + inline(node) + "\n\n"
    if t == "paragraph":
        return indent + inline(node) + "\n\n"
    if t in LISTS or t in ITEMS:
        items = kids if t in LISTS else [node]
        out = ""
        for item in items:
            parts = item.get("content") or []
            first = inline(parts[0]) if parts else ""
            out += f"{indent}- {first}\n"
            for rest in parts[1:]:
                out += block(rest, indent + "  ").rstrip("\n") + "\n"
        return out + ("\n" if not indent else "")
    if t == "blockquote":
        return "".join("> " + line + "\n" for line in "".join(block(c) for c in kids).strip().split("\n")) + "\n"
    if t == "horizontal_rule":
        return "---\n\n"
    return "".join(block(c, indent) for c in kids)


def main() -> None:
    if len(sys.argv) > 1:
        raw = subprocess.run(["heptabase", "note", "read", sys.argv[1]], capture_output=True, text=True).stdout
    else:
        raw = sys.stdin.read()
    data = json.loads(raw)
    doc = data.get("content")
    doc = json.loads(doc) if isinstance(doc, str) else (doc or {})
    print(block(doc).rstrip() + "\n")


if __name__ == "__main__":
    main()
