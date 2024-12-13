square=lambda side:side*side
rectangle=lambda l,b:l*b
triangle=lambda base,height:0.5*base*height
print("\n***AREA OF SQUARE***")
side=float(input("Enter The Side of Square:"))
print(f"Area is {square(side)}")
print("\n***AREA OF RECTANGLE***")
l=float(input("Enter The Length:"))
b=float(input("Enter The Breadth:"))
print(f"Area is {rectangle(l,b)}")
print("\n***AREA OF TRIANGLE***")
base=float(input("Enter The Base:"))
height=float(input("Enter the Height:"))
print(f"Area is {triangle(base,height)}")


