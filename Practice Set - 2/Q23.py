# 23. Divisibility of x by y and z

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x%y==0 and x%z==0:
    print("Divisible by both")
elif x%y==0:
    print("Divisible by y only")
elif x%z==0:
    print("Divisible by z only")
else:
    print("Not divisible")