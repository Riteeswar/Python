h = float(input("Enter the hardness(must be greater than 50): "))
cc = float(input("Enter the carbon content(must be less than 0.7): "))
ts = float(input("Enter the tensile strength(must be greater than 5600): "))

if(h>50 and cc<0.7 and ts>5600):
    print("Grade is 10")
elif(h>50 and cc<0.7 and ts<5600):
    print("Grade is 9")
elif(h<50 and cc<0.7 and ts>5600):
    print("Grade is 8")
elif(h>50 and cc>0.7 and ts>5600):
    print("Grade is 7")
elif((h>50 and cc>0.7 and ts<5600) or (h<50 and cc<0.7 and ts<5600) or (h<50 and cc>0.7 and ts>5600)):
    print("Grade is 6")
else:
    print("Grade is 5")