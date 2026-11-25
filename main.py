"""Write the 3 AM commit message to /output/entry.txt.

The entry is a single commit message, exactly as an AI agent would
write it right after breaking production at 3 AM.
"""

import os

# The joke's angle: the agent's "fix" was a revert, and the revert
# itself shipped the bug again -- the classic 3 a.m. move of
# breaking production twice while trying to unbreak it once.
# The commit-message shape ("fix: ...") and the precise timestamp
# (3:07 a.m.) are what make it read like a real commit, not a caption.
LINE = (
    "fix: reverted last night's deploy at 3:07 a.m.; "
    "the revert deployed the same bug twice, "
    "so production is now broken in stereo"
)


# Deterministic: the same single line on every run, no randomness,
# no network, stdlib only. Output is written with no trailing
# newline so the file is exactly the commit message.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
