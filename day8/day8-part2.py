from pprint import pp as pp
from itertools import combinations

debug = False
if debug:
    file_path = "example.input"


else:
    file_path = "input.input"
file = open(file_path, "r")
day_data = file.read().split("\n")
file.close()


puzzle_map = {}

a = 0
for row in day_data:
    b = 0
    for character in row:
        puzzle_map[(a, b)] = day_data[a][b]
        b += 1
    a += 1

freqs = {}
for i in puzzle_map:
    if puzzle_map[i] != ".":
        freqs[i] = puzzle_map[i]


def calc_anti_nodes(p1, p2, con):
    nodes = []
    inside_constraints = True
    diff = (p2[0] - p1[0], p2[1] - p1[1])
    an1 = p1[0] - diff[0], p1[1] - diff[1]
    an2 = p2[0] + diff[0], p2[1] + diff[1]
    while inside_constraints:
        an1_valid = False
        an2_valid = False
        if valid_anti_nodes(con, an1):
            nodes.append(an1)
            an1_valid = True
            p1 = an1
            an1 = p1[0] - diff[0], p1[1] - diff[1]
        if valid_anti_nodes(con, an2):
            nodes.append(an2)
            an2_valid = True
            p2 = an2
            an2 = p2[0] + diff[0], p2[1] + diff[1]
        if not an1_valid and not an2_valid:
            inside_constraints = False
    return nodes


def valid_anti_nodes(con, point):
    if point[0] < 0 or point[1] < 0:
        return False
    if point[0] >= a or point[1] >= a:
        return False
    else:
        print(f"{point} is valid in constraint of {con}")
        return True


grouped_nodes = {}
for node, value in freqs.items():
    grouped_nodes.setdefault(value, []).append(node)

pairs_by_group = {
    value: list(combinations(group, 2)) for value, group in grouped_nodes.items()
}


result = []
# Output the results
for value, pairs in pairs_by_group.items():
    print(f"Pairs for '{value}': {pairs}")
    # we need to add the nodes themselves if they are valid combinations.
    for pair in pairs:
        for i in pair:
            result.append(i)
        anx = calc_anti_nodes(pair[0], pair[1], a)
        for i in anx:
            result.append(i)

# remove duplicates
result_unique = list(set(result))

print(len(result_unique))
