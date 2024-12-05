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


incorrect_updates = []
for update in updates:
    for rule in order_rules:
        if rule[0] in update and rule[1] in update:
            rule0_index = update.index(rule[0])
            rule1_index = update.index(rule[1])
            if not rule0_index < rule1_index:
                incorrect_updates.append(update)
                break


def shift_by_rule(update, rule):
    # print(f"Shifting : {update} by : {rule}")
    index1 = update.index(rule[0])
    index2 = update.index(rule[1])
    value2 = update[index2]
    # print(f"removing value at index={index2} of update={update}")
    update.pop(index2)
    # print(f"update={update}")
    # print(f"inserting value={value2} at index={index1} of update={update}")
    update.insert((index1), value2)

    # print(f"returning new update={update}")
    return update


for update in incorrect_updates:
    changes_made = True
    while changes_made:
        changes_made = False
        for rule in order_rules:
            if rule[0] in update and rule[1] in update:
                rule0_index = update.index(rule[0])
                rule1_index = update.index(rule[1])
                if not rule0_index < rule1_index:
                    update = shift_by_rule(update, rule)
                    changes_made = True


for update in incorrect_updates:
    middle_index = len(update) // 2
    results += update[middle_index]

print(results)
