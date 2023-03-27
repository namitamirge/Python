#function for even and odd
def main():
    x = int(input("Enter value for x: "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):
     return n % 2 == 0
     #return True if n % 2 == 0 else False


main()
