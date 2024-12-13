from graphic import rectangle
from graphic import circle
from graphic.three_d_graphic import cuboid
from graphic.three_d_graphic import sphere
l=int(input("Enter length of rectangle : "))
b=int(input("Enter breadth of rectangle : "))
rectangle.rectangle(l,b)
print()
r=int(input("Enter radius of circle : "))
circle.circle(r)
print()
l=int(input("Enter length of cuboid : "))
b=int(input("Enter breadth of cuboid : "))
h=int(input("Enter height of rectangle : "))
cuboid.cuboid(l,b,h)
print()
l=int(input("Enter radius of sphere : "))
sphere.sphere(r)

