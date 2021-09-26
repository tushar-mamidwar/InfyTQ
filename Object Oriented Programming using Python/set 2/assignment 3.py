"""
Problem Statement

Care hospital wants to calculate the bill amount to be paid by patients visiting the hospital.
Bill amount includes consultation fees and price of medicines purchased from their pharmacy.

Write a Python program to implement the class diagram given below.



Method description:

calculate_bill_amount(consultation_fees, quantity_list, price_list): Accept consultation_fees,
    quantity_list (quantities of medicines purchased) and price_list (price per quantity of medicines purchased)

    a. Calculate total bill amount to be paid by the patient. Bill amount includes consultation fees
       and price of medicines
    b. Initialize attribute, bill_amount with the total bill amount

Note: quantity_list and price_list have one-to-one correspondence. Quantity and price per quantity of 1st medicine purchased by the patient is present at 0th index of both lists, 2nd medicine is present at 1st index and so on.

For testing:

Create objects of Bill class
Invoke calculate_bill_amount(consultation_fees, quantity_list, price_list) method on Bill object by passing consultation fees, quantity list and price list
Display bill id, patient name and bill amount
"""
class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=None

    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount
    def get_patient_name(self):
        return self.__patient_name
    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        bill_amount=consultation_fees
        for i in range(len(quantity_list)):
            bill_amount+=quantity_list[i]*price_list[i]
        self.__bill_amount=bill_amount

patient=Bill(2343,"patient1")
patient.calculate_bill_amount(250,[2,4,3,4],[34,56,12,5])
print(patient.get_bill_id(),patient.get_patient_name(),patient.get_bill_amount())