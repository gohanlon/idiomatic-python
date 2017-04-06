def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        t = y
        x, y = y, x+y

fibonacci(10)
