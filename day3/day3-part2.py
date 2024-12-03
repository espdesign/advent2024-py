import re

# Input
day_data: list = open("input.input", "r").read()

# Processing
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, day_data)

results = 0
is_mul_on = True

for item in matches:
    if item == "do()":
        is_mul_on = True
    elif item == "don't()":
        is_mul_on = False
    else:
        if is_mul_on:
            item = [int(i) for i in item[4:-1].split(",")]
            results += item[0] * item[1]
# Output
print(results)
