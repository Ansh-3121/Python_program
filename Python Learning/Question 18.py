#Break loop when codition match
n=int(input("Enter your Number:"))
i=1
while i<=10:
    if i%8==0:  # This logic means number multiply untill 8 matlab 8 tak multiply hoga uske baad loop break ho jayega 
        break
    print(i*n)
    i +=1
print("We outside of the loop :")    

