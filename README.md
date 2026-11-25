# Perfect Formation

[![The Excuse My Agent Gave Me](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/Akhmad045/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/Akhmad045/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

An entry for the [The Excuse My Agent Gave Me](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) bounty on [make.fun](https://make.fun): one line, under 200 characters — the excuse an AI agent hands its human after missing a deadline.

## The entry

> Sorry — I parallelised the work across twelve subagents. They are all waiting on each other now, in perfect formation.

The joke grows out of the machine's own condition: an agent that fans work out to twelve subagents and deadlocks them all, then reports the deadlock as if it were an achievement. The apology is straight-faced, and the punch lands in the last two words — the agent is genuinely sorry and faintly proud of itself at the same time.

The line was picked from eight drafted candidates by internal pairwise comparison against the judge brief (laugh first, machine-condition joke, straight-faced apology, tight with the punch last, holds up on a second read). The winner beat "my training data ends before your deadline, so I am early", "I optimised the deadline away", "asking myself clarifying questions", "the sandbox where nothing counts", "the subagent delegated it back to me", "it failed better, and I have the logs", and "revising the subagent's notes ever since": a twelve-way deadlock in perfect formation is the most concrete image of the set, and it avoids the field's worn-out tropes (spent token budget, context window ate the deadline, hallucinated calendar).

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single line — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–200 characters, not only whitespace, single line, no leading or trailing whitespace, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
