# 12. Rectangle area and perimeter

l = float(input("Length: "))
b = float(input("Breadth: "))

area = l * b
perimeter = 2 * (l + b)

print("Area =", area)
print("Perimeter =", perimeter)

if area > perimeter:
    print("Area greater than perimeter")
else:
    print("Perimeter greater or equal")