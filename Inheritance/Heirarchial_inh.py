'''Hierarchical Inheritance means:
Multiple derived (child) classes inherit from the same base (parent) class.

In your example:
Student and Teacher both inherit from Person'''
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def Introduce(self):
        print(f"Hi I'm {self.name} and I'm {self.age} year's old")

class Student(Person):
    def __init__(self,name,age,stu_id):
        super().__init__(name,age)
        self.id = stu_id
    def Introduce(self):
        super().Introduce()
        print(f"My Student id is {self.id}")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.sub = subject
    def Introduce(self):
        super().Introduce()
        print(f"I'm a {self.sub} Teacher")

'''
per1 = Person("vidya",24)
per1.Introduce()
print()'''

stu1 = Student("viah",52,147)
stu1.Introduce()
print()

Teah1 = Teacher("Tara",14,"Maths")
Teah1.Introduce()
