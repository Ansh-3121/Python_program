age=int(input("Enter your age "))
if age>18:
    country=input("Enter your contry ")
    if country=="india":
        print
        state=input("Enter you state ")
        if state=="uttar pradesh":
            print
            district=input("Enter your district ")
            if district=="jaunpur":
                print("Your form is sunbmited")
            else:
                print("Wrong info")
        else:
            print("Wrong info")
    else:
        print("Wrong info")
else:
    print("you are out of bellow conditions")                        
                           
                 
