import re

# Input
day_data: list = open("input.input", "r").read()

# Processing
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, day_data)

numbers = [(int(num1) * int(num2)) for num1, num2 in matches]

# Output
result = sum(numbers)
print(result)
