def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

upper_limit = int(input("Enter the Upper Limit: "))
print("Sum of digits for each value in range: ")

for num in range(1, upper_limit + 1):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum <= 1:
        continue
    if is_prime(digit_sum):
        print(f"Number: {num}, Sum of Digits: {digit_sum}")

