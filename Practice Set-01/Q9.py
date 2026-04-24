# 9. Write a program that takes the marks for 5 subjects as input and calculates the total and
# average marks.

sub1 = float(input("Enter first subject marks: "))
sub2 = float(input("Enter second subject marks: "))
sub3 = float(input("Enter third subject marks: "))
sub4 = float(input("Enter fourth subject marks: "))
sub5 = float(input("Enter fifth subject marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total/5
print(f"Total = {total}")
print(f"Average = {average}")