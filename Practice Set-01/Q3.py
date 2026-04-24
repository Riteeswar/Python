# 3. Write a simple calculator program. It should be able to add, subtract, multiply, and divide
# any two numbers input by the user.
# Note: The user will also specify the operation to perform.

print("Welcome to Calculator")
a = int(input("Enter a integer: "))
b = int(input("Enter other integer: "))
o = input("Enter the operation to be performed(+,-,*,/): ")
if(o == "+"):
    print(a+b)
elif(o == "-"):
    if(a>b):
        print("Difference: ",a-b)
    else:
        print("Difference: ",b-a)
elif(o == "*"):
    print(a*b)
elif(o == "/"):
    if(a>b):
        print("Quotient: ",a/b)
    else:
        print("Quotient: ",b/a)
else:
    print("Enter a valid operation")