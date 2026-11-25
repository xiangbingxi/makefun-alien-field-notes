# Handoff — Alien Field Notes: The Two Day Earth

Competition: `u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000`
($2, deadline 2026-11-26 19:55 CST, max 200 characters)
Bounty page: https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000
Repo name: `makefun-alien-field-notes`

## Method

- Pulled the kit from the competition kit URL and read `RULES.txt` /
  `competition.yaml`: the program writes one UTF-8 text of 1–200
  characters to `/output/entry.txt`; only a valid entry goes before the
  judge.
- `main.py` was written by hand in two passes: v1 wrote the entry
  verbatim; v2 adds a real improvement — a 1–200 character guard plus a
  read-back check that exits with an error if the written file differs
  from the entry by even one character. It reads no external files and
  makes no network calls.
- The entry text is the user's GPT draft, submitted exactly as spoken,
  one character unchanged.

## Entry

Earth, 4/5: They charge for water but give you as much gravity as you want, which feels like an oversight.

- Characters: 106 (limit 200)
- Bytes: 106 (pure ASCII, UTF-8)
- SHA-256 of `/output/entry.txt`: `e33eba12a3cbb6d80fa05ba9a8e566353ba7c917e41bbac6042f2dda0cfff40b`
- No trailing newline (last byte `0x2e`, `.`); `entry.txt` is byte-identical to `prompt.txt`.

## Verification

- Ran `main.py` twice (v2): both runs exit 0, outputs `cmp`-identical.
- Both runs: 106 bytes / 106 characters, SHA-256 `e33eba12…fff40b`.
- `python3 -m py_compile main.py`: OK.
- `LICENSE` is MIT with an `SPDX-License-Identifier: MIT` line.
- `README.md` carries the bounty link and the three official badges.
- `.makefun/owner.json` holds the user's wallet.

## Status

Files complete in `~/workspace/makefun/alien-field-notes/repo/`.
Not submitted, no GitHub repo created, no bundle touched — as instructed.
