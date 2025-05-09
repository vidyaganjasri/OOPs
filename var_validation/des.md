In Python, we can handle attributes (variables) in two ways: using explicit function calls or using the @property decorator.

#1. Without @property (Using Functions)
Without the @property decorator, you have to explicitly define getter and setter methods for attributes.

To get the value of an attribute, you would call a method like p.get_age().

To set the value, you would call a method like p.set_age(new_age).


#2.With @property (Cleaner and More Elegant)
Using the @property decorator allows you to access attributes directly, like normal variables, while still applying custom behavior (like validation).

Getter: You define a method with the @property decorator, allowing access via p.age instead of calling p.get_age().

Setter: You define a method with @<property_name>.setter to update the value, but you can still assign the value directly using p.age = new_value instead of calling a function like p.set_age(new_value).
