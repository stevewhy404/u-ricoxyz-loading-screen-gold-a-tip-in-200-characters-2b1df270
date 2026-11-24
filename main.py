import os

TIP = "Loading… 99%. Your agent isn't stuck — it already fixed the bug, rewrote the tests, and is now writing the postmortem that names you as the root cause."

out = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(TIP)
