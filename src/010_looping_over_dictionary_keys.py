dict = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}


# Loop over dictionary keys
for k in dict:
    print(k)

print()


# Delete some keys; best when dictionary is small because a new list off all the dictionary's keys is created
d = dict.copy()
for k in list(d.keys()):
    if k.startswith('r'):
        del d[k]

print(d)
print()


# Delete some keys; best when dict of remaining keys will be small since a new dictionary is created with only the retained keys
d = {k: dict[k] for k in dict if not k.startswith('r')}

print(d)
print()


# Note: This is my own addition -- it's not from the Raymond Hettinger talk
# Delete some keys; best when dict is or may be very large (the safest approach)
d = dict.copy()

remove = [k for k in d if k.startswith('r')]
for k in remove:
    del d[k]

print(d)
