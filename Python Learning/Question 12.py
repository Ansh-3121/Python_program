#Q12 Write a program that takes Salary  as input. Using conditional statements,calculate the final tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary=float(input("Enter your Salary amount: "))
if salary<30000:
    tax=salary*5/100
    print(" 5% Tax on your total salary amount",tax)
elif salary>=30000 and salary<=70000:
    tax=salary*15/100 
    print("15% Tax on your total salary amount",tax)
else:
    tax=salary*25/100
    print("25% Tax on your total salary amount",tax)      

