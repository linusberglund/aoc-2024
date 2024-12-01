import re
from pathlib import Path
from pprint import pp

from aocd import submit

################################################################################


def part1(data):
    pass


################################################################################


def part2(data):
    pass


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    return data


def auto_submitter():
    example_part1 = False
    example_part2 = False

    if example_part1 == part1(parse("src/dayXX/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/dayXX/input.txt")), part="a", day=0, year=2024)

        if example_part2 == part2(parse("src/dayXX/example.txt")):
            print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
            submit(part2(parse("src/dayXX/input.txt")), part="b", day=0, year=2024)


data = "src/dayXX/input.txt"
data = "src/dayXX/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))

auto_submitter()

# clear && ruff format . && ruff check --fix --select I . && ruff check --fix .
# clear && ruff format ./src && ruff check --fix --select I ./src && ruff check --fix ./src
# clear && py .\src\dayXX\solution.py
