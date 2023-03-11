#The target of this exercise is to create two lists called x_list and y_list, 
#which contain 10 instances of the variables x and y, respectively. 
#You are also required to create a list called big_list, which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created.

# to declare variable x and y
x=object()
y=object()


x_list=[x] * 10
y_list=[y] * 10

big_list=x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list)) 



## This prints out "John is 23 years old."
name="John"
age=23
print("%s is %d years old"%(name, age))

#for list
list=[1,2,3]
print("A is : %s"%(list))

#Hello John Doe. Your current balance is $53.44.
data=("John","Doe",53.44)
str="Hello %s %s your current balance is$ %s"
print(str%data)

#to get the length of string
str="Welcome Home"
print(len(str))
