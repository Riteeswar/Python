# Write a program that takes as input n1 o1 n2 o2 n3 where n1, n2, n3 are natural numbers and o1, o2 are operaters. The
# program should use nested if-else-if so as to handle the expresion which can have o1 and o2 from any of the operators
# in {+,-,*}

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
o1 = input("Enter first operator(+,-,*): ")
o2 = input("Enter second operator(+,-,*): ")

if(o1 == "+"):
    if(o2 == "+"):
        print(f"Answer = {n1 + n2 + n3}")
    elif(o2 == "-"):
        print(f"Answer = {n1 + n2 - n3}")
    elif (o2 == "*"):
        print(f"Answer = {(n1 + n2) * n3}")
    else:
        print("second operator is invalid")
elif(o1 == "-"):
    if(o2 == "+"):
        print(f"Answer = {(n1 - n2) + n3}")
    elif(o2 == "-"):
        print(f"Answer = {(n1 - n2) - n3}")
    elif(o2 == "*"):
        print(f"Answer = {(n1 - n2) * n3}")
    else:
        print("second operator is invalid")
elif(o1 == "*"):
    if (o2 == "+"):
        print(f"Answer = {(n1 * n2) + n3}")
    elif (o2 == "-"):
        print(f"Answer = {(n1 * n2) - n3}")
    elif (o2 == "*"):
        print(f"Answer = {(n1 * n2) * n3}")
    else:
        print("second operator is invalid")
else:
    print("First operator is invalid")