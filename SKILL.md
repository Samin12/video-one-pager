---
name: video-one-pager
description: >-
  Samin Yasar's own way of outlining a YouTube video before he films it: a one-page plan (Video idea,
  Goal of video, Key things to create, Intro, Why this matters, Level 1-3, CTA END) where every point
  gets an example, story or analogy and, when he screenshares, step-by-step moves; then his inline-note
  revisions; then a script written block by block (spoken lines as prose, on-screen moments as bullets)
  delivered as Heptabase cards laid out left to right, plus variations of any block and prompts for
  slide visuals. Use this whenever Samin asks for a one-pager, an outline or plan for his next video, to
  fold his notes into an outline, to turn an outline into a script, to write script blocks or cards in
  Heptabase, or for a new version of the intro or a level, even if he only says "outline this", "make
  the one-pager" or "write the script for this video". Prefer it over the generic outlines skill; reach
  for levels-format-video-outline only when he asks for its full packaging and dual-document delivery.
---

# Video One-Pager

This is how Samin plans a video: he outlines it on one page, marks the page up with notes, then scripts
it block by block on his Heptabase board. The format is his. Your job is to fill it with his material,
keep his wording, and never pad it with fields, results or numbers he didn't give you. He has to defend
every line on camera, so a plausible-sounding invention is worse than a visible gap.

Read before starting:

- [references/samin-rules.md](references/samin-rules.md): his notes in his own words, dated, and the
  standing rules they add up to. A newer note always beats an older rule.
- [references/template.md](references/template.md): the blank one-pager. Field names are his.
- [references/voice.md](references/voice.md): his stock lines, speech patterns and analogy bank. Read it
  before writing an intro, a Why this matters, or any script.

Read when you reach that stage:

- [references/script-blocks.md](references/script-blocks.md): script format, block list, slide prompts.
- [references/heptabase-delivery.md](references/heptabase-delivery.md): cards on his board, with
  `scripts/heptabase_blocks.py`.
- [examples/](examples/): the stock market video (reference one-pager) and the Genjutsu video (the whole
  loop: first draft, his notes, revised one-pager, script blocks, a Level 1 variation).

## The loop

1. Gather his material.
2. Write the one-pager.
3. Fold in his notes (repeat as often as he sends them).
4. Write the script blocks and put them on Heptabase, left to right.
5. Make variations of single blocks.
6. After he edits the cards, diff his versions against yours and record what changed.

He can enter at any stage: "give me the one-pager for this", a pasted outline full of notes, "now write
the blocks in Heptabase", "make a new variation of level one". Work out the stage from his message.

## 1. Gather before you write

- **His message is the brief.** Pull out the working title, the demos he wants to show, what it "means"
  (that becomes Why this matters), the things he says the video must explain ("what it is, how to use
  it, how to use it cheaply"), and anything he already made.
- **His Heptabase board.** If the video has a board, read it with the heptabase CLI:
  `heptabase whiteboard read <id> --mode content` for previews, `heptabase note read <cardId>` for a
  full card (ProseMirror JSON, convert it to text), `heptabase whiteboard cards <id>` for created and
  edited times. Look for his hook and intro drafts, his Why this matters cards (he rewrites these, so
  use the most recently edited one), prompts he already ran for demos, saved stories and analogies, and
  any template he edited himself. The board is his thinking; reuse it before writing anything new.
- **Reference videos.** Get transcripts with Eden `eden_read_social_post` (by URL) first, and fall back
  to `yt-dlp --skip-download --write-auto-subs --sub-langs "en.*"` for exact English. His own past
  videos are the best source of his voice and his reusable lines.
- **Facts that change a viewer's decision** (prices, limits, availability): verify against a current
  source, and name the source in your chat reply, not in the doc.
- Don't ask him for anything a tool can find. For things only he knows, put a `[bracketed placeholder]`
  in the doc rather than stopping to ask.

## 2. Write the one-pager

Use [references/template.md](references/template.md). What matters:

- **It's a planning doc.** Write as though the video hasn't been filmed, in his forward-looking planning
  voice. This holds even when he asks you to break down one of his published videos: write the page he
  would have written before filming it. No view counts, no results that only exist afterwards, no
  source or metrics line.
- **The fields are his:** Video idea, Goal of video, Key things to create, Intro, Why this matters,
  Level 1-3, CTA END. Don't add titles, key takeaways, a goal per point or talking points unless he asks.
  When his skeleton and an older message disagree, the more recent one wins.
- **Key things to create** is his prep list: the builds and demos, proof assets (a backtest, a
  before/after), cost screenshots, prompts for the description and classroom. Say when something
  already exists ("already made; pull the raw clip too for the before/after").
- **Intro** is bullets of what he'll say: the hook claim, a proof line (a placeholder if you don't know
  his result), "3 levels: (1) ..., (2) ..., (3) ...", then the objection killer ("Even if you've never
  ..., you can do this. We're just talking to ChatGPT."). His exact phrasings are in voice.md.
- **Why this matters** opens with his authority line, "the problem comes down to 3 things", then three
  points, each with its own Example / story analogy. When the video's tool fixes the problem in one
  place, add a short "The fix" block after the three points rather than a fourth point, so the
  "3 things" framing holds.
- **Every point** is a bold one-liner (what the viewer should get), then `Example / story analogy`
  (always) and `Step by step (screenshare)` only when he will actually show it on screen. Concept points
  don't get steps.
- **Levels:** three, and each must be a real step up. Setup belongs in Level 1. If he names demos, one
  level per demo is a strong default; say in chat that the split is your proposal. When breaking down
  an existing video, check the body against the intro's promise; the stock market video's intro said
  Level 2 was copy trading, but the body ran a trailing-stop bot first.
- **Analogies:** his own first (board cards, past videos, the bank in voice.md). Write a new one only
  when none of his fit, and tell him in chat which ones are new.
- **Placeholders** such as `[real result]`, `[credit cost of ...]` and `[your edit steps]` stand in for
  anything only he can supply. Never invent a result, a number or a personal story.
- **CTA END**, not Close: the "watch this next" line that points to his next video. No recap unless he
  asks for one.
- Save it locally (he keeps these in `~/decisons/video-one-pager/<slug>.md`) and show it in chat. He
  usually pastes approved one-pagers onto his board himself; only create a card when he asks.

## 3. Fold in his notes

He revises by pasting the one-pager back with notes inside it: `EDIT:` lines under a point, loose
bullets under a level, new mini-sections, rewritten lines, and things he deleted.

- **Every note goes in, in his words.** Keep his phrasing whenever it reads as a sentence he'd say.
- **Deleted stays deleted.** If he removed an example, a step, a point or a section, it doesn't come
  back. (He cut the cover-song analogy and the clothes and e-comm ad points; they stayed out.)
- **Order his notes logically.** He jots notes wherever the cursor is. Put setup before the first demo,
  but keep everything he said.
- **Leave what he didn't touch alone**, apart from consistency fixes his notes force: the intro's level
  breakdown, Key things to create, a level's title.
- A framing note ("mainly talk about the opportunity") becomes that level's opening line. A new
  mini-section he adds (like "Edit / Fragmentation help") becomes a labeled block where he put it.
- **He dictates.** Read mishearings in context: "gen two" is Genjutsu, and "pink cut" was the pink
  bottle from his typed demo prompt. When dictated and typed words disagree, trust the typed ones.
- **Return only the outline.** At most one line afterwards if you had to drop or reinterpret something.

## 4. Script blocks

When he asks for the script (his words: "for different blocks write different things ... a kind of a
script ... unless I am presenting something on the screen, then you can just have that as a bullet ...
going from left to right"):

- Write one block per section: Intro, Why This Matters, Level 1, Level 2, Level 3, CTA. Title them
  `Script N: <Section> — <name>`.
- Start from his own drafts. If his board has a Hook or intro card, script from it and change only what
  the one-pager changed; he put his own hook back over a newly written one.
- Everything he says is prose in his voice (voice.md), in short lines of one or two sentences, with each
  thing said once. Visuals that play while he talks go inline in square brackets (`[show analytics from
  my YouTube and Instagram videos]`). Everything he presents or walks through on screen (a demo, a
  screenshare step, a slide, a side by side) is a bullet he can talk over. Don't script what he'll
  ad-lib while showing something. Keep demos out of Why This Matters.
- Carry every placeholder through. The CTA block is the "watch this next" line plus an end-screen bullet.
- Deliver them as Heptabase cards in a row, left to right, inside a section named
  `<Video> Script (left to right)`, using `scripts/heptabase_blocks.py row`. Keep local copies in
  `~/decisons/video-one-pager/<slug>-script/`. Formats are in
  [references/script-blocks.md](references/script-blocks.md), commands in
  [references/heptabase-delivery.md](references/heptabase-delivery.md).

## 5. Variations

"Make a new variation of level one" means a new card; the old one stays.

- Title it `Script N (v2): ...` and put it directly under the original block in the same column
  (`scripts/heptabase_blocks.py variation`), growing the section to fit. The left-to-right order stays
  intact, and the alternative sits with the block it would replace.
- Follow the order he dictates. His Level 1 for a tool video went: what's new (a slide) → why we run it
  from this app → "we're going to need the desktop app" → Step 1, set up the desktop app → Step 2,
  connect the plugin, then ask "Do you have access to <tool>?" → Step 3, start using it with the first
  demo → what else it can do (tease the later levels) → how to do it cheaply → recap.
- When he mentions a slide or a visual, write the image prompt in his slide style (script-blocks.md)
  and put it at the bottom of the card.
- When he picks a variation, he renames it, swaps it into the row, and folds the old block. Leave that
  layout alone.

## After he edits the cards

He often edits cards on the board without telling you. Before the next round, export his versions
(`python3 scripts/pm_to_md.py <cardId>`) and diff them against what you wrote. His changes are the
clearest signal of what he wants. Add anything new to references/samin-rules.md with the date.

## Before you hand anything back

- Field names match the template, or his latest edits to it.
- Planning voice throughout, with no after-the-fact numbers.
- Every point has an example or story; steps appear only where he screenshares.
- Nothing is invented: results, costs and pipeline steps are sourced or bracketed.
- Every one of his notes is in, and his deletions stayed deleted.
- Scripts start from his own drafts, use short lines, put visual cues inline in [brackets], and keep
  bullets for what he presents on screen.
- Heptabase: cards run left to right inside the section, lint shows no new issues on your objects, and
  none of his cards were overwritten.
