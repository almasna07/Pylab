n = int(input("Enter the number : "))
temp = n
digits = 0
while temp > 0:
        temp = temp // 10
        digits = digits + 1
temp = n
arm = 0
while temp > 0:
        arm = arm +  (temp % 10) ** digits 
        temp  = temp // 10
if arm == n:
        print("Armstrong number")
else:
        print("Not an armstrong number")
