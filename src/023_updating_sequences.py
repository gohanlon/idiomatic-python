from collections import deque

names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])
print(names)

del names[0]
names.popleft()
names.appendleft('mark')

print(names)
