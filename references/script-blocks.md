# Script blocks

The script turns the approved one-pager into what he'll say, block by block. Each block is one
Heptabase card. He films with the cards open (or on his prompter), so a card has to read top to bottom
without jumping around.

## Blocks and titles

| # | Title | Source in the one-pager |
|---|---|---|
| 1 | `Script 1: Intro` | Intro bullets |
| 2 | `Script 2: Why This Matters` | Why this matters, including any "fix" block |
| 3 | `Script 3: Level 1 — <name>` | Level 1 |
| 4 | `Script 4: Level 2 — <name>` | Level 2 |
| 5 | `Script 5: Level 3 — <name>` | Level 3 |
| 6 | `Script 6: CTA` | CTA END |

Variation: `Script 3 (v2): Level 1 — <new name>`, placed under Script 3 (see heptabase-delivery.md).

## Prose, inline cues and bullets

- **Prose** is anything he says. Write it in his voice (voice.md): short lines, "So," / "Okay," /
  "Now,", his stock lines. One or two sentences per paragraph; he splits anything longer. Say each
  thing once.
- **Inline cues** are visuals that play while he talks (a montage, analytics, a character sheet). They
  go in square brackets inside the spoken line, the way he writes them: `...gets hundreds of thousands
  of views. [show analytics from my YouTube and Instagram videos]`.
- **Bullets** are what he presents or walks through on screen: a demo, a screenshare step, a slide, a
  side by side, the end screen. Write the bullet as what's on screen, not what he says about it; he
  ad-libs over it. A step-by-step screenshare is a bullet list, one step per bullet, with arrows allowed
  inside a bullet.
- Placeholders carry through: `[real result]`, `[costs]`. He often fills them in himself on the card.

Pattern:

```markdown
# Script 3: Level 1 — What Genjutsu Is + Your First Edit

All right, level one. Let's start with what Genjutsu actually is.

Genjutsu edits videos you already have, and it does it in two ways.

- Genjutsu page: upload a 4–30 second clip + up to 30 reference images → pick Motion Transfer or Object Swap

Now, you can do all of this on the website. But we're going to do it the easy way, by just talking to
ChatGPT. And setting it up is kind of like pairing Bluetooth.

- Download the ChatGPT desktop app
- Add the Higgsfield plugin
- Ask: "Do you have access to Genjutsu?"
```

## What each block needs

- **Intro:** if his board has a Hook or intro card, start from it word for word and change only what
  the one-pager changed; he replaced a newly written hook with his own. Otherwise: the hook claim with
  inline cues, the proof line, the three levels, then the objection killer and "Let's get into it."
- **Why This Matters:** "Okay, before we get into anything..." then his authority line, the old way, the
  three things with their stories, the fix (name the whole setup, e.g. "ChatGPT + Genjutsu"), and "So
  let's get into level one." Reuse his latest Why-this-matters draft from the board; it's usually already
  in his words. No demo bullets here; he cut them.
- **Levels:** open with the level's framing line (his note, if he gave one), then each point: the spoken
  explanation with its analogy, then the screen bullets. End Level 1 with a short recap. Level 2 and 3
  can end on a show-it-end-to-end bullet or a costs bullet, whichever his notes ask for.
- **CTA:** the "watch this next" line and one `End screen: next video` bullet. No recap unless he asks.

## Slide visual prompts

When he says "slide", "visual" or "write the prompt for the visual", add a `## Slide visual prompt`
section at the bottom of the card and point to it from the bullet (`- Slide: "<title>" (visual prompt at
the bottom)`).

His slide look (matches his chapter cards and his levels graphics): a clean white background with a
faint light-gray grid, a large bold black sans-serif title (Inter Extra Bold), one small gray subtitle,
blue numbered circles, rounded cards with a soft shadow, and very little text. Keep the words short,
because image models misspell long text. Say "no logos, no watermark". Where real footage exists,
suggest swapping generated frames for real stills.

Example (the Genjutsu "What's new" slide):

> 16:9 presentation slide on a clean white background with a faint light-gray grid. Top left: the word
> "Genjutsu" in large bold black sans-serif (Inter Extra Bold), with one small gray line under it: "Edit
> the video you already have. No reshoot." Below, two equal cards side by side with rounded corners and
> a soft shadow. Left card: a blue circle with a white "1", the label "Motion Transfer", and two video
> frames joined by a blue arrow: a man in a plain white t-shirt talking to camera in a room, then the
> exact same pose as a different person on a neon-lit city street. Caption: "Same motion. New person,
> place and look." Right card: a blue circle with a white "2", the label "Object Swap", and two frames
> joined by a blue arrow: a hand holding a pink bottle, then the same hand holding a glowing purple
> magic orb. Caption: "Change one thing. Keep the rest." Flat, modern and minimal, lots of white space,
> crisp legible text, no logos, no watermark.

Only write the prompt unless he asks you to render it. If he does, use his image pipeline (Higgsfield
`gpt_image_2_5` with his references, or ChatGPT images).
