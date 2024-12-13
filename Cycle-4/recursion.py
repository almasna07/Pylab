def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = 10
for i in range(num):
    print(fibonacci(i), end=" ")
print()


