#!/usr/bin/env python3
"""Put script blocks on a Heptabase whiteboard as cards, left to right, inside a titled section.

  row        one card per markdown file, laid out left to right and wrapped in a section
  variation  one card placed directly under an existing card (same column), growing the section

Uses only the `heptabase` CLI (0.6+). The JSON shapes are the ones verified on 2026-09-22; see
references/heptabase-delivery.md. --dry-run prints each mutation instead of running it (reads still run).

Examples:
  python3 heptabase_blocks.py row --whiteboard <id> --section-title "Video Script (left to right)" \
      --next-to <sectionId> --next-to-type section --side above 1-intro.md 2-why.md 3-level-1.md
  python3 heptabase_blocks.py variation --whiteboard <id> --under <cardId> --section <sectionId> 3b.md
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

GAP = 80          # horizontal gap between blocks in a row
UNDER_GAP = 100   # vertical gap between a block and its variation
PAD = 40          # section padding around its cards (what create-section uses)

LAYOUT_LINE = re.compile(
    r'^\s*(?P<kind>\w+) "(?P<title>.*)" \[(?P<id>[0-9a-f-]{36})\] at \((?P<x>-?\d+), (?P<y>-?\d+)\) '
    r"size (?P<w>\d+)x(?P<h>\d+|\?)"
)


def heptabase(args: list[str], payload: dict | None = None) -> dict:
    proc = subprocess.run(
        ["heptabase", *args],
        input=json.dumps(payload) if payload is not None else None,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        sys.exit(f"heptabase {' '.join(args)} failed:\n{proc.stderr or proc.stdout}")
    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError:
        sys.exit(f"heptabase {' '.join(args)} returned non-JSON:\n{proc.stdout[:500]}")
    if isinstance(out, dict) and out.get("error"):
        sys.exit(f"heptabase {' '.join(args)} error:\n{out['error']}")
    return out


def mutate(command: str, payload: dict, dry: bool) -> dict:
    args = ["whiteboard", command, "--input", "-"]
    if dry:
        print(f"[dry-run] heptabase {' '.join(args)}\n{json.dumps(payload, indent=2)}")
        return {}
    out = heptabase(args, payload)
    if out.get("status") == "failed":
        sys.exit(f"{command} failed: {json.dumps(out)[:800]}")
    return out


def estimate_height(words: int) -> int:
    # Rendered 520px-wide note cards measured ~3.4-4.8 px per word on 2026-09-22; overestimate a little.
    return int(words * 3.6 + 300)


def read_layout(whiteboard: str, objects: list[dict]) -> dict[str, dict]:
    out = heptabase(
        ["whiteboard", "read-layout", "--input", "-"],
        {"whiteboardId": whiteboard, "focus": {"objects": objects}},
    )
    found: dict[str, dict] = {}
    for line in out.get("content", "").splitlines():
        m = LAYOUT_LINE.match(line)
        if m:
            found[m["id"]] = {
                "kind": m["kind"],
                "title": m["title"],
                "x": int(m["x"]),
                "y": int(m["y"]),
                "w": int(m["w"]),
                "h": None if m["h"] == "?" else int(m["h"]),
            }
    return found


def note_words(card_id: str) -> int:
    out = heptabase(["note", "read", card_id])
    doc = out.get("content")
    doc = json.loads(doc) if isinstance(doc, str) else (doc or {})
    words = 0

    def walk(node: dict) -> None:
        nonlocal words
        if node.get("type") == "text":
            words += len(node.get("text", "").split())
        for child in node.get("content") or []:
            walk(child)

    walk(doc)
    return words


def create_note(path: Path, dry: bool, n: int) -> tuple[str, str]:
    text = path.read_text()
    title = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), path.stem)
    if dry:
        print(f"[dry-run] heptabase note create -f {path.resolve()}   # {title}")
        return f"dry-run-card-{n}", title
    out = heptabase(["note", "create", "-f", str(path.resolve())])
    return out["id"], out.get("title", title)


def new_lint_issues(whiteboard: str, ids: set[str]) -> list[dict]:
    out = heptabase(["whiteboard", "lint", whiteboard])
    hits = []
    for issue in out.get("lintIssues", []):
        objs = list(issue.get("objects") or []) + [issue.get("object") or {}, issue.get("section") or {}]
        if any(o.get("id") in ids for o in objs):
            hits.append(issue)
    return hits


def grow_section(whiteboard: str, section_id: str, bottom_needed: int, dry: bool) -> None:
    sec = read_layout(whiteboard, [{"id": section_id, "objectType": "section"}]).get(section_id)
    if not sec:
        print(f"warning: section {section_id} not found; not resized")
        return
    height = bottom_needed + PAD - sec["y"]
    if sec["h"] is not None and height <= sec["h"]:
        return
    mutate(
        "resize-objects",
        {
            "whiteboardId": whiteboard,
            "resizes": [
                {"mode": "setSize", "id": section_id, "objectType": "section", "width": sec["w"], "height": height}
            ],
        },
        dry,
    )


def cmd_row(a: argparse.Namespace) -> None:
    files = [Path(f) for f in a.files]
    for f in files:
        if not f.is_file():
            sys.exit(f"not a file: {f}")
    words = [len(f.read_text().split()) for f in files]
    cards = [create_note(f, a.dry_run, i) for i, f in enumerate(files, 1)]
    objs = [{"id": cid, "objectType": "card"} for cid, _ in cards]

    if a.x is not None and a.y is not None:
        dest = {"type": "point", "x": a.x, "y": a.y}
    elif a.next_to:
        dest = {"type": "nextTo", "objectId": a.next_to, "objectType": a.next_to_type, "side": a.side}
    else:
        dest = {"type": "auto"}
    mutate("place-objects", {"whiteboardId": a.whiteboard, "objects": objs, "destination": dest}, a.dry_run)
    mutate(
        "arrange-objects",
        {"whiteboardId": a.whiteboard, "objects": objs, "layout": {"type": "row", "gap": a.gap}},
        a.dry_run,
    )

    tallest = max(estimate_height(w) for w in words)
    if a.dry_run:
        print(f"[dry-run] tallest block estimated at {tallest}px; the row moves up if it would hit the anchor")
    elif dest["type"] == "nextTo" and a.side == "above":
        # nextTo uses unmeasured heights, so a tall row can run into the anchor below: lift it clear.
        layout = read_layout(a.whiteboard, objs + [{"id": a.next_to, "objectType": a.next_to_type}])
        anchor = layout.get(a.next_to)
        tops = [layout[cid]["y"] for cid, _ in cards if cid in layout]
        if anchor and tops:
            overlap = min(tops) + tallest + PAD + a.gap - anchor["y"]
            if overlap > 0:
                mutate(
                    "move-objects",
                    {
                        "whiteboardId": a.whiteboard,
                        "moves": [
                            {
                                "selection": {"type": "objects", "objects": objs},
                                "destination": {"type": "delta", "dx": 0, "dy": -overlap},
                            }
                        ],
                    },
                    False,
                )

    section_id = None
    if a.section_title:
        res = mutate(
            "create-section",
            {"whiteboardId": a.whiteboard, "objects": objs, "title": a.section_title},
            a.dry_run,
        )
        section_id = res.get("sectionId")
    if section_id:
        layout = read_layout(a.whiteboard, objs)
        bottoms = [
            layout[cid]["y"] + (layout[cid]["h"] or estimate_height(w))
            for (cid, _), w in zip(cards, words)
            if cid in layout
        ]
        if bottoms:
            grow_section(a.whiteboard, section_id, max(bottoms), a.dry_run)

    summary = {"cards": [{"id": cid, "title": t} for cid, t in cards], "sectionId": section_id}
    if not a.dry_run:
        summary["lintIssuesOnNewObjects"] = new_lint_issues(
            a.whiteboard, {cid for cid, _ in cards} | ({section_id} if section_id else set())
        )
    print(json.dumps(summary, indent=2))


def cmd_variation(a: argparse.Namespace) -> None:
    f = Path(a.file)
    if not f.is_file():
        sys.exit(f"not a file: {f}")
    under = read_layout(a.whiteboard, [{"id": a.under, "objectType": "card"}]).get(a.under)
    if not under:
        sys.exit(f"card {a.under} is not on whiteboard {a.whiteboard}")
    under_h = under["h"] or estimate_height(note_words(a.under))
    x, y = under["x"], under["y"] + under_h + UNDER_GAP

    cid, title = create_note(f, a.dry_run, 1)
    mutate(
        "place-objects",
        {
            "whiteboardId": a.whiteboard,
            "objects": [{"id": cid, "objectType": "card"}],
            "destination": {"type": "point", "x": x, "y": y},
        },
        a.dry_run,
    )
    if a.section:
        grow_section(a.whiteboard, a.section, y + estimate_height(len(f.read_text().split())), a.dry_run)

    summary = {"card": {"id": cid, "title": title, "x": x, "y": y}, "under": a.under}
    if not a.dry_run:
        summary["lintIssuesOnNewObjects"] = new_lint_issues(
            a.whiteboard, {cid} | ({a.section} if a.section else set())
        )
    print(json.dumps(summary, indent=2))


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("row", help="create cards from markdown files and lay them out left to right")
    r.add_argument("--whiteboard", required=True)
    r.add_argument("--section-title", help='e.g. "Genjutsu Script (left to right)"')
    r.add_argument("--next-to", help="anchor object id (a section or card) to place the row next to")
    r.add_argument("--next-to-type", default="section", choices=["section", "card"])
    r.add_argument("--side", default="above", choices=["above", "below", "left", "right"])
    r.add_argument("--x", type=int)
    r.add_argument("--y", type=int)
    r.add_argument("--gap", type=int, default=GAP)
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("files", nargs="+", help="markdown files in left-to-right order; first '# heading' = title")
    r.set_defaults(func=cmd_row)

    v = sub.add_parser("variation", help="create a card directly under an existing block")
    v.add_argument("--whiteboard", required=True)
    v.add_argument("--under", required=True, help="card id of the block this varies")
    v.add_argument("--section", help="section id to grow so the new card stays inside")
    v.add_argument("--dry-run", action="store_true")
    v.add_argument("file")
    v.set_defaults(func=cmd_variation)

    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
