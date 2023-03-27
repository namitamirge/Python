#list program list of student in hogwart

students = ["Her", "Harry", "Ron"]  # list- set of multiple values
print(students[0])
# for loop ti iterate string
for student in students:    #no need to intialise student variable
    print(student)

for i in range(len(students)):
    print(i, students[i])


#dict- dictionary that allows you to associate with one key with  value {}
students={
    "Nil": "Villa", 
    "Nitin": "hownhome",
    "Mukesh": "hut",
}

#print(students["Nil"])

for student in students:
    print(student,students[student], sep=":")


#list of dictionary

students=[
    {"name": "Nil", "house": "Villa", "pet": "cat"},
    {"name": "Nitin", "house": "townhome", "pet": "dog"},
    {"name": "Mukesh", "house": "hut", "pet": "None"},    #None- absense of value
]

for student in students:
    print(student["name"], student["house"], student["pet"], sep=":")