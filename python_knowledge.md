# Python Knowledge

1. What is the difference between == and is in Python?
Answer:

== checks for value equality. It determines if the values of two objects are equal.
is checks for identity equality. It determines if two references point to the same object in memory.

---
2. How does Python's garbage collection work?
Answer:
Python uses automatic garbage collection to manage memory. It primarily uses reference counting and a cyclic garbage collector to detect and clean up unused objects.

Reference Counting: Each object has a reference count that increases when a reference to the object is created and decreases when a reference is deleted.
Cyclic Garbage Collector: Handles cyclic references by identifying and collecting groups of objects that reference each other but are not reachable from the program.

---
3. What are Python decorators and how do you use them?
Answer:
Decorators are a way to modify or enhance functions or methods without changing their definition. They are typically used to add functionality to existing code in a reusable way.

Example of a decorator:
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```python
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

---
4. What are list comprehensions and generator expressions? Provide examples.

Answer:

List Comprehensions: A concise way to create lists.
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Generator Expressions: Similar to list comprehensions, but they return a generator object which yields items one at a time and uses less memory.

```python
squares_gen = (x**2 for x in range(10))
print(list(squares_gen))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---
5. Explain the use of self in Python classes.
Answer:
self is a reference to the current instance of the class and is used to access variables and methods associated with the class. It allows each object to keep track of its own data.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Alice", 30)
person.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

---
6. What is the Global Interpreter Lock (GIL) in Python?
Answer:
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This means that even in a multi-threaded Python program, only one thread can execute Python code at a time. The GIL can be a limitation for CPU-bound programs but doesn't affect I/O-bound programs as much.

---
7. How do you handle exceptions in Python? Provide an example.
Answer:
Exceptions in Python are handled using try, except, else, and finally blocks. The try block contains the code that might raise an exception, the except block contains the code to handle the exception, the else block (optional) runs if no exceptions are raised, and the finally block (optional) contains code that always runs regardless of whether an exception was raised.

Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
else:
    print("No exceptions were raised.")
finally:
    print("This block runs no matter what.")
```

Output:
```python
Caught an exception: division by zero
This block runs no matter what.
```

---
8. What are the differences between staticmethod and classmethod in Python?
Answer:

@staticmethod: A static method does not receive any implicit first argument. It behaves like a plain function that belongs to a class’s namespace.
@classmethod: A class method receives the class as its first argument, which is typically named cls. It can access and modify class state.

Example:

```python
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"
    
    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"

print(MyClass.static_method())  # Output: This is a static method
print(MyClass.class_method())  # Output: This is a class method of MyClass
```

Additionally, you don't have to instantiate an object in order to call these methods.

---
9. What is a Python generator and how does it work?
Answer:
A generator in Python is a function that returns an iterator which we can iterate over (one value at a time). Generators are written using the yield statement instead of return. They are memory efficient because they produce items one at a time and only when required.

Example:
```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
for number in counter:
    print(number)
```

Output:
```python
1
2
3
4
5
```

---
10. Explain the concept of list slicing and provide an example.
Answer:
List slicing allows you to access a subset of a list by specifying a start, stop, and step index. The syntax for slicing is list[start:stop:step].

Example:
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing examples
print(numbers[2:7])      # Output: [2, 3, 4, 5, 6]
print(numbers[:5])       # Output: [0, 1, 2, 3, 4]
print(numbers[5:])       # Output: [5, 6, 7, 8, 9]
print(numbers[::2])      # Output: [0, 2, 4, 6, 8]
print(numbers[::-1])     # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
