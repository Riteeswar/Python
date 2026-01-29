# 1. Write a program that takes the radius of a circle as input and computes its area.
# Note: If the radius is non-negative, display an appropriate message.

r = float(input("Enter radius: "))
area = (3.14)*(r*r)

if(r>0):
    print("Area of circle: ", area)
else:
    print("Radius should be greater than zero")