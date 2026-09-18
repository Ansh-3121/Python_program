# The user enters a string containing a number (e.g., "45"). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types

num=input("Enter a number : ")

a=float(num)
b=int(num)
c=str(num)

print(type(a),a)
print(type(b),b)
print(type(c),c)
