#Mario

#def main():
 #   print_row(4)


#def print_row(width):
#    print("?" * width)

#main()


def main():
    print_square(3)

def print_square(size):

    # for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print("#", end="")

        print()         #for printing new line after done with loop

main()






def main():
    print_square(3)

def print_square(size):

    
    for i in range(size):       
        #print("#" * size)   
            print_row(size)

def print_row(width):
    print("#" * width)

main()




