def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

x = int(input())

for i in range(x):
    print(fibonacci(x))