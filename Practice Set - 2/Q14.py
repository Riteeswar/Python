# 14. Point inside / outside circle

cx =     int(input("Center x: "))
cy = int(input("Center y: "))
r = int(input("Radius: "))

px = int(input("Point x: "))
py = int(input("Point y: "))

d = (px-cx)**2 + (py-cy)**2

if d < r*r:
    print("Inside circle")
elif d == r*r:
    print("On circle")
else:
    print("Outside circle")