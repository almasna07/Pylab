import math
a=int(input("Enter the First Number"))
b=int(input("Enter the Second Number"))
c=int(input("Enter the Third Number"))
d=(b**2)-(4*a*c)
if d>0:
	print("The Roots are real and different\n")
	ans1=(-b-math.sqrt(d))/(2*a)
	ans2=(-b+math.sqrt(d))/(2*a)
	print(f"The roots are {ans1} and {ans2}")
elif d==0:
	print("The Roots are Real and equal \n")
	ans3=-b/(2*a)
	print(f"The root is {ans3}")
else:
	real=-b/(2*a)
	imaginary=math.sqrt(abs(d))/(2*a)
	print(f"The Roots are complex:{real}+{imaginary}i")
