names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melisa', 'judith', 'charlie']

d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

print(d)
