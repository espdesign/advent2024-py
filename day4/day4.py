# Input
day_data: list = open("input.input", "r").read().split("\n")

WORDSEARCH = [
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, -1),
    (0, +1),
    (+1, -1),
    (+1, 0),
    (+1, +1),
]
# Processing
# create a dict containing the coordinates of each value, and one that has the x_coords
coordinates = {}
coordinates_of_x = {}
valid_coords = []
a = 0
for row in day_data:
    b = 0
    for character in row:
        # print(f"({a},{b}), {day_data[a][b]}")
        coordinates[(a, b)] = day_data[a][b]
        if character == "X":
            coordinates_of_x[(a, b)] = day_data[a][b]
        b += 1
    a += 1
# print(f"dict {coordinates[3, 3]}")
# look at each neighboring point
result = 0

for a_b in coordinates_of_x:
    a, b = a_b[0], a_b[1]
    print(f"X({a},{b})")
    # check each point next to it using WORDSEARCH values
    for tup in WORDSEARCH:
        try:
            x = a + tup[0]
            y = b + tup[1]
            point = day_data[x][y]
            print(f"checking for m at {x,y}")
            if point == "M":
                # print("valid")
                if (a + (tup[0] * 2)) < 0 or (b + (tup[1]) * 2) < 0:
                    raise IndexError
                point2 = day_data[(a + (tup[0] * 2))][(b + (tup[1]) * 2)]
                print(f"checking for A at {(a + (tup[0] * 2)),(b + (tup[1]) * 2)}")
                if point2 == "A":
                    # print("valid")
                    if (a + (tup[0] * 3)) < 0 or (b + (tup[1]) * 3) < 0:
                        raise IndexError
                    point3 = day_data[(a + (tup[0] * 3))][(b + (tup[1]) * 3)]
                    print(f"checking for S at {(a + (tup[0] * 3)),(b + (tup[1]) * 3)}")
                    if point3 == "S":
                        print("~ complete XMAS +1")
                        result += 1
                        valid_coords.append(f"({a},{b}),{point},{point2},{point3}")
                    else:
                        print("invalid S")
                else:
                    print("invalid A")
            else:
                print("invalid M")

        except IndexError:
            print("out of range")
# if it is an M continue in the direction to look for a and s
# if it is a complete XMAS +1 to total result


# Output

print(result)
