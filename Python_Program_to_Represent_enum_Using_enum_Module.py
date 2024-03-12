from enum import Enum

class Subject(Enum):
    MATHS = 1
    SCIENCE = 2
    ENGLISH = 3

# print the enum member
print(Subject.MATHS)

# get the name of the enum member
print(Subject.MATHS.name)

# get the value of the enum member
print(Subject.MATHS.value)
