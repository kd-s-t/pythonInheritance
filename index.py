import controllers.Inheritance as inheritance
import controllers.Multilevel_Inheritance as multilevel_inheritance
import controllers.Multiple_Inheritance as multiple_inheritance
import sys

first_var = sys.argv[1]

if first_var == 'inheritance':
    parts = inheritance.Body()
    print(parts.chest())
    print(parts.stomach())
    print(parts.eyes())
    print(parts.ears())
elif first_var == 'multilevel':
    g = multilevel_inheritance.GrandChild("Ken Dan", 18, "Cebu City")
    print(g.getName(), g.getAge(), g.getAddress())
elif first_var == 'multiple':
    resident = multiple_inheritance.Resident('Ken Dan', 18, '10305504')
    print("ID: ", resident.getId())
    print("Name: ", resident.showName())
    print("Age: ", resident.showAge())
else:
    print("Invalid value")
