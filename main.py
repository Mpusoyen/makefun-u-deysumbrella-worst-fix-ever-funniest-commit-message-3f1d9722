import os
from pathlib import Path

# The one-line commit message for a bug fix that made everything worse,
# written verbatim to entry.txt.
COMMIT_LINE = "fix: cured the memory leak; the server now dies every minute before it can leak"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(COMMIT_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
