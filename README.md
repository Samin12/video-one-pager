# video-one-pager

Samin's way of outlining a YouTube video before he films it, packaged as a skill. It covers the
one-page plan (Video idea, Goal of video, Key things to create, Intro, Why this matters, Level 1-3,
CTA END), where every point gets an example, story or analogy and a screenshare walkthrough when he
shows something on screen. From there it folds in his inline notes, writes the script block by block as
Heptabase cards laid out left to right, and makes variations of single blocks with slide visual prompts.

## Install

Claude Code:

```bash
git clone https://github.com/Samin12/video-one-pager ~/.claude/skills/video-one-pager
```

Codex:

```bash
git clone https://github.com/Samin12/video-one-pager ~/.codex/skills/video-one-pager
```

Update later with `git -C <that folder> pull`.

## Use

- Claude Code: `/video-one-pager`, or just ask: "make the one-pager for my next video about ...",
  "here are my notes, give me back the outline", "write the script blocks in Heptabase", "make a new
  variation of level one".
- Codex: `$video-one-pager`.

Give the agent your idea (dictated is fine), the demos you want to show, and your Heptabase board if the
video has one. It reads the board and any reference videos, writes the one-pager in your planning voice,
takes your marked-up copy back, then writes the script cards left to right on the board.

Needs: the Heptabase desktop app with the local CLI enabled (`heptabase` 0.6+). Optional: the Eden MCP
or `yt-dlp` for transcripts.

## What's inside

- `SKILL.md`: the workflow agents follow.
- `references/template.md`: the blank one-pager, with Samin's field names.
- `references/samin-rules.md`: his notes in his own words, dated, plus the standing rules. Add new notes
  here.
- `references/voice.md`: his stock lines, speech patterns and analogy bank.
- `references/script-blocks.md`: script format (prose, inline cues, bullets) and slide visual prompts.
- `references/heptabase-delivery.md`: whiteboard input shapes, placement recipes and gotchas.
- `scripts/heptabase_blocks.py`: puts script blocks on a board left to right inside a section (`row`), or
  a variation under its block (`variation`). `--dry-run` prints the calls.
- `scripts/pm_to_md.py`: turns a Heptabase card into markdown, for reusing his drafts and diffing his
  edits.
- `examples/stock-market-video/`: the reference one-pager ("Claude Just Changed the Stock Market
  Forever!").
- `examples/genjutsu-video/`: the whole loop (first draft, his notes, revised one-pager, script blocks,
  Level 1 variation) with his own edits.
