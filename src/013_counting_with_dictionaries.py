colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
    d[color] += 1

print(d)
