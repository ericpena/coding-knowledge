
"""
Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.
1. create interface with attributes and global function (as abstract class)
2. create separate operations
3. create context
"""
from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def apply_operation(self, a, b):
        pass

class Addition(Operation):

    def apply_operation(self, a, b) -> float:
        return a + b
    
    def __str__(self):
        return '+'

class Subtraction(Operation):

    def apply_operation(self, a, b) -> float:
        return a - b
    
    def __str__(self):
        return '-'
    
class OperationContext():

    def __init__(self, strategy):
        self._strategy = strategy

    def apply_operation(self, a, b) -> float:
        return self._strategy.apply_operation(a, b)

def main():

    addition_strategy_operation = Addition()
    subtraction_strategy_operation = Subtraction()
    
    a = 10
    b = 3

    operation_context = OperationContext(addition_strategy_operation)
    result = operation_context.apply_operation(a, b)
    print(f'{a} {addition_strategy_operation} {b} = {result}')
    
    operation_context = OperationContext(subtraction_strategy_operation)
    result = operation_context.apply_operation(a, b)
    print(f'{a} {subtraction_strategy_operation} {b} = {result}')
    

if __name__ == "__main__":
    main()