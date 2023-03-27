# program to print meaw using functions

def main():
    number = get_number()
    cat(number)

def get_number():
    while True:
        n = int(input("enter the number :"))
        if n > 0:
            break
    return n

def cat(n):

    for _ in range(n):
        print ("meow")


main()
