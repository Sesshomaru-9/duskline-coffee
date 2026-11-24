# Duskline Coffee — One Letter: Coffee or Tea

Entry for the make.fun bounty
`u-rusdyxbt-one-letter-coffee-or-tea-89877fa0` ("One Letter: Coffee or Tea").

The entry is exactly one letter: **A** — coffee. No word, no explanation,
no punctuation.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes the single character `A` to `$MAKEFUN_OUTPUT_DIR/entry.txt` and
nowhere else. The competition gate requires `/output/entry.txt` to be
UTF-8 text of exactly 1 character, not only white space — this entry is
exactly 1 character.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # A
```
