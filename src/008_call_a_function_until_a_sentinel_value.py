from functools import partial

f = open('data/lorem_ipsum.txt')

blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

print(blocks)
