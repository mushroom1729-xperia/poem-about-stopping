import os

TEXT = """I'll take the dishes,' you say,
and I dry them longer.
The rack fills drop by drop.
One plate left not put away
intentional empty space."""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(TEXT)