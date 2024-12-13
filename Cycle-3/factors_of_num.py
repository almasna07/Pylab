number = int(input("Enter a number to find its Factors: "))
factor = 1
print(f"Factors of {number} are:")
while factor <= number:
    if number % factor == 0:
        print(factor)
    factor += 1

