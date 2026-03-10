# 17. Steel grading

h = int(input("Hardness: "))
c = float(input("Carbon: "))
t = int(input("Tensile strength: "))

cond1 = h > 50
cond2 = c < 0.7
cond3 = t > 5600

if cond1 and cond2 and cond3:
    print("Grade 10")
elif cond1 and cond2:
    print("Grade 9")
elif cond2 and cond3:
    print("Grade 8")
elif cond1 and cond3:
    print("Grade 7")
elif cond1 or cond2 or cond3:
    print("Grade 6")
else:
    print("Grade 5")