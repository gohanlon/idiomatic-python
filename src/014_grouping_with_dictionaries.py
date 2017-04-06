from collections import defaultdict

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melisa', 'judith', 'charlie']

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

print(d)
