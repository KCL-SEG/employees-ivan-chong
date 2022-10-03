"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self._calc_contract() + (0 if self.commission is None else self._calc_commission())

    def _calc_contract(self):
        #self.contract = [contract_type, contract_value, (number_of_hours_worked)]
        if self.contract[0] == 'Monthly':
            return self.contract[1]
        elif self.contract[0] == 'Hourly':
            return self.contract[1] * self.contract[2]

    def _calc_commission(self):
        #self.commission = [commission_type, commission_value, (contract_count)]
        if self.commission[0] == 'Bonus':
            return self.commission[1]
        elif self.commission[0] == 'Contract':
            return self.commission[1] * self.commission[2]

    def _str_contract(self):
        if self.contract[0] == 'Monthly':
            return f'monthly salary of {self.contract[1]}'
        else:
            return f'contract of {self.contract[1]} hours at {self.contract[2]}/hour'

    def _str_commission(self):
        str = ""
        if self.commission != None:
            if self.commission[0] == 'Bonus':
                str += f'bonus commission of {self.commission[1]}'
            else:
                str += f'commission for {self.commission[1]} contract(s) at {self.commission[2]}/contract'
        return f' and receives a {str}' if str != "" else ""

    def __str__(self):
        return f'{self.name} works on a {self._str_contract()}{self._str_commission()}.  Their total pay is {self.get_pay()}.'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ('Monthly', 4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ('Hourly', 100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', ('Monthly', 3000), ('Contract', 4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ('Hourly', 150, 25), ('Contract', 3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', ('Monthly', 2000), ('Bonus', 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ('Hourly', 120, 30), ('Bonus', 600))
