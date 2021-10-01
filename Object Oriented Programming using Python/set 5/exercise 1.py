"""
Problem Statement
ABC DTH (Direct to Home) firm wants to calculate monthly rent for its consumers.
A consumer can register for one Base Package. Write a python program to implement the below given class diagram.



Class Description:
    DirectToHomeService class:
        1. Initialize static variable counter to 101
        2. Inside constructor, auto-generate consumer_number starting from 101

    BasePackage class:
        1. validate_base_pack_name():
            a. Validate base pack name. Valid values are "Silver", "Gold" and "Platinum".
            b. If invalid, set attribute, base_pack_name as "Silver" and display "Base package name is incorrect, set to Silver"
        2. calculate_monthly_rent():
            a. Check if subscription period is between 1 and 24 (both inclusive). If so,
                - Validate base pack name
                - Identify monthly rent based on base pack. Refer table given.
                - Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
                - Calculate final monthly rent as per the formula given below:
                - final monthly rent = ((monthly rent * subscription period) – discount amount)/subscription period
                - Return the calculated final monthly rent
            b. If not, return -1

Base Pack Name                      Monthly Rent
Silver                                 350.00
Gold                                   440.00
Platinum                               560.00

Note: Perform case sensitive string comparison

For testing:

Create objects of BasePackage class
Invoke calculate_monthly_rent() on BasePackage object
Display the details
"""
from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter += 1
        self.__consumer_name=consumer_name
    def get_consumer_name(self):
        return self.__consumer_name
    def get_consumer_number(self):
        return self.__consumer_number
    @abstractmethod
    def calculate_monthly_rent(self):
        pass



class BasePackage(DirectToHomeService):
    def __init__(self,subscription_period,base_pack_name,consumer_name):
        super().__init__(consumer_name)

        self.__base_pack_name=base_pack_name
        self.__subscription_period = subscription_period
    def validate_base_pack_name(self):
        packages=["Silver","Gold","Platinum"]
        if self.__base_pack_name in packages:
            return True
        self.__base_pack_name="Silver"
        print("Base package name is incorrect, set to Silver")
    def calculate_monthly_rent(self):
        if not 1<=self.__subscription_period<=24:
            return -1
        self.validate_base_pack_name()
        monthly_charges={'Silver':350,'Gold':440,'Platinum':560}
        total_charge=monthly_charges[self.__base_pack_name]*self.__subscription_period
        if self.__subscription_period>12:
            total_charge-=monthly_charges[self.__base_pack_name]
        return total_charge/self.__subscription_period
    def get_subscription_period(self):
        return self.__subscription_period
    def get_base_pack_name(self):
        return self.__base_pack_name

obj=BasePackage(23,'Silver',"cus1")



