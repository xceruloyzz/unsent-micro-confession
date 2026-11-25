# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/xceruloyzz/unsent-micro-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/xceruloyzz/unsent-micro-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for the [make.fun bounty "Unsent: The Micro-Confession Sprint"](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba):
write one micro-confession in exactly two parts — a `To:` line naming
who it was meant for, and the unsent message itself, one line written
exactly as it was typed.

`main.py` is the harness driver (program/v1): it writes the confession
to `/output/entry.txt` — the same text on every run, no input, no
network, no randomness.

> To: Dad
>
> I practiced telling you I quit the job you brag about at every family dinner, then deleted it because I could already hear the silence on your end.

155 characters total (message line 147). The reason it stayed in
drafts is felt, not stated: the confession was typed, rehearsed, and
deleted — too afraid of the silence on the other end. The `To:` line
and the message need each other: only Dad brags about that job at
every family dinner, so swapping the addressee would break it.

## Local check

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 155 chars, byte-identical on every run
```

## License

MIT — see [LICENSE](LICENSE).
