from pprint import pp as pp
from itertools import combinations

debug = False
if debug:
    file_path = "example.input"
    ## ADD ANTINODE DATA
    file_path2 = "example-a.input"
    file2 = open(file_path2, "r")
    anti_node_data = file2.read().split("\n")
    file2.close()

    anti_node_data_puzzle_map = {}
    a = 0
    for row in anti_node_data:
        b = 0
        for character in row:
            anti_node_data_puzzle_map[(a, b)] = anti_node_data[a][b]
            b += 1
        a += 1

    for i in anti_node_data_puzzle_map:
        if anti_node_data_puzzle_map[i] == "#":
            print(i)
    pp(anti_node_data)

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


def calc_anti_nodes(p1, p2):
    diff = (p2[0] - p1[0], p2[1] - p1[1])
    an1 = p1[0] - diff[0], p1[1] - diff[1]
    an2 = p2[0] + diff[0], p2[1] + diff[1]
    return [an1, an2]


def valid_anti_nodes(con, point):
    print(f"Testing {point} is valid. with constraint {con}")
    if point[0] < 0 or point[1] < 0:
        return False
    if point[0] >= a or point[1] >= a:
        return False
    else:
        return True


grouped_nodes = {}
for node, value in freqs.items():
    grouped_nodes.setdefault(value, []).append(node)

pairs_by_group = {
    value: list(combinations(group, 2)) for value, group in grouped_nodes.items()
}


result = []
for value, pairs in pairs_by_group.items():
    print(f"Pairs for '{value}': {pairs}")
    for pair in pairs:
        anx = calc_anti_nodes(pair[0], pair[1])
        if valid_anti_nodes(a, anx[0]):
            result.append(anx[0])
        if valid_anti_nodes(a, anx[1]):
            result.append(anx[1])


result_unique = list(set(result))

print(len(result_unique))
### WORKING ANTINODE CALC
# p1 = (3, 7)
# p2 = (2, 5)

# diff = (p2[0] - p1[0], p2[1] - p1[1])
# print(p1[0] - diff[0], p1[1] - diff[1])
# print(p2[0] + diff[0], p2[1] + diff[1])
