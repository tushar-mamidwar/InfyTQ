"""
Continuing with the previous scenario, a student eligible for admission has to choose a course and pay the fees for it. If they have scored more than 85 marks in qualifying exam, they get 25% discount on fees.

Valid course ids and fees are given below:

course id                       fees

   1001                        25575.0

   1002                        15500.0

Extend the program written in the previous assignment to include the above requirement.

Instance variables and methods to be included in Student class are given below.

Class name: Student

Attributes                course_id
(private)                    fees



Methods                  __init__()                 Create and initialize newly created instance variables also to None
(public)

                    choose_course(course_id)        Accept the course_id chosen by the student.

                                                        -If course_id is valid,
                                                        -set attributes course_id and fees
                                                        -if marks is more than 85, apply 25% discount on fees
                                                    return true
                                                    Else, return false

                        getter methods              Include getter methods for newly added instance variables

"""


class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None

    def validate_marks(self):
        if 0 <= self.__marks and self.__marks <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.__marks >= 65:
            return True
        else:
            return False

    def choose_course(self, course_id):
        if course_id == 1001:
            self.__course_id = course_id
            self.__fees = 25575
            if self.__marks > 85:
                self.__fees *= 0.75
            return True
        elif course_id == 1002:
            self.__course_id = course_id
            self.__fees = 15500
            if self.__marks > 85:
                self.__fees *= 0.75
            return True
        return False

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees


maddy = Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(65)
if (maddy.check_qualification()):
    print("Student has qualified")
    if (maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
