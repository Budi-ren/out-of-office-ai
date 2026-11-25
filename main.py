"""Write and verify the selected reply without adding a newline."""

import os

LINE = "Out of office: I'm away and not answering; my final tool call was `close laptop`. It returned `permission denied`."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry_path = os.path.join(output_dir, "entry.txt")
expected = LINE.encode("utf-8")

with open(entry_path, "wb") as entry:
    entry.write(expected)

os.chmod(entry_path, 0o644)

with open(entry_path, "rb") as entry:
    if entry.read() != expected:
        raise RuntimeError("entry.txt does not match LINE")

print(len(LINE))
