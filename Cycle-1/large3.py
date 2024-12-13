a=int(input("Enter the First Value:"))
b=int(input("Enter the Second Value:"))
c=int(input("enter the Third Value:"))
if a>b and a>c:
	print(f"{a} is largest")
elif b>a and b>c:
	print(f"{b} is largest")
else:
	print(f"{c} is largest")

