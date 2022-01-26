"""
Problem Statement
Write a Python program to generate tickets for online bus booking, based on the class diagram given below.



Method description:

1. Initialize static variable counter to 0
2. validate_source_destination(): Validate source and destination. source must always be Delhi and destination
   can be either Mumbai, Chennai, Pune or Kolkata. If both are valid, return true. Else return false
3.generate_ticket():
    a. Validate source and destination
    b. If valid, generate ticket id and assign it to attribute, ticket_id. Ticket id should be generated
    with the first letter of source followed by first letter of destination and an auto-generated value
    starting from 01 (Ex: DM01, DP02,.. ,DK10,DC11)
    c. Else, set ticket_id as None
Note: Perform case insensitive string comparison


For testing:

- Create objects of Ticket class
- Invoke generate_ticket() method on Ticket object
- Display ticket id, passenger name, source, destination
- In case of error/invalid data, display appropriate error message
"""


class Ticket:
    counter = 0

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.__source = source
        self.__destination = destination

    def validate_source_destination(self):
        if self.__source.title() == "Delhi" and (
            self.__destination.title() == "Mumbai"
            or self.__destination.title() == "Pune"
            or self.__destination.title() == "Kolkata"
            or self.__destination.title() == "Chennai"
        ):
            return True
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter += 1
            self.__ticket_id = (
                self.__source[0]
                + self.__destination[0]
                + "{:02d}".format(Ticket.counter)
            )
        else:
            return False

    def get_ticket_id(self):
        return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination


passenger = Ticket("Tushar", "Delhi", "Pune")
ticket = passenger.generate_ticket()
if ticket == False:
    print("Invalid Input")
else:
    print(
        passenger.get_passenger_name(),
        passenger.get_ticket_id(),
        passenger.get_source(),
        passenger.get_destination(),
    )
