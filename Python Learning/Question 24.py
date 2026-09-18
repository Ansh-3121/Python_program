# Print sum of first 'N' natural numbers
n=int(input("Enter your last number :"))
sum=0
for i in range(1,n+1): #isme ssabhi number ek doosre se aad honge jo number denge
        sum +=i         #Example 10 to 1+2+3+4+5+6+7+8+9+10=55 we can use formula= n(n+1)/2
print( "sum of all number is =",sum)    