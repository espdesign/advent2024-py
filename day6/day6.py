from pprint import pp as pp
from pprint import pformat as pformat
from copy import copy

debug = False
if debug:
    file_path = "example.input"
else:
    file_path = "input.input"
file = open(file_path, "r")
day_data = file.read().split()
file.close()


class Guard:
    """
    Guard Object to hold location and position
    """

    def __init__(self, location, facing):
        self.facing = facing
        self.bounds = copy(situation_map)
        self.out_of_bounds = False
        self.looping_x_times = False
        self.coords = location

    # def __repr__(self):
    # return f"Guard | {self.coords} | {self.facing}"

    def rotate_right(self):
        # Rotate the guard 90 degrees to the right
        if self.facing == "^":
            self.facing = ">"
        elif self.facing == ">":
            self.facing = "V"
        elif self.facing == "V":
            self.facing = "<"
        elif self.facing == "<":
            self.facing = "^"
        else:
            raise Exception("Error finding next rotation")

    def decide_next_move(self):
        next_move = self.coords[:]
        if self.facing == "^":
            # check upwards loc
            next_move[0] -= 1
        elif self.facing == "V":
            next_move[0] += 1
            # check downwards loc
        elif self.facing == ">":
            next_move[1] += 1
            # check right loc
        elif self.facing == "<":
            next_move[1] -= 1
            # check left loc
        else:
            raise Exception("Error deciding coords for next move")

        if tuple(next_move) not in situation_map.keys():
            print(f"OUT OF BOUNDS BREAK {next_move}")
            self.out_of_bounds = True
        else:
            if (
                situation_map[tuple(next_move)] == "#"
                or situation_map[tuple(next_move)] == "0"
            ):
                # print(f"{next_move} is hazard")
                if self.facing == "^":
                    # check upwards loc
                    next_move[0] += 1
                elif self.facing == "V":
                    next_move[0] -= 1
                    # check downwards loc
                elif self.facing == ">":
                    next_move[1] -= 1
                    # check right loc
                elif self.facing == "<":
                    next_move[1] += 1
                    # check left loc
                self.rotate_right()
                # print(previous_move)
            else:
                self.coords = next_move
                # print(f"Moving to{next_move}")
                self.bounds[tuple(next_move)] = "X"


situation_map = {}
a = 0
starting_location = [0, 0]
starting_facing = ""
for row in day_data:
    b = 0
    for character in row:
        # print(f"({a},{b}), {day_data[a][b]}")
        situation_map[(a, b)] = day_data[a][b]
        if character == "^" or character == ">" or character == "<" or character == "V":
            starting_location = [a, b]
            starting_facing = character
        b += 1
    a += 1

guard = Guard(starting_location, starting_facing)
while not guard.out_of_bounds:
    guard.decide_next_move()
result = 0
for i in guard.bounds.values():
    if i == "X":
        result += 1

print(result)
