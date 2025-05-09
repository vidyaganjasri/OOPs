'''
multilevel inheritance, where each class builds upon the previous one. Here's a brief explanation:

🧩 Breakdown of the Example:
Person Class:
This is the base class that defines the basic attributes name and age, and has a method Intro() to introduce a person.

Student Class:
This is derived from Person and adds the stu_id (student ID). It uses the super() function to call the Intro() method from the Person class, 
then adds its own Intro_st() method to introduce the student's ID.

GradStu Class:
This class is derived from Student. It adds a new attribute deg (degree) and has the method Intro_grad() to introduce the graduate student. 
It calls the Intro_st() method from Student using super() to get the student's details and then introduces the degree.

🧐 Key Points:
Multilevel inheritance is where a class inherits from another class, which itself is derived from a base class.

You’re extending functionality at each level: Person → Student → GradStu.

Using super() allows you to reuse functionality from the parent class without repeating code.

👏 Why It’s Good:
Code Reusability: You avoid repeating code in each class (e.g., introducing the name and age).

Organized Structure: Each class has a clear responsibility (basic person details, student details, grad student details).

Easily Extensible: You can easily add more specialized classes like PostGradStudent or DoctorateStudent by further extending the GradStu class.'''
class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def Intro(self):
        print(f"Hi I'm {self.name} and I'm {self.age} year's old")

class Student(Person):
    def __init__(self,name,age,stu_id):
        super().__init__(name,age)
        self.stu_id = stu_id 
        
    def Intro_st(self):
        super().Intro()
        print(f"My student id is {self.stu_id}")
    
class GradStu(Student):
    def __init__(self,name,age,stu_id,deg):
        super().__init__(name,age,stu_id)
        self.deg = deg 

    def Intro_grad(self):
        super().Intro_st()
        print(f"I'm pursuing {self.deg}")
g1 = GradStu("vihan",22,147,"BE")
g1.Intro_grad()
