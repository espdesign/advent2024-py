import math
import itertools


debug = False
if debug:
    file_path = "example.input"
else:
    file_path = "input.input"
file = open(file_path, "r")
day_data = file.read().split("\n")
file.close()

# Elephant Operators Available
EO = ("*", "+")


def perform_operation(a, b, operator):
    if operator == "*":
        return a * b
    elif operator == "+":
        return a + b


def define_permutation_formula(perm, numbers):
    formula = []
    for i, p in zip(numbers, perm):
        formula.append(i)
        formula.append(p)
    formula.append(numbers[-1])
    return formula


class Equation:
    def __init__(self, data):
        self.data = data
        self.test_value = int(data[0])
        self.numbers = data[1]
        self.formula = self.create_formula()
        self.valid = False
        # Check and rule out single operator use
        self.same_operators_only()
        if not self.valid:
            print(f"{self.test_value}:{self.formula} not valid, cont testing..")
            self.check_permutations()

    def check_permutations(self):
        # create list of possible operators
        available_operators = ["*", "+", "||"]
        operator_placeholder_total = self.formula.count("?")
        # print(f"operator placeholders = {operator_placeholder_total}")
        # prmu = list(itertools.product(a, repeat=b))[1:-1]
        products = list(
            itertools.product(available_operators, repeat=operator_placeholder_total)
        )[1:-1]
        # print(f"total permutations remaining to check: {len(products)}")
        for product in products:
            new_formula = define_permutation_formula(product, self.numbers)
            # print(new_formula)
            answer = new_formula[0]
            for i in range(1, len(new_formula) - 1, 2):
                operator = new_formula[i]
                operand = new_formula[i + 1]
                if operator == "+":
                    answer += operand
                if operator == "*":
                    answer *= operand
                if operator == "||":
                    x = str(answer) + str(operand)
                    answer = int(x)
            # print(answer, self.test_value)
            if answer == self.test_value:
                self.valid = True

    def create_formula(self):
        """Create a formula with missing operators

        Returns:
            list: numbers and missing operators in correct order
        """
        formula = []
        s = 0
        e = len(self.numbers) - 1
        for number in self.numbers:
            formula.append(number)
            if s < e:
                formula.append("?")
            s += 1
        return formula

    def same_operators_only(self):
        if sum(self.numbers) == self.test_value:
            self.valid = True
        if math.prod(self.numbers) == self.test_value:
            self.valid = True
        concat_all = ""
        for i in self.numbers:
            concat_all += str(i)
        if int(concat_all) == self.test_value:
            self.valid = True

    def __repr__(self):
        return f"({self.test_value}):{self.numbers}"


# format day_data
d = []
for line in day_data:
    line = line.split(":")
    x = line[0]
    y = [int(line) for line in line[1].split()]
    equation = [x, y]
    d.append(equation)

# build class objects from equations
result = 0
equations = []
for case in d:
    equation = Equation(case)
    equations.append(equation)

    print(f"{equation.test_value}{equation.formula}{equation.valid}")
    if equation.valid:
        result += equation.test_value
print(result)
