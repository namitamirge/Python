
def main():
    x = get_int("What's x?")
    print(f"Value of x is {x}")   

def get_int(prompt):   
    while True:   # loop for the user to input valid number
        try:

            x=int(input("prompt: "))
            #return int(input("prompt"))
        except ValueError:
            #print("x is not an integer")
            pass       #used for handling the errors
            
        else:
               return x    #return value and break
    
main()




