annual_sal=float(input("enter the salary"))
portion_saved=float(input("entert the amount you want to save every month :"))
total_cost=float(input("enter the total cost of the house:"))
semi_annual_raise=float(input("enter the raise of the employee for every six months"))

down_pay=0.25*total_cost

monthly_sal=annual_sal/12

net_savings=0
r=0.04
months=0

while net_savings<down_pay:
    net_savings+=net_savings*(r/12)
    net_savings+= monthly_sal*portion_saved
    months+=1
if months %6==0:
    monthly_sal+=monthly_sal*semi_annual_raise
print(f"the no.of for to achevie the dream house is {months}")