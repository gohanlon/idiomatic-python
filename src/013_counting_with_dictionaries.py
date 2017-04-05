from collections import defaultdict

colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = defaultdict(int)
for color in colors:
    d[color] += 1

print(d)
