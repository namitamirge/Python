# to create function
def main():
    x = int(input("what is x?: "))
    print("Square of x is :", square(x))

def square(n):
   # return (n * n)  
   return (n ** 2)   # n raise to 3,4, 5 etc
    # return(pow(n,2))  #power of number

main() 


def hello(to="World"):
    print("hello,",to)

hello()
name=input("What is your name?").capitalize()
hello(name)




