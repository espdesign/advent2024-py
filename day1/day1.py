day_data: list = open("input", "r").read().split()

ll, rl = [], []


index = 0
for i in day_data:
    if index % 2 == 0:
        ll.append(i)
    else:
        rl.append(i)
    index += 1

ll.sort()
rl.sort()

result = []

for i in range(0, len(ll)):
    x = int(ll[i])
    y = int(rl[i])
    result.append(abs(x - y))

print(sum(result))
