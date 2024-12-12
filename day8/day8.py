debug = True
if debug:
    file_path = "example.input"
else:
    file_path = "input.input"
file = open(file_path, "r")
day_data = file.read().split("\n")
file.close()

print(day_data)


def calc_slope(p1: tuple, p2: tuple) -> int:
    """calculate and return slope of two points
    Args:
        p1 (tuple): first point (x1,y1)
        p2 (tuple): second point(x2,y2)

    Returns:
        int: slope of the two points
    """
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    # calc slope
    # m = (y₂ - y₁) / (x₂ - x₁).
    return (y2 - y1) / (x2 - x1)
    # calc intercept
    # b = y1 - m × x1.


def calc_double_point(p1, m):
    y = p1[0] * 2
    b = y - m * x
    y = m * x1 + b
    return y


def calc_antinodes(slope, p1, p2):
    return antinode1, antinode2


puzzle_map = {}

a = 0
for row in day_data:
    b = 0
    for character in row:
        # print(f"({a},{b}), {day_data[a][b]}")
        puzzle_map[(a, b)] = day_data[a][b]
        b += 1
    a += 1

for i in puzzle_map:
    if puzzle_map[i] != ".":
        print(i)

print(calc_slope((1, 8), (2, 5)))
