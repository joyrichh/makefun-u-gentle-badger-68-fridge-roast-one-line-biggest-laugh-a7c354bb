"""Print the Fridge Roast entry."""

import sys

LINE = "My smart fridge has three cameras and no ice. It's gathering evidence against itself."


def main() -> None:
    if sys.argv[1:] == ["--check"]:
        assert 0 < len(LINE) <= 200
        assert LINE == LINE.strip()
        assert LINE.isprintable()
        return
    if sys.argv[1:]:
        raise SystemExit("usage: python3 main.py [--check]")
    print(LINE)


if __name__ == "__main__":
    main()
