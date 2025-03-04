students = [

        {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
        {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag" },
        {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel Terrier" },
        {"name" : "Draco", "house" : "Slytherin", "patronus" : None},
]

for student in students :
    print(student["name"], student["house"], student["patronus"], sep=" => ")

"""
Fourth version, now with dictionaries
students = {
    "Hermione":"Gryffindor", 
    "Harry":"Gryffindor", 
    "Ron":"Gryffindor", 
    "Draco":"Slytherin",
    }

for student in students :
    print(student, students[student], sep=" => ")
"""

"""
Third version :
students = ["Hermione", "Harry", "Ron"]

for _ in range(len(students)) :
    print(_ + 1, students[_])
"""

"""
My example :

students = ["Hermione", "Harry", "Ron"]
number = len(students)


for _ in range(number) :
    print(students[_])
"""

"""
Second example :

students = ["Hermione","Harry","Ron"]
for student in students:
    print(student)
"""

"""
First example :

students = ["Hermione","Harry","Ron"]

print(students[0])
print(students[1])
print(students[2])
"""