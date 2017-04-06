import random

def influence(x, y, dx, dy, partial=None):
    if partial == 'x':
        return dx / 2
    elif partial == 'y':
        return dy / 2

    return None

x, y, dx, dy = random.sample(range(1, 100), 4)
t = 1

print('Before:', x, y, dx, dy)

x, y, dx, dy = (x + dx * t,
        y + dy * t,
        influence(x, y, dx, dy, partial='x'),
        influence(x, y, dx, dy, partial='y'))

print('After:', x, y, dx, dy)
