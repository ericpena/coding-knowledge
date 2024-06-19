
from dataclasses import dataclass

@dataclass
class Employee():

    # :: init not needed for dataclasses
    employee_id : int
    name : str
    position : str
    salary : int | float
    performance_score : int

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    def calculate_bonus(self):

        if 1 <= self.performance_score <= 3:
            self.salary *= 1.05
        elif 4 <= self.performance_score <= 7:
            self.salary *= 1.1
        elif 8 <= self.performance_score <= 10:
            self.salary *= 1.2
        else:
            print('Not Valid Performance Score.')
            pass
    
def main():
    e1 = Employee(0, 'Eric', 'Engineer', 1000, 5)
    e2 = Employee(1, 'David', 'Engineer', 2000, 1)
    e3 = Employee(employee_id=2, name='Richard', position='Senior Engineer', salary=4000, performance_score=8)

    data4 = [3, 'Ron', 'Principal Engineer', 5000, 2]
    e4 = Employee.from_sequence(data4)

    for e in [e1, e2, e3, e4]:
        print(e.salary)
        e.calculate_bonus()
        print(e.salary)
        print('------------------')

if __name__ == "__main__":
    main()