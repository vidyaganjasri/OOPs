'''We define a Person class, and the Student class inherits from it. 
Since the Student class requires the same attributes as the Person class, 
we leverage inheritance to reuse those attributes. 
For actions, such as introducing the person, we use the super() function to 
call and refer to the parent class’s methods.'''
class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def introduce(self):
        print()
        print(f"Hi I'm {self.name} and I'm {self.age} year's old")

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id 
    def introduce(self):
        super().introduce()
        print(f"I'm currently a student bearing a roll numbers {self.student_id}")

stu1 = Student("yara",21,147)
stu1.introduce()

stu1 = Student("Viha",25,143)
stu1.introduce()

per1 = Person("Taanya",22)
per1.introduce()
