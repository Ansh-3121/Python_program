#Q Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest
# Formula:  SI = (P ∗ R ∗ T )/100
p=float(input("Enter principal amount :"))
r=float(input("Enter intrest rate :"))
t=float(input("Enter time period :"))
SI=(p*r*t)/100
Tamount=p+SI
print(f"Intrest on amount {SI}, and  total amount wit intrest {Tamount}")