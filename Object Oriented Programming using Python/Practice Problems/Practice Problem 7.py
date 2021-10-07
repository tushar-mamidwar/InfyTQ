"""
An IT company wants to automate the process of allocating projects to its employees.
Write a python program to implement the class diagram given below.

Class description
    Employee:
        1. Initialize static variable, employee_count to 1000
        2, generate_employee_id(): Auto-generate attribute, employee_id starting from 'E1001'
           ('E1001','E1002','E1003'…etc)

    Project:
        1. update_number_of_employees(): Increment attribute, number_of_employees by 1

    Department:
        1. dep_project_list: Static list of Project objects which are in this department. Initialize
           it to an empty list.
        2. employee_dict: Static dictionary which contains the employee id as key and corresponding
           project_id as value. Initialize it to an empty dictionary.
        3. add_project(project_list): Accept a list of projects to be added to the department.
            a. Append the projects in the project list to static list, dep_project_list, if the total
               number of projects is not more than 5 (existing projects + new projects waiting to be added)
            b. Otherwise, return -1
        4. add_employee(employee,project_id): Accept the object of the Employee who should be added to
           the given project_id.
            a. If the given project is not available in the department, display appropriate message and
               return -1
            b. A project can have maximum 10 employees. If the number of employees in the given
               project is already 10, then display an error message and return -2
            c. Otherwise,
                - Generate employee id by invoking Employee.generate_employee_id() method
                - Add the employee to the given project by adding the employee_id as key and project_id as value in employee_dict
                - Increment the number of employees in the given project by invoking Project.update_number_of_employees() method

Perform case sensitive string comparison.
Create objects of Project class. Create a list of projects and add it to department by invoking
add_project() method. Also add employees to the projects in the department by invoking add_employee()
method and test your program.
"""


class Employee:
    __employee_count = 1000

    def __init__(self):
        self.__employee_id = None

    def generate_employee_id(self):
        Employee.__employee_count += 1
        self.__employee_id = 'E' + str(Employee.__employee_count)

    def get_employee_id(self):
        return self.__employee_id


class Project:
    def __init__(self, project_id, number_of_employees):
        self.__project_id = project_id
        self.__number_of_employees = number_of_employees

    def get_project__id(self):
        return self.__project_id

    def get_number_of_employees(self):
        return self.__number_of_employees

    def update_number_of_employees(self):
        self.__number_of_employees += 1


class Department:
    __dep_project_list = []
    __employee_dict = {}

    @staticmethod
    def add_project(project_list):
        if len(Department.__dep_project_list) < 5:
            for project in project_list:
                Department.__dep_project_list.append(project)
        return -1

    @staticmethod
    def add_employee(employee, project_id):
        project_id_index = -1
        for i in range(len(Department.__dep_project_list)):
            if Department.__dep_project_list[i].get_project__id() == project_id:
                project_id_index = i
                break
        else:
            print("Project id is invalid")
            return -1
        project = Department.__dep_project_list[project_id_index]
        if project.get_number_of_employees() < 10:
            employee.generate_employee_id()
            Department.__employee_dict[employee.get_employee_id()] = project_id
            project.update_number_of_employees()
        else:
            print("No more employees can be added")
            return -2
