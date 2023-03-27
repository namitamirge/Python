
    
while True:   
    try:

        x=int(input("What is value of x?:"))
    
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"Value of x is {x}")
