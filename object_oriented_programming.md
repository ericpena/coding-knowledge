# Object Oriented Programming

## Key Principles of OOP
* Encapsulation: Grouping related variables and functions that operate on them into objects.
* Inheritance: Creating new classes from existing ones, promoting code reuse.
* Polymorphism: Writing code that can work with objects of multiple types.
* Abstraction: Hiding implementation details and showing only the necessary features.

## Study Tips
* Practice writing classes and creating objects.
* Implement simple projects using OOP principles.
* Understand how inheritance, polymorphism, encapsulation, and abstraction work in practice.
* Review sample interview questions and solutions related to OOP in Python.

## Fundamentals
### Classes and Objects
Class: A blueprint for creating objects (a particular data structure), defining attributes and methods.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says woof!"
```

Object: Instance of a class
```python
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!
```
### Attributes and Methods

Attributes: Variables that belong to a class (class attributes) or an instance of a class (instance attributes).

```python
class Car:
    wheels = 4  # Class attribute
    
    def __init__(self, make, model):
        self.make = make  # Instance attribute
        self.model = model
```

Methods: Functions defined within a class that describe the behaviors of the objects of the class.

```python
class Car:
    def start(self):
        return "The car is starting"
```

### The `__init__` Method

Constructor: The __init__ method is called when an object is instantiated, allowing you to initialize attributes.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
```

### Inheritance

Allows a class (child) to inherit attributes and methods from another class (parent).

```python
class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__('Dog')
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.make_sound())  # Output: Woof!
```

### Encapsulation

Encapsulation restricts access to certain components of an object and prevents the accidental modification of data. Use underscores to indicate private attributes.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "Insufficient funds"
    
    def get_balance(self):
        return self.__balance
```

### Polymorphism

Allows objects of different classes to be treated as objects of a common superclass. It provides a way to use a common interface for multiple forms (data types).

```python
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog("Buddy", 3), Cat("Whiskers")]

for animal in animals:
    print(animal.make_sound())  # Output: Woof! Meow!
```

### Abstraction

Abstraction involves hiding the complex implementation details and showing only the necessary features of an object. This can be achieved using abstract classes (from the `abc` module)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(10, 20)
print(rect.area())  # Output: 200
```

## Abstraction Specifics

An abstract class in object-oriented programming (OOP) serves as a blueprint for other classes. It allows you to define methods that must be created within any child classes built from the abstract class. Abstract classes cannot be instantiated on their own and are used to provide a common interface for all the subclasses.

Key Points of Abstract Classes:
Enforcing a Contract:
Abstract classes define a set of methods that must be implemented by any subclass. This ensures that certain methods are always present in the subclasses, providing a consistent interface.

Partial Implementation:
Abstract classes can contain both concrete methods (with implementation) and abstract methods (without implementation). This allows for a shared base functionality while leaving specific details to be implemented by subclasses.

Promoting Code Reusability:
By defining common behavior in an abstract class, you can avoid code duplication in subclasses. Subclasses inherit the common behavior and only implement the specific behavior.

Example in Python
In Python, you can define an abstract class using the abc module. Here is an example:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def move(self):
        print("Moving...")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# This will raise an error
# animal = Animal()

dog = Dog()
print(dog.sound())  # Output: Woof!
dog.move()          # Output: Moving...

cat = Cat()
print(cat.sound())  # Output: Meow!
cat.move()          # Output: Moving...
```

### Explanation:

1. Abstract Class Definition:

Animal is an abstract class that inherits from ABC (Abstract Base Class).
The sound method is an abstract method, meaning it has no implementation in the Animal class and must be implemented in any subclass.
The move method is a concrete method with an implementation that will be inherited by subclasses.

2. Concrete Subclasses:

Dog and Cat are concrete subclasses that inherit from Animal.
Both Dog and Cat provide implementations for the sound method.

3. Instantiation:

Trying to instantiate Animal directly will raise an error because it contains abstract methods.
Dog and Cat can be instantiated because they provide implementations for all abstract methods defined in Animal.

### Benefits of Using Abstract Classes:
* Enforced Consistency: Ensures that all subclasses follow a certain structure, making it easier to understand and maintain the code.
* Code Reusability: Common methods and properties can be defined once in the abstract class and reused across multiple subclasses.
* Clear Design: Abstract classes help to define a clear and consistent interface for a family of related classes, which can improve the design and readability of the code.

Abstract classes are a powerful tool in OOP that help to create a well-defined and consistent code structure, promoting good design principles and code reuse.