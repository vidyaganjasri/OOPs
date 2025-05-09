'''Instance Method: Operates on instance-specific data (e.g., borrowing a book for a specific user).

Class Method: Operates on class-level data (e.g., the total number of books borrowed across all users).

Static Method: Does not access or modify any class or instance data (e.g., checking if the library is open on a specific day).'''
class Library:
    total_books = 0 
    def __init__(self,name):
        self.name = name 
        self.books = []
        
    def took(self,title):
        self.books.append(title)
        Library.total_books+=1 
        print(f"{self.name} has borrowed {title}")
    
    def my_books(self):
        print(self.books)
    
    @classmethod
    def total_books_lib(cls):
        print(cls.total_books)
        
    @staticmethod
    def is_lib_holiday(day):
        print("sunday"==day.lower().strip())
        
arjith = Library('arjith')
arjith.took("pta")
arjith.my_books()

kushal = Library("kushal")
kushal.took("lara")
kushal.my_books()

arjith.total_books_lib()

kushal.is_lib_holiday("monday")
arjith.is_lib_holiday("sunday")


#output:
'''    
arjith has borrowed pta
['pta']
kushal has borrowed lara
['lara']
2
False
True
'''
