"""The Battery's Last Text to Its Charger — make.fun entry.

The program writes the phone battery's last text message to its
charger to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Deterministic: no network, no randomness, no clock.
"""

import os

# The entry: one line, 169 characters (limit 200), plain text.
ENTRY_TEXT = (
    "1%. i waited all day by the outlet while you charged his phone, "
    "so i'm breaking up with you by text. fitting, honestly. "
    "tell the toaster i said hi \u2014 she always shows up."
)


def write_entry(text: str, out_dir: str) -> str:
    """Write ``text`` to ``entry.txt`` inside ``out_dir``; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
