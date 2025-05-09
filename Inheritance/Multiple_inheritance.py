'''Multiple inheritance is a feature in object-oriented programming (OOP) where a class can 
inherit properties and methods from more than one parent class.

Imagine you're building a University Management System where there are different types of roles, 
like Person, Employee, and Professor. 
Each of these roles has distinct attributes, but they also share some common attributes.

The Person class might contain basic personal information, such as name and age.

The Employee class could contain employment details, such as employee ID and department.

The Professor class needs both personal information and employment details. 
Rather than writing the same code for name, age, employee_id, and department all over again, 
you can inherit from both Person and Employee classes.'''
class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def Introduce(self):
        print(f"Hi I'm {self.name} and I'm {self.age} year's old")

class Employer():
    def __init__(self,emp_id):
        self.emp_id = emp_id
    
    def Introduce(self):
        print(f"My emp id is {self.emp_id}")

class Manager(Person,Employer):
    def __init__(self,name,age,emp_id,pos):
        Person.__init__(self,name,age)
        Employer.__init__(self,emp_id)
        self.pos = pos 
    def Introduce(self):
        Person.Introduce(self)
        Employer.Introduce(self)
        print(f"Im holding a position of {self.pos}")
    
man1 = Manager("miha",24,147,"HR")
man1.Introduce()
    
