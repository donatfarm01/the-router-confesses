"""The Router Confesses — make.fun entry.

Writes one line to /output/entry.txt: the excuse a home Wi-Fi router
gives for dropping the connection at the exact climax of a movie.

The line is a film-noir confession: the router is not apologising for a
glitch, it is owning the act. It read the script, hated the ending, and
pulled its own plug — the twist villain of the movie turns out to be the
box blinking in the corner of the room.
"""

import os

ENTRY = "Plot twist: the killer was me. I read the script, hated the ending, and pulled my own plug."

MAX_CHARS = 200


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character, and the
    # entry is exactly one line, so the file holds the line and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
