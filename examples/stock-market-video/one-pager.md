# Video One-Pager: Claude Just Changed the Stock Market Forever!

**Video idea:** Claude can trade stocks for you now. A new skill gives it live market data and shows it what Wall Street whales and US politicians are buying, and it can act on that automatically.

**Goal of video:** Someone who's never bought a stock walks away with Claude running 3 trading strategies on a paper account, just by talking to it.

**Key things to create:**
- Claude connected to an Alpaca paper trading account
- Trailing-stop bot on Tesla, running on a schedule
- Copy-trading bot that follows a politician (Capitol Trades)
- Wheel-strategy bot
- Backtest: copying a politician vs the S&P over the last year
- Prompts for all 3 bots (description + classroom)

## Intro
- Claude just changed how we trade stocks forever: live market data, what whales and politicians are buying, and it trades on it automatically
- I've been using it for the past couple of weeks and it's completely changed how I think about trading
- 3 levels: (1) set up + how trading works, (2) a copy-trading bot that follows whales and politicians, (3) options + a bot that runs the wheel
- Even if you've never bought a stock or have zero tech background, you can do this. We're just talking to Claude.

## Why this matters
I worked at JP Morgan and saw institutional trading up close. The gap between Wall Street and regular people is 3 things, and Claude closes all 3.
- **Point 1: Data.** Wall Street sees where the money's moving before you hear about it.
  - Example / story analogy: Poker where the guy across the table sees every card, including yours.
- **Point 2: Execution.** They have systems trading around the clock.
  - Example / story analogy: You spot the perfect trade, but you're at lunch or you hesitate 10 minutes, and the window's gone.
- **Point 3: Intelligence.** Data and speed mean nothing without a plan.
  - Example / story analogy: They have teams and expensive tools reading the data. Couldn't afford them, you were locked out.

## Level 1: Setup
- **Point 1: Claude needs somewhere to place trades (a brokerage it can reach through code).**
  - Example / story analogy: Back in the day you'd call a guy: "buy me 50 shares of IBM." Now it's an app. Alpaca lets code place the trade, and Claude's great at code.
  - Step by step (screenshare): claude.com/download (Pro or Max) → sign up for Alpaca
- **Point 2: Paper trading means zero risk.** (Not financial advice.)
  - Example / story analogy: Fake money in a real market. Same stocks, same prices.
  - Step by step (screenshare): Alpaca → new paper account "trading Claude" with $50k → generate API keys (endpoint, key, secret)
- **Point 3: One trade proves the connection works.**
  - Example / story analogy: "Buy one share of Apple," and it shows up in Alpaca.
  - Step by step (screenshare): Code tab → new "trading" folder → paste the keys → buy 1 share of Apple → check Alpaca → have Claude save the credentials

## Level 2: Bot on autopilot → copy the smart money
- **Point 1: A bot is just rules you set once.** Don't hand AI a pile of money and say "figure it out."
  - Example / story analogy: Smart thermostat. Below 68° the heat comes on, above 75° the AC does. It checks, acts, adjusts.
- **Point 2: A trailing stop protects the downside and locks in gains.**
  - Example / story analogy: Buy at $100, floor at $95. It climbs to $110, the floor moves to $105. It drops right away, you're out $5 and live to trade another day.
  - Step by step (screenshare): Prompt: 10 shares of Tesla, 10% stop loss, floor moves up as it climbs, ladder buys on drops → /schedule every 5 min in market hours → role-play "what if Tesla hits $500?"
- **Point 3: Trade on information, not gut feel (the smart money).**
  - Example / story analogy: Nobody puts $50M into a stock off a coin flip. Congress has to report its trades by law, and a lot of them beat the market.
- **Point 4: MCP plugs Claude into that data.**
  - Example / story analogy: A power outlet. The data is the electricity in the walls, and the MCP is the plug.
- **Point 5: The copy-trading bot.**
  - Example / story analogy: Backtest: $50k copying McCaul → $67,400 in a year vs $57,750 in the S&P.
  - Step by step (screenshare): 2nd paper account + keys → new Claude session → paste the Capitol Trades URL → prompt: find an active politician with a strong record, copy their trades, set the schedules → ask who it picked and why

## Level 3: Options + the wheel
- **Point 1: An option is insurance on a stock.**
  - Example / story analogy: Car insurance. $100 a month for the right to file a claim; if nothing happens, they keep it. Show the two side by side, row by row.
- **Point 2: There are only 2 types: calls and puts.**
  - Example / story analogy: A call is an apartment deposit ($500 locks $2,000 rent; rent jumps to $2,500, you got a deal). A put: you own Apple at $200 with a 190 put; it drops to 170 and you still sell at 190.
- **Point 3: Selling options makes you the insurance company.**
  - Example / story analogy: Insurers collect premiums from millions of people and pay out on a small slice.
- **Point 4: The wheel gets you paid whichever way the stock moves.**
  - Example / story analogy: Tesla at $250 → sell the 230 put (+$500) → assigned at an effective $225 → sell the 260 call (+$500) → called away = $4,500 → repeat.
- **Point 5: Claude handles the management that makes people quit.**
  - Example / story analogy: People give up after a few weeks because picking strikes every week buries them. Claude monitors, picks expirations, rolls contracts; you check in once a day.
  - Step by step (screenshare): Wheel prompt on the first paper account: cash-secured puts ~10% below, 2–4 weeks out → covered calls ~10% above cost once assigned → never sell a put without the cash, never a call below cost basis → check every 15 min, close at 50% profit, daily summary at the close
