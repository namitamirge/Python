# match
name=input("What's your name? ")
match name:
    case "Harry"| "Barry" | "Mike":
        print("Grayffinder")
    case "Darco":
        print("Dhome")
    case _:
        print("Who?")