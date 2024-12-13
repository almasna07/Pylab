number = input("Enter a number: ")
length = len(number)
is_palindrome = True
for i in range(length // 2):
    if number[i] != number[length - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print(f"{number} is a Palindrome")
else:
    print(f"{number} is not a Palindrome")


