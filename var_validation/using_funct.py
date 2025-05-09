class Person:
    def __init__(self, age):
        self.set_age(age)

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    def get_age(self):
        return self._age

p = Person(25)
print(p.get_age())  # Access using a method
p.set_age(30)       # Set using a method
try:
    p.set_age(-5)
except ValueError as e:
    print(f"{e}")
