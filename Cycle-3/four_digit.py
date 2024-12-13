import math

def even_perfect_squares(start, end):
    result = []
    for num in range(start, end):
        if 1000 <= num <= 9999 and num % 2 == 0:
            root = int(math.sqrt(num))
            if root * root == num:
                digits = str(num)
                if all(int(digit) % 2 == 0 for digit in digits):
                    result.append(num) 
    return result

start_range = int(input("Enter start range: "))
end_range = int(input("Enter end range: "))
print(f"Four digit even perfect squares: {even_perfect_squares(start_range, end_range)}")

