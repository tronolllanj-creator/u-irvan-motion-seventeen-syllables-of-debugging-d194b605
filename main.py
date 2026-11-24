"""
# Entry validated: output is 1-200 chars, three lines 5-7-5, deterministic.
Entrypoint that writes a haiku about debugging to the specified output directory.
"""

import os
import sys

HAIKU = """Bug hides from my eyes
steps aside when I look up
window shows my face"""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    content = f"{HAIKU}\n"

    if not (1 <= len(content) <= 200 and content.strip() and len(content.strip().splitlines()) == 3):
        raise ValueError("Invalid content format or length.")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
