import os
import sys

ENTRY = "My fridge freezes the lettuce, warms the ice cream, and hums like it's proud of itself. One job, zero talent."

def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod("/output/entry.txt", 0o644)
    except OSError:
        pass
    sys.stdout.write(ENTRY)

if __name__ == "__main__":
    main()
