What is OOP?
OOP stands for Object-Oriented Programming. 
It is a programming model supported by many modern languages like Java, Python, C++, and more.

🔹 Why was OOP introduced?
Initially, programming was done using procedural languages like C. 
These languages followed a top-down approach like main task is divided into sub task which only works for small data, or when dealing with less number of entities, 
which made it difficult to manage large and complex applications.

For example, in an app like WhatsApp, handling millions of users using only procedural programming would mean:
Repeating the same code for each user
Having an unstructured layout
Difficulty in making updates or scaling

🔴 Problem: You’d need to manually write separate logic for each user, making the code hard to maintain and inefficient.

✅ How OOP solves this
OOP introduces the idea of classes and objects.
You can define a class once (a template).
Then create multiple objects (users) from that class.
This avoids code duplication and improves clarity.

It also brings in powerful features:
Inheritance – reuse code from one class to another
Abstraction – hide complex details and show only what’s needed
Polymorphism – use one interface for multiple behaviors
Encapsulation – wrap data and methods into a single unit and protect it

🧠 Key Concepts in OOP:
Term	Description
Class	A blueprint or template for creating objects
Object	An actual instance created from a class
self	Refers to the current object inside the class
__init__()	Constructor method, runs when the object is created
The __init__ method initializes the attributes of the current instance (or object) of a class.
__del__()	Destructor method, runs when the object is deleted
del obj	Deletes the object manually

🧪 Example (in Python):'''

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self):
        print(f"{self.name} sent a message.")

# Creating objects
user1 = User("Alice")
user2 = User("Bob")

user1.send_message()  # Alice sent a message.
user2.send_message()  # Bob sent a message.

del user1  # Deletes the object (calls __del__ internally)
'''

🎯 Summary:
OOP was created to solve the limitations of procedural programming by making code more organized, reusable, and scalable.
It is essential for building real-world apps like WhatsApp or Facebook, where you need to manage millions of users efficiently with minimal code repetition.
