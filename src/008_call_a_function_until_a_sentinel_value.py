f = open('data/lorem_ipsum.txt')

blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

print(blocks)
