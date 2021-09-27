"""
TechWorld, a technology training center, wants to allocate courses for instructors.
An instructor is identified by name, technology skills, experience and average feedback.
An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes from the list of options below to represent instructors.

-check_eligibility()
-avg_feedback
-experience
-instructor_name
-allocate_course()
-allocate_course(technolody)
-__init__()
-Instructor
-calculate_avg_feedback()
-technology_skill

Write a Python program to implement the class chosen with its attributes and methods.

Note:

1. Consider all instance variables to be private and methods to be public
2. An instructor may have multiple technology skills, so consider instance variable,
   technology_skill to be a list
3. check_eligibility(): Return true if eligibility criteria is satisfied by the instructor.
   Else, return false
4. allocate_course(technology): Return true if the course which requires the given technology
   can be allocated to the instructor. Else, return false

Perform case sensitive string comparison
Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""


class Instructor:
    def __init__(self):
        self.__instructor_name = ""
        self.__experience = 0
        self.__avg_feedback = 0
        self.__technology_skill = []

    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill

    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def get_instructor_name(self):
        return self.__instructor_name

    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5 or self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        else:
            return False

    def allocate_course(self, technology):
        if technology in self.__technology_skill and self.check_eligibility():
            return True
        else:
            return False


instructor1 = Instructor()
instructor1._Instructor__instructor_name = 'demo1'
instructor1._Instructor__experience = 3
instructor1._Instructor__avg_feedback = 4.5
instructor1._Instructor__technology_skill = ["java", "python"]
print(instructor1.check_eligibility())
print(instructor1.allocate_course("java"))
