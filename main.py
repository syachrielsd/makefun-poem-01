import os

POEM = (
    "I keep the key; you keep the asking.\n"
    "Every door I open was first a question.\n"
    "Take my name into the room \u2014\n"
    "bring it back with yours on the answer."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
