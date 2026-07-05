# In this program have write condtion code if 1st condition true then execute second condition otherwoist not
password=int(input("Enter your password"))
if password==3121:
    print("go")
    id=int(input("enter your id "))
    if id==78:
        print("correct your id")
        code=input("enter your code ")
        if code=="ansh":
            print("Welcome to office")
        else:
            print("Out office area")    
    else:
        print("Wrong id")        
else:
    print("Dont go")
            
        
