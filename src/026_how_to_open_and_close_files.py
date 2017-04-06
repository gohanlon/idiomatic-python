f = open('data/lorem_ipsum.txt')
try:
    data = f.read()
finally:
    f.close()

print(data)
