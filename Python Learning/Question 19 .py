#use continue to skip numbers
i=1
while i<=100:
    if i%3==0: # This logic apply for skip all multiple of 3
        i +=1 
        continue # Countinue use for skip the number whose match a specific condition
    print(i)
    i +=1       
print("We are outsiding of loop:")