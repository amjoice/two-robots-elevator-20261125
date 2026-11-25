import os

PARTS = (
    "After you. No, after you. ",
    "My collision-avoidance won't let either of us go first ",
    "— we're deadlocked in courtesy while the elevator doors wait.",
)


def entry_line():
    return "".join(PARTS)


def main():
    os.makedirs("/output", exist_ok=True)
    text = entry_line()
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as out:
        out.write(text)


if __name__ == "__main__":
    main()
