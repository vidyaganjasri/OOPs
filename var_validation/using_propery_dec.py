class Person:
    def __init__(self,age):
        self.age = age#this is more or less acting like a function age.setter which validates it 
    
    @property
    def age(self):
        return self._age#this simply returns the age without calling a functoin just do obj.age
    
    @age.setter
    def age(self,val):
        if val<0:
            raise ValueError("Invlalid age")
        self._age = val#we have self._age  instead of self.age it will fall nito infinit loop as it would recursively keep on calling the setter function 

per = Person(34)
print(per.age)
per.age = 64
print(per.age)
try:
    per.age = -3
except ValueError as e:
    print(f"{e}")


'''
34
64
Invlalid age'''
