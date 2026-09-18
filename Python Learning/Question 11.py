
#Q11 Creat student result  markheet  Add The student total marks and percentage
rn=int(input("Enter Your Roll nu :"))
name=input("Enter Your name :")
age=int(input("Enter Your age:"))
phy=float(input("Enter Marks of physics:"))
chem=float(input("Enter Marks of Chemistry:"))
maths=float(input("Enter Marks of Math:"))
Hin=float(input("Enter Marks of Hindi:"))
eng=float(input("Enter Marks of english:"))

# Total of all subject 
a=phy+chem+maths+Hin+eng

# Percentage of given marks
percent=a/5
print(f"Total marks {a} and percent {percent}")

