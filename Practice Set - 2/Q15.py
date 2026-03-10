# 15. Quadrant of point

x = int(input("x: "))
y = int(input("y: "))

if x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
else:
    print("On X-axis")