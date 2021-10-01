"""
Problem Statement

Rio Logistics Company provides two categories of services, namely Passenger logistics and Goods logistics.

Some part of the program for this requirement is already given to you. You may need to implement or debug the given code to meet the requirements.

Starter code given to you has three classes – Logistics, PassengerLogistics and GoodsLogistics

Class Description:
Logistics class: Debug and add logic based on details given below
    1. Start reading should be less than end reading
    2. generate_consumer_id(): Attribute, consumer_id should be auto-generated starting from 7001.
       Use the static variable counter to implement it

PassengerLogistics class: Implement calculate_bill_amount() based on details mentioned below
calculate_bill_amount():
    a. Validate vehicle type and meter reading
    b. If valid,
        - Generate consumer id
        - Identify distance travelled based on start reading and end reading
        - Calculate bill amount based on vehicle type, distance travelled and charge per km
        - Note: charge per km for first 100km and charge per km for rest of the distance are different.
          Refer static lists provided in the class
        - If the bill amount is less than the minimum charge for the vehicle type, consider bill amount
          to be the minimum charge
        - Add 5% service tax on bill amount
        - Return the final bill amount
    c. Else, return -1

GoodsLogistics class: Debug calculate_bill_amount() based on details mentioned below
calculate_bill_amount():
    a. Validate carrier type and meter reading
    b. If valid,
        - Generate consumer id
        - Identify distance travelled based on start reading and end reading
        - Calculate bill amount based on carrier type, distance travelled and charge per km
        - Note: Charge per kilometer for first 1000kg of goods is given in the table
        - For every next 1000kg, charge per kilometer should be doubled until 3000kg (eg: 20,40,80 or 30,60,120 etc).
        - If weight is above 3000kg, then consider charge per kilometer to be Rs.200 irrespective of carrier type
        - Add 10% service tax on bill amount
        - Add Rs. 2000 as sales tax amount on the taxed bill amount
        - Return the final bill amount
    c. Else, return -1

Note: Perform case sensitive string comparison
"""
# lex_auth_012737551870525440860
from abc import ABCMeta, abstractmethod


class Logistics(metaclass=ABCMeta):
    __counter = 7000

    def __init__(self, start_reading, end_reading):
        self.__consumer_id = None
        self.__start_reading = start_reading
        self.__end_reading = end_reading

    def get_consumer_id(self):
        return self.__consumer_id

    def get_start_reading(self):
        return self.__start_reading

    def get_end_reading(self):
        return self.__end_reading

    def validate_meter_reading(self):
        if (self.__start_reading < self.__end_reading):
            return True
        else:
            return False

    def generate_consumer_id(self):
        if Logistics.__counter == None:
            Logistics.__counter = 7000
        Logistics.__counter += 1
        self.__consumer_id = Logistics.__counter

    @abstractmethod
    def calculate_bill_amount(self):
        pass


class PassengerLogistics(Logistics):
    __list_vehicle = ["BMW", "TOYOTA", "FORD"]
    __list_minimum_charge = [3000, 1500,
                             1000]  # these lists are storing vehicle type, minimum charge, rate per kilometer for first hundred and rate per kilometer for rest of distance
    __list_charge_for_hundred = [30, 15, 10]  # there is a one to one correspondence
    __list_charge_after_hundred = [25, 12, 7]

    def __init__(self, vehicle_type, start_reading, end_reading):
        super().__init__(start_reading, end_reading)
        self.__vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type

    def validate_vehicle_type(self):
        for index in range(0, len(PassengerLogistics.__list_vehicle)):
            if (PassengerLogistics.__list_vehicle[index] == self.__vehicle_type):
                return index
        return -1

    def calculate_bill_amount(self):
        index = self.validate_vehicle_type()
        if index != -1 and self.validate_meter_reading():
            self.generate_consumer_id()
            distance_travelled = self.get_end_reading() - self.get_start_reading()
            price = 0
            if distance_travelled <= 100:
                price = distance_travelled * PassengerLogistics.__list_charge_for_hundred[index]
            else:
                price = 100 * PassengerLogistics.__list_charge_for_hundred[index] + (distance_travelled - 100) * \
                        PassengerLogistics.__list_charge_after_hundred[index]
            if price < PassengerLogistics.__list_minimum_charge[index]:
                price = PassengerLogistics.__list_minimum_charge[index]
            price *= 1.05
            return price
        return -1


class GoodsLogistics(Logistics):
    __carrier_dict = {"TATA": 20, "EICHER": 30,
                      "FORCE": 35}  # stores the carrier type and rate per kilometer for 1000kg

    def __init__(self, carrier_type, goods_weight, start_reading, end_reading):
        super().__init__(start_reading, end_reading)
        self.__carrier_type = carrier_type
        self.__goods_weight = goods_weight

    def get_carrier_type(self):
        return self.__carrier_type

    def get_goods_weight(self):
        return self.__goods_weight

    def validate_carrier_type(self):
        for carrier in GoodsLogistics.__carrier_dict:
            if (carrier == self.__carrier_type):
                return True
        return False

    def calculate_bill_amount(self):
        if (self.validate_carrier_type()):
            if (self.validate_meter_reading()):
                self.generate_consumer_id()
                total_distance = self.get_end_reading() - self.get_start_reading()
                if (self.__goods_weight <= 1000):
                    charge_per_kilometer = self.__carrier_dict[self.__carrier_type]
                elif (self.__goods_weight > 1000 and self.__goods_weight <= 2000):
                    charge_per_kilometer = self.__carrier_dict[self.__carrier_type] * 2
                elif (self.__goods_weight > 2000 and self.__goods_weight <= 3000):
                    charge_per_kilometer = self.__carrier_dict[self.__carrier_type] * 4
                else:
                    charge_per_kilometer = 200
                bill_amount = total_distance * charge_per_kilometer
                bill_amount = bill_amount + (bill_amount * 0.1) + 2000
                return bill_amount
            else:
                return -1
        else:
            return -1


passenger_logistic = PassengerLogistics("BMW", 300, 400)
bill_amount = passenger_logistic.calculate_bill_amount()
if (bill_amount == -1):
    print("Invalid vehicle type or meter reading ")
else:
    print("Consumer id    :", passenger_logistic.get_consumer_id())
    print("Start reading  :", passenger_logistic.get_start_reading())
    print("End reading    :", passenger_logistic.get_end_reading())
    print("Total Amount   :", bill_amount)
print("------------------------------------------------------------")
goods_logistic = GoodsLogistics("FORCE", 3000, 300, 400)
bill_amount = goods_logistic.calculate_bill_amount()
if (bill_amount == -1):
    print("Invalid career type or meter reading ")
else:
    print("Consumer id    :", goods_logistic.get_consumer_id())
    print("Goods weight   :", goods_logistic.get_goods_weight())
    print("Start reading  :", goods_logistic.get_start_reading())
    print("End reading    :", goods_logistic.get_end_reading())
    print("Total Amount   :", bill_amount)
