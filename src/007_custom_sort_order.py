colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

# Breaks on Python 3 because comparator functions are replaced with key functions
#print(sorted(colors, cmp=compare_length))
