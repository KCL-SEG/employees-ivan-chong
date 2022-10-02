"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, contract_value, number_of_hours_worked=None, commission_type=None, commission_value=None, contract_count=None):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type
        self.commission_value = commission_value
        self.contract_value = contract_value
        self.number_of_hours_worked = number_of_hours_worked
        self.contract_count = contract_count

    def get_pay(self):
        return self._calc_contract() + (0 if self.commission_type is None else self._calc_commission())

    def _calc_contract(self):
        if (self.contract_type == 'Monthly'):
            return self.contract_value
        elif (self.contract_type == 'Hourly'):
            return self.contract_value * self.number_of_hours_worked

    def _calc_commission(self):
        if (self.commission_type == 'Bonus'):
            return self.commission_value
        elif (self.commission_type == 'Contract'):
            return self.contract_count * self.commission_value

    def __str__(self):
        if (self.contract_type == 'Monthly'):
            contract_str = f'{self.name} works on a monthly salary of {self.contract_value}'
        elif (self.contract_type == 'Hourly'):
            contract_str = f'{self.name} works on a contract of {self.number_of_hours_worked} hours at {self.contract_value}/hour'

        if (self.commission_type == 'Contract'):
            commission_str = f' and receives a commission for {self.contract_count} contract(s) at {self.commission_value}/contract'
        elif (self.commission_type == 'Bonus'):
            commission_str = f' and receives a bonus commission of {self.commission_value}'

        return f'{contract_str}{"" if self.commission_type is None else commission_str}.  Their total pay is {self.get_pay()}.'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract_type='Monthly', contract_value=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract_type='Hourly', contract_value=25, number_of_hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract_type='Monthly', contract_value=3000, commission_type='Contract', contract_count=4, commission_value=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract_type='Hourly', contract_value=25, number_of_hours_worked=150, commission_type='Contract', contract_count=3, commission_value=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract_type='Monthly', contract_value=2000, commission_type='Bonus', commission_value=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract_type='Hourly', contract_value=30, number_of_hours_worked=120, commission_type='Bonus', commission_value=600)
