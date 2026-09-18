#Q14 Write a function that takes two integers a and b, and prints all even numbers between them (inclusive)
a=int(input("Enter startin number: "))
b=int(input("Enter last number: "))
for num in range(a,b+1):
    if num %2 ==0:
        print(num)