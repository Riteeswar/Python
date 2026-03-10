# 13. Check if points lie on straight line

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1):
    print("Points lie on straight line")
else:
    print("Points do not lie on straight line")