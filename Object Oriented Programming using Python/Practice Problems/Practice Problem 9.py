"""
Informatica, a consultancy services company has planned to offer cashless transaction service to its
employees. The employees can use their smart cards any transaction (credit/debit).

Write a python program to implement the class diagram given below.

Class description
SmartCard class:
    set_account_balance(account_balance): Initialize account_balance to 500.

Employee class:
    1. validate_employee_id(): Employee id should be in the range of 1000 (not inclusive) to 700000(inclusive). If valid return true. Else return false
    2. validate_card_no(): Validate employee's smart card number.
         a. Smart card number should have 9 characters
         b. It should begin with "INF" and
         c. It should not contain alphabets in any other positions
       If the above rules are satisfied, return true. Else return false

Transaction class:
    1. top_up_card(employee, amount): Accept the object of the employee whose smart card should be topped up with given amount.
        a. If the given amount is between 500 and 10000 (both inclusive),
            - If employee.employee_id and employee.smart_card.card_no are valid, add the given amount to employee.smart_card.account_balance
            - Else, return -1
        b. Else, return -1
    2. make_payment(employee,amount): Debit the given amount from the employee’s smart card and auto-generate attribute transaction_id starting with "T" followed by first digit of the employee id and first two numeric values of the card number, if the below rules are satisfied
        a. Enough balance should be present in employee's smart card
        b. employee.employee_id and employee.smart_card.account_balance should be valid
        c. It should be possible to maintain minimum balance of Rs.500 in the smart card even after the transaction is made
       If any of the above rules are not satisfied, return -1

Perform case sensitive string comparison.
Create an object of SmartCard class, create an object of Employee using the SmartCard object.
Create objects of Transaction class for the Employee object, invoke make_payment() and top_up_card() methods and display the details.
"""


class SmartCard:
    def __init__(self, card_no):
        self.__account_balance = 500
        self.__card_no = card_no

    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance

    def get_account_balance(self):
        return self.__account_balance

    def get_card_no(self):
        return self.__card_no


class Employee:
    def __init__(self, employee_id, smart_card, employee_name):
        self.__employee_name = employee_name
        self.smart_card = smart_card
        self.__employee_id = employee_id

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_id(self):
        return self.__employee_id

    def validate_employee_id(self):
        if 1000 < self.__employee_id <= 700000:
            return True
        return False

    def validate_card_no(self):
        card_no = self.smart_card.get_card_no()
        if len(card_no) == 9 and card_no[:3] == "INF" and card_no[3:].isdigit():
            return True
        return False


class Transaction:
    def __init__(self):
        self.__transaction_id = None

    def top_up_card(self, employee, amount):
        if 500 <= amount <= 10000 and employee.validate_employee_id() and employee.validate_card_no():
            employee.smart_card.set_account_balance(employee.smart_card.get_account_balance() + amount)
        else:
            return -1

    def make_payment(self, employee, amount):
        balance = employee.smart_card.get_account_balance()
        if (balance - 500) >= amount and employee.validate_employee_id():
            employee.smart_card.set_account_balance(balance - amount)
            self.__transaction_id = "T" + str(employee.get_employee_id())[0] + employee.smart_card.get_card_no()[3:5]
            return
        else:
            return -1

    def get_transaction_id(self):
        return self.__transaction_id


card1 = SmartCard("INF4567")
emp1 = Employee(4000, card1, "emp1")
transaction = Transaction()
print(transaction.top_up_card(emp1, 6000))
print(transaction.make_payment(emp1, 5000))
