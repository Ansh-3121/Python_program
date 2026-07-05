# Madels for rankers
rank=int(input("Enter your rank:"))

match rank:
    case 1:
        print("You are gold madelist")
    case 2:
        print("You are silver madelist")
    case 3:
        print("You are win prizes")
    case _:
        print("You are not under in prize")
