day_data: list = open("input.input", "r").read()


# REPORT SAFE RULES
# RULE1   The levels are either all increasing or all decreasing.
def is_increasing(levels):
    results = all(i < j for i, j in zip(levels, levels[1:]))
    return results


def is_decreasing(levels):
    results = all(i > j for i, j in zip(levels, levels[1:]))
    return results


def is_ordered(levels):
    if is_decreasing(levels) or is_increasing(levels) is True:
        return True
    else:
        return False


# RULE2   Any two adjacent levels differ by at least one and at most three.
def is_diff_safe(levels):
    diff_levels = [abs(levels[i] - levels[i - 1]) for i in range(1, len(levels))]
    for i in diff_levels:
        if i > 3 or i == 0:
            return False
    return True


def problem_damper(levels):
    damper_levels = []
    for i in range(0, len(levels)):
        damper_levels.append(levels[:i] + levels[i + 1 :])
    for i_levels in damper_levels:
        if is_ordered(i_levels) and is_diff_safe(i_levels):
            return True
    return False


class Report:
    def __init__(self, report):
        # Safe by default
        self.safe = True

        self.report = [int(i) for i in report.split()]
        self.fails = []
        self.ordered = is_ordered(self.report)
        if not is_diff_safe(self.report):
            self.fails.append("fail-r2")
            self.safe = False
        if not self.ordered:
            self.fails.append("fail-r1")
            self.safe = False
        if not self.safe:
            self.safe = problem_damper(self.report)


reports = [Report(report) for report in day_data.split("\n")]

results = 0
for report in reports:
    if report.safe:
        results += 1

print(results)
