
"""
Decorator is a structural design pattern that lets you attach new behaviors to objects
by placing these objects inside special wrapper objects that contain the behaviors.
"""

class DecoratorTest():

    def __wrapper1(func):

        def inner1(*args, **kwargs):

            print('This is before the function call!')
            func(*args, **kwargs)
            print('This is after the function call!')

        return inner1

    def __wrapper2(func):

        def inner2(n):

            print('This is before the function call!')
            func(n)
            print('This is after the function call!')

        return inner2

    @staticmethod
    @__wrapper1
    def spit_numbers1(n=10):
        print([i for i in range(n)])

    @staticmethod
    @__wrapper2
    def spit_numbers2(n=10):
        print([i for i in range(n)])

DecoratorTest.spit_numbers1(3)

DecoratorTest.spit_numbers2(4)


class Coffee():

    def __init__(self):
        self.__cost = 1

    def get_cost(self):
        return self.__cost
    
class MilkCoffee(Coffee):

    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 2
    
class SugarCoffee(Coffee):

    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 5
    
def main():

    coffee = Coffee()
    milk_coffee = MilkCoffee(coffee)
    print(milk_coffee.get_cost())

    milk_sugar_coffee = SugarCoffee(milk_coffee)
    print(milk_sugar_coffee.get_cost())

if __name__ == '__main__':
    main()