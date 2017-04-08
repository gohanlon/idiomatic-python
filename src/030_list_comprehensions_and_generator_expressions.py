# Comprehension: a list is created in memory
print(sum([i**2 for i in range(10)]))

# Geneartor: only iterables are created; no list is created in memory
print(sum(i**2 for i in range(10)))
