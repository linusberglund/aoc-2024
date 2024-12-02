from pathlib import Path

################################################################################


def part1(data):
    left = []
    right = []

    for line in data:
        left.append(line[0])
        right.append(line[1])

    left.sort()
    right.sort()

    total_distance = []

    for x, y in zip(left, right):
        total_distance.append(abs(x - y))

    return sum(total_distance)


################################################################################


def part2(data):
    left = []
    right = []

    for line in data:
        left.append(line[0])
        right.append(line[1])

    similarity_score = 0

    for n in left:
        similarity_score += n * right.count(n)

    return similarity_score


################################################################################


def parse(path):
    data = Path(path).read_text().splitlines()
    data = [n.split("   ") for n in data]
    data = [[int(n) for n in line] for line in data]
    return data


data = "src/day01/input.txt"
data = "src/day01/example.txt"

print(part1(parse(data)))
print(part2(parse(data)))
