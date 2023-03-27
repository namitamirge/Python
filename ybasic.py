#Ask for the name

name=input("What is your name?" )

#remove whitespaces from str and capitalize user's name
name=name.strip().title()

#used to capitalise first letter of every word in string
name=name.title()

#Split first and last name from string
first, last=name.split(" ")

#Capitalize first word user name
#name=name.capitalize()

# print with ??? as seperator

print("hello", name, sep="???")

print("hello, \"friend\"")  #\used to keep "" in output
print('hello, \"friend\"') 
print(f"hello, {first}")