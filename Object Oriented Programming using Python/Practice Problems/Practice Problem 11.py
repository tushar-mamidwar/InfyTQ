"""
Problem Statement
The consultants of WeHire Company help students to get placements in companies registered with it.
There are multiple companies registered in WeHire. Students are registered for placement based
their on choice of company and vacancies available in those companies.

Write a python program to implement the class diagram given below.

Class description:
Consultant class:
    1. registered_company_list: List containing names of registered companies
    2. vacancy_list: List containing number of vacancies in registered companies. There is one to
       one correspondence between the two lists
    3. registered_student_dict: Dictionary which stores the company name as key and list of ids of
       students who have registered with that company as value.
    4. validate_vacancy(company_name): Check for vacancy in the given company. If available, return
       the index position of the company in registered_company_list. Else, return -1
    5. register_student_for_placement(index,student_id): Register the given student id in the company
       whose index position is passed to the method.
         a. Update vacancy_list of the company
         b. Update registered_student_dict so as to add the given student id to the student list of the company

Student class:
    1. check_eligibility(): The students can register for a company only they have minimum aggregate
       percentage of 65 and their year of passing is 2015.
         - If the above two conditions are satisfied, return true. Else return false.
    2.  apply_for_job(company_name,consultant): Apply for job in the given company through the given consultant.
        a. Check if vacancy is available in the given company. (Hint: Invoke consultant.validate_vacancy())
        b. If available, check if the student is eligible
            - If eligible, register the student for placement by invoking appropriate method of consultant
            - Else return -1
        c. Else return -1

Create objects of Student and Consultant class, invoke appropriate methods and test your program.
"""


class Consultant:
    def __init__(
        self, name, registered_company_list, vacancy_list, registered_student_dict
    ):
        self.__name = name
        self.__registered_company_list = registered_company_list
        self.__vacancy_list = vacancy_list
        self.__registered_student_dict = registered_student_dict

    def get_name(self):
        return self.__name

    def get_registered_company_list(self):
        return self.__registered_company_list

    def get_registered_student_dict(self):
        return self.__registered_student_dict

    def get_vacancy_list(self):
        return self.__vacancy_list

    def validate_vacancy(self, company_name):
        if company_name in self.__registered_company_list:
            index = self.__registered_company_list.index(company_name)
            if self.__vacancy_list[index] > 0:
                return index
        return -1

    def register_student_for_placement(self, index, student_id):
        self.__vacancy_list[index] -= 1
        self.__registered_student_dict[self.__registered_company_list[index]].append(
            student_id
        )


class Student:
    def __init__(self, name, student_id, branch, aggregate_percentage, year_of_passing):
        self.__name = name
        self.__student_id = student_id
        self.__branch = branch
        self.__aggregate_percentage = aggregate_percentage
        self.__year_of_passing = year_of_passing

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_branch(self):
        return self.__branch

    def get_aggregate_percentage(self):
        return self.__aggregate_percentage

    def get_year_of_passing(self):
        return self.__year_of_passing

    def check_eligibility(self):
        if self.__aggregate_percentage >= 65 and self.__year_of_passing == 2015:
            return True
        return False

    def apply_for_job(self, company_name, consultant):
        index = consultant.validate_vacancy(company_name)
        if index != -1 and self.check_eligibility():
            consultant.register_student_for_placement(index, self.__student_id)
        else:
            return -1


consultant = Consultant(
    "Consultant1",
    ["TCS", "Infosys", "Campegini", "Accenture"],
    [5, 4, 6, 0],
    {"TCS": [], "Infosys": [], "Campegini": [], "Accenture": []},
)

student = Student("Student1", 1234, "CS", 78, 2015)
print(student.apply_for_job("TCS", consultant))
print(consultant.get_registered_student_dict())
