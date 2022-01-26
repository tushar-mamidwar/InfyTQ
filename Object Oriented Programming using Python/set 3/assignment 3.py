"""
Problem Statement
A telecom company wants to generate reports on the call details of the customers. Each customer can make
multiple phone calls.

Problem Statement:
The parse_customer method takes a list of Customer objects and a list of CallDetail objects. For every
customer, identify all the corresponding Call Detail objects ( the customer phone number and the phone
number of Call detail object have to match ), add them to the list_of_calls of corresponding customer
object and add the updated customer object to list_of_customer_calldetail_objects of Util class.
"""


# lex_auth_01275802761392128033
class Customer:
    def __init__(self, phone_no, name, age):
        self.phone_no = phone_no
        self.name = name
        self.age = age
        self.list_of_calls = None


class CallDetail:
    def __init__(self, phone_no, called_no, duration):
        self.phone_no = phone_no
        self.called_no = called_no
        self.duration = duration


class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects = []

    def parse_customer(self, list_of_customers, list_of_calls):
        for customer in list_of_customers:
            customer.list_of_calls = []
            for call in list_of_calls:
                if customer.phone_no == call.phone_no:
                    customer.list_of_calls.append(call)
            self.list_of_customer_calldetail_objects.append(customer)


cust1 = Customer(9900009901, "cust1", 23)
cust2 = Customer(9900009902, "cust2", 24)
cust3 = Customer(9900009903, "cust3", 25)
list_of_customers = [cust1, cust2, cust3]

call1 = CallDetail(9900009901, 8800123401, 5)
call2 = CallDetail(9900009903, 8800123402, 10)
call3 = CallDetail(9900009902, 8800123403, 2)
call4 = CallDetail(9900009901, 8800123404, 8)
call5 = CallDetail(9900009901, 8800123405, 7)
call6 = CallDetail(9900009903, 8800123406, 9)
call7 = CallDetail(9900009903, 8800123407, 4)
list_of_calls = [call1, call2, call3, call4, call5, call6, call7]

Util().parse_customer(list_of_customers, list_of_calls)
