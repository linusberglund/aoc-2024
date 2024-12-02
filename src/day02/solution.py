from pathlib import Path

from aocd import submit

################################################################################


def part1(data):
    safe_reports = 0

    for line in data:
        increasing = line[0] < line[1]
        prev = None
        safe = True

        for x in line:
            if prev is None:
                prev = x
                continue

            if increasing:
                if x <= prev or x > prev + 3:
                    safe = False

            if not increasing:
                if prev <= x or prev > x + 3:
                    safe = False

            if safe is False:
                break

            prev = x

        safe_reports += safe

    return safe_reports


################################################################################


def part2(data):
    safe_reports = 0
    dampen = []

    for line in data:
        increasing = line[0] < line[1]
        prev = None
        safe = True

        for i, x in enumerate(line):
            if prev is None:
                prev = x
                continue

            if increasing:
                if x <= prev or x > prev + 3:
                    safe = False

            if not increasing:
                if prev <= x or prev > x + 3:
                    safe = False

            if not safe:
                dampen.append((line, i))
                break

            prev = x

        # print(line, safe)
        safe_reports += safe

    # print()

    for line, i in dampen:
        line.pop(i)

        increasing = line[0] < line[1]
        prev = None
        safe = True

        for x in line:
            if prev is None:
                prev = x
                continue

            if increasing:
                if x <= prev or x > prev + 3:
                    safe = False

            if not increasing:
                if prev <= x or prev > x + 3:
                    safe = False

            if safe is False:
                break

            prev = x

        # print(line, safe, i)
        safe_reports += safe

    return safe_reports


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [line.split(" ") for line in data]
    data = [[int(x) for x in line] for line in data]

    return data


def auto_submitter():
    example_part1 = 2
    example_part2 = 4

    if example_part1 == part1(parse("src/day02/example.txt")):
        print(f"PART 1 EXAMPLE PASS ({example_part1}), SUBMITTING")
        submit(part1(parse("src/day02/input.txt")), part="a", day=2, year=2024)

        if example_part2 == part2(parse("src/day02/example.txt")):
            print(f"PART 2 EXAMPLE PASS ({example_part2}), SUBMITTING")
            submit(part2(parse("src/day02/input.txt")), part="b", day=2, year=2024)


data = "src/day02/input.txt"
data = "src/day02/example.txt"

# print(part1(parse(data)))
# print(part2(parse(data)))

auto_submitter()

# clear && ruff format . && ruff check --fix --select I . && ruff check --fix .
# clear && ruff format ./src && ruff check --fix --select I ./src && ruff check --fix ./src
# clear && py .\src\day02\solution.py
