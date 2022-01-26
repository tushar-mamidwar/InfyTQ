"""
Problem Statement
A company is in the process of providing annual hike to its employees based on incentives and performance of the employee.
A partial python program has been written for the above requirement, complete the code by using the information and part of class diagram given below:



Class Description:
The program has three classes – Company, Employee and PermanentEmployee. Company and Employee classes are already coded for you. Refer starter code.

Employee class:
1. Every employee is given a performance rating (1-3) at the end of every year
2. Last five year's performance rating of an employee is stored in the attribute, performance_list

Refer table for example and interpretation of data in performance_list, assuming current year is 2015

                                       0         1         2         3         4
performance_list                       1         2         1         1         2
Corresponding year                    2010      2011      2012      2013      2014



Permanent Employee class:

1. identify_performance_hike():
    a. Permanent employees are eligible for performance hike based on their last three years performance as given in table
    b. Identify the hike % and return it. If hike is not applicable, return None

        Performance for last three years                            Hike %
        Last year       Last but one        Last but two
        1                    1             Not considered             5
        1                    2                  1                     3

2. identify_job_level_hike():
    a. Permanent employees are eligible for hike based on job level
    b. Identify job level based hike using the information provided in the Company class and return it. If hike cannot be identified, return None
3. identify_incentive():
    a. Permanent employees are eligible for company level, employee level and permanent employee level incentives
    b. Calculate total incentive (in Rs) and return it
3. calculate_salary(): Calculate total salary
    a. Implement it in the same way as it is implemented in Employee class
Note: Perform case sensitive string comparison
For testing:

- Create objects of Company class and PermanentEmployee class

- Invoke calculate_salary() on PermanentEmployee object

- Display the details of the employee
"""


# lex_auth_0127575870118707200
class Company:
    # Stores hike% based on job level.
    dict_hike = {"A": 5, "B": 6, "C": 10, "D": 11}
    # Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive = 5000

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive


class Employee:
    def __init__(self, emp_id, e_incentive, job_level, salary, performance_list):
        self.emp_id = emp_id
        self.__e_incentive = e_incentive
        self.__salary = salary
        self.__job_level = job_level
        self.__performance_list = performance_list

    def get_e_incentive(self):
        return self.__e_incentive

    def get_performance_list(self):
        return self.__performance_list

    def get_salary(self):
        return self.__salary

    def get_job_level(self):
        return self.__job_level

    def identify_performance_hike(self):
        return None

    def identify_job_level_hike(self):
        return None

    def identify_incentive(self):
        return None

    def update_salary(self, hike, incentive):
        self.__salary = (self.__salary + self.__salary * hike / 100) + incentive

    def calculate_salary(self):
        jl_hike = self.identify_job_level_hike()
        ex_hike = self.identify_performance_hike()
        if jl_hike != None:
            hike = jl_hike
            if ex_hike != None:
                hike += ex_hike
            incentive = self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False


# Implement the class here
class PermanentEmployee(Employee):
    def __init__(
        self, emp_id, e_incentive, p_incentive, job_level, salary, performance_list
    ):
        super().__init__(emp_id, e_incentive, job_level, salary, performance_list)
        self.__p_incentive = p_incentive

    def get_p_incentive(self):
        return self.__p_incentive

    def identify_incentive(self):
        return self.__p_incentive + self.get_e_incentive() + Company.get_c_incentive()

    def identify_performance_hike(self):
        performance_list = self.get_performance_list()
        if performance_list[-1] == 1:
            if performance_list[-2] == 1:
                return 5
            elif performance_list[-2] == 2 and performance_list[-3] == 1:
                return 3
        return None

    def identify_job_level_hike(self):
        try:
            return Company.dict_hike[self.get_job_level()]
        except:
            return None

    def calculate_salary(self):
        job_level_hike = self.identify_job_level_hike()
        performance_hike = self.identify_performance_hike()
        hike = 0
        if job_level_hike != None:
            hike = job_level_hike
            if performance_hike != None:
                hike += performance_hike
            incentive = self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        return False
