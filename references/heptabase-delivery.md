# Putting blocks on his Heptabase board

Everything goes through the `heptabase` CLI (0.6+). The desktop app has to be running (`heptabase start`
launches it). Don't touch Heptabase's local files or databases.

## The fast path: `scripts/heptabase_blocks.py`

```bash
# Six script blocks in a row, left to right, inside a titled section, above an existing section:
python3 scripts/heptabase_blocks.py row \
  --whiteboard <whiteboardId> \
  --section-title "Genjutsu Script (left to right)" \
  --next-to <sectionOrCardId> --next-to-type section --side above \
  1-intro.md 2-why-this-matters.md 3-level-1.md 4-level-2.md 5-level-3.md 6-cta.md

# A variation directly under the block it replaces, growing the section to fit:
python3 scripts/heptabase_blocks.py variation \
  --whiteboard <whiteboardId> --under <originalCardId> --section <sectionId> \
  3b-level-1-v2.md
```

Add `--dry-run` to print every call and payload without changing the board (reads still run). Use
`--x/--y` instead of `--next-to` to place at an exact point, or leave both out for automatic placement.
The script creates the notes (the first `# heading` is the card title), places and arranges them, adds
the section, sizes the section to the cards' measured heights (or estimates them when Heptabase hasn't
rendered the cards yet), then runs `lint` and reports any issue that involves the new objects.

## Before you place anything

- **Re-read the layout.** He moves sections around (he moved the Genjutsu script section right after it
  was placed). Use `heptabase whiteboard read-layout <id>`, or focus it:
  `echo '{"whiteboardId":"<id>","focus":{"objects":[{"id":"<cardId>","objectType":"card"}]}}' | heptabase whiteboard read-layout --input -`
- **Check that the target area is empty** with a viewport read:
  `{"whiteboardId":"<id>","viewport":{"x":...,"y":...,"width":...,"height":...}}`
- **Never overwrite his cards.** A card he has marked up holds his notes. Add new cards and leave his.

## Input shapes (verified 22 Sep 2026, CLI 0.6.0)

The mutation commands take `--input <file|->` JSON, and `--help` doesn't show the schema.

- `place-objects`: `{whiteboardId, objects:[{id, objectType:"card"}], destination:{type:"auto"} | {type:"point", x, y} | {type:"nextTo", objectId, objectType, side:"above"|"below"|"left"|"right"} | {type:"inSection", sectionId}}`
- `arrange-objects`: `{whiteboardId, objects:[...in order], layout:{type:"row"|"column"|"grid", gap:<number>}}`. The first object is the anchor.
- `move-objects`: `{whiteboardId, moves:[{selection:{type:"objects", objects:[...]}, destination:{type:"delta", dx, dy} | {type:"point", x, y} | {type:"nextTo", ...}}]}`
- `create-section`: `{whiteboardId, objects:[...], title}`
- `resize-objects`: `{whiteboardId, resizes:[{mode:"setSize", id, objectType, width, height} | {mode:"fitToContent" ...} | {mode:"defaultSize" ...} | {mode:"setFolded" ...}]}`
- `remove-objects`: `{whiteboardId, removals:[{id, objectType}]}`. Removing a section keeps its cards on the board.
- `read-layout --input`: `{whiteboardId, focus:{objects:[...]}}` or `{whiteboardId, viewport:{x, y, width, height}}`
- `screenshot --input <same> -o out.png --force` renders a schematic PNG for checking the layout.

## Gotchas

- **Unknown keys are dropped silently,** so a probe that happens to be valid runs for real. A
  `create-section` probe with just `{whiteboardId, objects}` put a stray "Section 1" around his Hook card.
  Discover fields only with input that's definitely invalid (wrong types, empty discriminators). If you
  do create something by accident, remove it straight away, check nothing moved, and tell him.
- `nextTo` places several cards edge to edge (no gap) using unmeasured heights, so a tall card can run
  into whatever is below. Arrange with a gap (80 works), then check.
- New cards report `size 520x?` until the app renders them. Estimate about 3.6 px per word plus 300 when
  sizing the section, and re-check after he opens the board. Measured on 22 Sep: 207 words came to 993
  px and 437 words to 1,679 px.
- Sections don't grow on their own. Resize the section when you add a card below.
- `lint` also lists his older overlaps. Only issues involving your objects are yours to fix.
