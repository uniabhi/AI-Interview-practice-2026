# from collections import Counter

# counts = Counter()

# with open("app.log", "r") as file:
#     for line in file:
#         level = line.split()[0]
#         counts[level] += 1

# for level, count in counts.items():
#     print(level, count)

from collections import Counter

counts = {}

with open("app.log", "r") as file:
    for line in file:
        level = line.split()[0]
        counts[level] = counts.get(level, 0) +1

print(counts)
