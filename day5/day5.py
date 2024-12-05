file = open("input.input", "r")
day_data = file.read().split()
file.close()

order_rules = []
updates = []
results = 0

# Parse the input data, create two lists containing integer rules and updates
for data in day_data:
    if "|" in data:
        order_rules.append([int(i) for i in data.split("|")])
    else:
        updates.append([int(i) for i in data.split(",")])

# Search for relevant rules
for update in updates:
    print(f"Starting check with update: {update}")
    relevant_rules = []
    update_valid = True
    for rule in order_rules:
        # print(f"rule checking with - {rule}")
        if rule[0] in update and rule[1] in update:
            # print(f"VALID, Adding to relevant_rules")
            # relevant_rules.append(rule)
            rule0_index = update.index(rule[0])
            rule1_index = update.index(rule[1])
            if not rule0_index < rule1_index:
                update_valid = False

        else:
            pass

    if update_valid:
        middle_index = int((len(update) - 1) / 2)
        print(f"PASS-{update[middle_index]}")
        results += update[middle_index]
    else:
        print("FAIL-update not in order")

print(results)
