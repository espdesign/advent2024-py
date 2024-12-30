debug = False
if debug:
    file_path = "example.input"
else:
    file_path = "input.input"
example = open(file_path, "r")
diskmap = example.read()
example.close()

print(diskmap)


class PFile:
    def __init__(self, length: int, file_id: str):
        self.length = length
        self.file_id = file_id
        self.block = ""
        self.construct_block()

    def __repr__(self):
        return f"{self.block}"

    def construct_block(self):
        for i in range(0, self.length):
            self.block += f"{self.file_id} "


class Freespace:
    def __init__(self, length: int):
        self.length = length
        self.block = ""
        self.construct_block()

    def __repr__(self):
        return f"{self.block}"

    def construct_block(self):
        for i in range(0, self.length):
            self.block += ". "


class Diskmap:
    def __init__(self, disk_map):
        self.disk_objects = []

        file_id = 0
        files = []
        for file in disk_map[::2]:
            files.append(PFile(int(file), file_id))
            file_id += 1

        # free_space = ["." * int(j) for j in disk_map[1::2]]
        free_space = []
        for fp in disk_map[1::2]:
            free_space.append(Freespace(int(fp)))

        if len(free_space) < len(files):
            free_space.append(Freespace(0))

        for file, freespace in zip(files, free_space):
            self.disk_objects.append(file)
            self.disk_objects.append(freespace)


# test_free_space = Freespace(2)
# test_file = File(2, 3)
# print(test_file.block)
# print(test_free_space.block)


disk_test = Diskmap(diskmap)
# print("DISK IS THE FOLLOWING:")
# print(disk_test.disk_objects)

working_disk = []
for i in disk_test.disk_objects:
    for j in i.block.split(" "):
        if j:
            working_disk.append(j)
print(working_disk)


for i in range(1, len(working_disk)):
    x_stop = working_disk.count(".")
    # is the index i a empty space?
    # yes ->
    #       take last non empty space and pop it off, and change empty space to popped item
    # no -> check next index
    x = -1
    if working_disk[i] == ".":
        while True:
            if x == x_stop * -1 - 1:
                break
            if working_disk[x] == ".":
                x -= 1
            else:
                print(
                    f"changing index {i}({working_disk[i]}) to index {x}({working_disk[x]})"
                )

                working_disk[i] = working_disk[x]
                working_disk.pop(x)
                working_disk.append(".")
                # print(working_disk)
                break
    else:
        pass

# for i in working_disk:
#     if i == ".":
#         working_disk.pop(working_disk.index("."))
working_disk[:] = (value for value in working_disk if value != ".")
print("".join(working_disk))
print("0099811188827773336446555566..............")

result = 0
x = 0
for i in working_disk:
    result += int(i) * x
    x += 1
print(result)
