#Q10 Take a decimal number as input (like ,45.78 ) and output its:
#integer part 45
#fractional part .78
num=(input("Enter a number : "))
num=num.split(".")
print("Integer part:", num[0])
print("Decimal part:", num[1])

