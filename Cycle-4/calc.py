def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Division by zero is not possible\n")
    else:
        print(f"Quotient of the numbers {a} and {b} is {a / b}")

while True:
    print("\n1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5. EXIT")
    choice = int(input("Enter your choice: ")) 
    
    if choice == 5:
        print("EXIT")
        break
    
    if choice in [1, 2, 3, 4]:
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))
        
        if choice == 1:
            print(f"Sum is {add(num1, num2)}")
        elif choice == 2:
            print(f"Difference is {sub(num1, num2)}")
        elif choice == 3:
            print(f"Product is {mul(num1, num2)}")
        elif choice == 4:
            div(num1, num2)
    else:
        print("Invalid Choice!!")
