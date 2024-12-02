day_data: list = open("input", "r").read()

# REPORT SAFE RULES
# RULE1   The levels are either all increasing or all decreasing.
# RULE2   Any two adjacent levels differ by at least one and at most three.


class Report:
    def __init__(self, report):
        self.safe = True
        self.report = [int(i) for i in report.split()]
        self.diff = [
            abs(self.report[i] - self.report[i - 1]) for i in range(1, len(self.report))
        ]
        self.fails = []
        # Safe by default
        for i in self.diff:
            if i > 3 or i == 0:
                self.fails.append("Rule2 Fail")
                self.safe = False
                break

        self.increasing = all(i < j for i, j in zip(self.report, self.report[1:]))
        self.decreasing = all(i > j for i, j in zip(self.report, self.report[1:]))
        if self.increasing or self.decreasing is True:
            pass
        else:
            self.fails.append("Rule1 Fail")
            self.safe = False


reports = [Report(report) for report in day_data.split("\n")]

results = 0
for report in reports:
    if report.safe:
        results += 1
    print(report.safe, report.report, report.diff, report.fails)
print(results)
