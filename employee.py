"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.get_salary() + self.commission.get_commission()

    def __str__(self):
        return f'{self.name} {self.contract.__str__()}{self.commission.__str__()}.  Their total pay is {self.get_pay()}.'

class Salary:
    def __init__(self, salary):
        self.salary = salary
    def get_salary(self):
        pass
    def __str__(self):
        pass

class MonthlySalary(Salary):
    def get_salary(self):
        return self.salary
    def __str__(self):
        return f'works on a monthly salary of {self.salary}'

class HourlySalary(Salary):
    def __init__(self, hours, salary):
        Salary.__init__(self, salary)
        self.hours = hours
    def get_salary(self):
        return self.salary * self.hours
    def __str__(self):
        return f'works on a contract of {self.hours} hours at {self.salary}/hour'

class Commission:
    def __init__(self, commission):
        self.commission = commission
    def get_commission(self):
        pass
    def __str__(self):
        pass

class NoCommission(Commission):
    def __init__(self):
        pass
    def get_commission(self):
        return 0
    def __str__(self):
        return ''

class BonusCommission(Commission):
    def get_commission(self):
        return self.commission
    def __str__(self):
        return f' and receives a bonus commission of {self.commission}'

class ContractCommission(Commission):
    def __init__(self, contract_count, commission):
        Commission.__init__(self, commission)
        self.contract_count = contract_count
    def get_commission(self):
        return self.commission * self.contract_count
    def __str__(self):
        return f' and receives a commission for {self.contract_count} contract(s) at {self.commission}/contract'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(100, 25), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(120, 30), BonusCommission(600))
