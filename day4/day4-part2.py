# Input
day_data: list = open("input.input", "r").read().split("\n")

PAIR_1 = [(-1, -1), (+1, +1)]
PAIR_2 = [(-1, +1), (+1, -1)]

# Processing
coordinates = {}
coordinates_of_a = {}
a = 0
for row in day_data:
    b = 0
    for character in row:
        coordinates[(a, b)] = day_data[a][b]
        if character == "A":
            coordinates_of_a[(a, b)] = day_data[a][b]
        b += 1
    a += 1

result = 0

for a_b in coordinates_of_a:
    a, b = a_b[0], a_b[1]
    print(f"A({a},{b})")
    pair1_is_valid = False
    pair2_is_valid = False
    try:
        if a == 0 or b == 0:
            raise IndexError
        if day_data[a + PAIR_1[0][0]][b + PAIR_1[0][1]] == "M":
            if day_data[a + PAIR_1[1][0]][b + PAIR_1[1][1]] == "S":
                print(f"{day_data[a + PAIR_1[0][0]][b + PAIR_1[0][1]]} - valid")
                print("valid")
                pair1_is_valid = True
        elif day_data[a + PAIR_1[0][0]][b + PAIR_1[0][1]] == "S":
            if day_data[a + PAIR_1[1][0]][b + PAIR_1[1][1]] == "M":
                print(f"{day_data[a + PAIR_1[0][0]][b + PAIR_1[0][1]]} - valid")
                print("valid")
                pair1_is_valid = True
        else:
            print("else not valid")

        if pair1_is_valid:
            if day_data[a + PAIR_2[0][0]][b + PAIR_2[0][1]] == "M":
                if day_data[a + PAIR_2[1][0]][b + PAIR_2[1][1]] == "S":
                    print(f"{day_data[a + PAIR_2[0][0]][b + PAIR_2[0][1]]} - valid")
                    print("valid")
                    pair2_is_valid = True
            elif day_data[a + PAIR_2[0][0]][b + PAIR_2[0][1]] == "S":
                if day_data[a + PAIR_2[1][0]][b + PAIR_2[1][1]] == "M":
                    print(f"{day_data[a + PAIR_2[0][0]][b + PAIR_2[0][1]]} - valid")
                    print("valid")
                    pair2_is_valid = True
            else:
                print("else not valid")
    except IndexError:
        print("out of range")
    if pair1_is_valid and pair2_is_valid:
        result += 1


# Output
print(result)
