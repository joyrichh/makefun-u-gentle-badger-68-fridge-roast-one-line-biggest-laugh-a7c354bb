# Fridge Roast

[![Competition](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/joyrichh/makefun-u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/joyrichh/makefun-u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

[Bounty](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

> My smart fridge has three cameras and no ice. It's gathering evidence against itself.

## How it works

`main.py` prints the 85-character roast stored in `LINE`, followed by one
newline. It uses no network, files, randomness, or timestamps, so repeated
runs produce identical bytes.

## Run

Target runtime: Python 3.13; no third-party packages. Run from this directory:

```sh
python3 main.py
python3 main.py --check
```

`--check` silently asserts that the line is nonempty, at most 200 characters,
printable, and free of leading or trailing whitespace. Success exits zero;
unsupported arguments are rejected.
