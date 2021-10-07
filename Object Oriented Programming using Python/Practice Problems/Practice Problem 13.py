"""
Problem Statement
Infosys wants to automate the visitor management process in the campus. An employee can register only one visitor at a time. Employee should register the visitor details in advance so that the security team will have the details when the visitors arrive in the campus.
Write a python program to implement the class diagram given below.



Class description
Security class:

    employee_list: Static list which contains the list of employees in the company. Initialize it to an empty list

    visitor_list: Static list which contains the objects of visitor who are registered by the employees. Initialize it to an empty list. There is one-to-one correspondence between the two lists

    Constructor: Initialize Security.employee_list using the value passed to it. Initialize Security.visitor_list with a list of same size as that of Employee.employee_list containing None in all index positions.

    security_check(employee,visitor): Check the visitor details at the time of arrival against the registered details based on the rules given below.

    The given employee should be present in Security,employee_list

    If present, employee should have already registered the given visitor

    If registered, visitor should have a valid id proof. Valid id proofs are "Passport", "Voter id" and "PAN Card"


Employee class:
    register_visitor(visitor): Register the given visitor based on the rules given below.

    Employee should be present in Security.employee_list. [Hint: validate using employee_id]

    Employee should not have registered any visitor

    Validate the relationship of the visitor with the employee. Relationship can be "Parent", "Sibling", "Spouse" or "Child"

    If all the above three rules are satisfied, update the visitor object in Security.visitor_list at the index position corresponding to the employee and return true

    Else, return false

    If all the rules are satisfied return true. Else return false.

Perform case sensitive comparison.
Create objects of Employee, Visitor and Security classes, invoke appropriate methods and test your program.
"""


class Security:
    employee_list = []
    visitor_list = []

    def __init__(self, employee_list):
        Security.employee_list = employee_list
        Security.visitor_list = [None] * len(Security.employee_list)

    def security_check(self, employee, visitor):
        if employee in Security.employee_list:
            index = Security.employee_list.index(employee)
            if Security.visitor_list[index] == visitor:
                valid_id_proofs = ('Passport', 'Voter Id', 'PAN Card')
                if visitor.get_valid_id() in valid_id_proofs:
                    return True
                return False
            return False
        return False


class Employee:
    def __init__(self, employee_name, employee_id):
        self.__employee_id = employee_id
        self.__employee_name = employee_name

    def get_employee_id(self):
        return self.__employee_id

    def get_employee_name(self):
        return self.__employee_name

    def register_visitor(self, visitor):
        for i in range(len(Security.employee_list)):
            if Security.employee_list[i].get_employee_id() == self.__employee_id:
                if Security.visitor_list[i] != None:
                    valid_relationships = ["Parent", "Sibling", "Spouse", "Child"]
                    if visitor.get_relationship_wiht_emp() in valid_relationships:
                        Security.visitor_list[i] = visitor
                        return True
                    return False
                return False
            return False


class Visitor:
    def __init__(self, visitor_name, valid_id, relationship_with_emp):
        self.__visitor_name = visitor_name
        self.__valid_id = valid_id
        self.__relationship_with_emp = relationship_with_emp

    def get_visitor_name(self):
        return self.__visitor_name

    def get_valid_id(self):
        return self.__valid_id

    def get_relationship_with_emp(self):
        return self.__relationship_with_emp


Sec = Security(["emp1", "emp2"])
