# this program say hello and ask for my name and age and print name and age
print("Hello, What is your name?") # ask for the name

name=input()

print("Hi %s" %name)
print("the length of your name is")
print(len(name))


print("How old are you %s ?" %name)
age=input()
print("Thanks " +name)
print("You will be " + str(int(age)+1) +" in one year")  # to print the next year age 


    