#definition of the class starts here
class Person:
    #defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    #defining class methods
    def showName(self):
        return self.name

    def showAge(self):
        return self.age

    #end of class definition

# defining another class
class Student: # Person is the
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId


class Resident(Person, Student): # extends both Person and Student class
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)
