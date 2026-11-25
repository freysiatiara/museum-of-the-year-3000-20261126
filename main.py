"""Museum of the Year 3000 -- one-line museum label entry.

Writes the chosen label, a single line of at most 200 characters, to
/output/entry.txt (or the path the environment asks for).
Standard library only.
"""

import os

LINE = "Retractable pen, c. 2023. A tiny sword, drawn with a click, used to sign away money and then lost forever."


def output_path():
    """Resolve where entry.txt goes; never rely on the working directory."""
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        if os.environ.get(var):
            return os.path.join(os.environ[var], "entry.txt")
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    # Validation guard: the gate accepts 1-200 non-blank characters, one line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read-back check: what landed on disk must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written entry differs from the chosen line"


if __name__ == "__main__":
    main()
