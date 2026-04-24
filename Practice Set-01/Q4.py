# 4. Write a program that takes the length and breadth of a rectangle as input and prints its area
# and perimeter.
# Note: If the inputs are invalid, display an appropriate message.

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

if(l>0, b>0):
    perimeter = (l+b)/2.0
    area = l*b
else:
    print("Length and Breadth should be greater than zero")

print(perimeter)
print(area)