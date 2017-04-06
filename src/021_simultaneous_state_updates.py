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

tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(x, y, dx, dy, partial='x')
tmp_dy = influence(x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

print('After:', x, y, dx, dy)
