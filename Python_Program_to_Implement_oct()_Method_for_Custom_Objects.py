class Person:
    age = 19

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print("The octal value is :", oct(person))
