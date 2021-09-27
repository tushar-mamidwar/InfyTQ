"""
Problem Statement
In the Athlete class given below,

-make all the attributes private and
-add the necessary accessor and mutator methods

Represent Maria, the runner and make her run.
"""


# lex_auth_01275045546160947226
class Athlete:
    def __init__(self, name, gender):
        self.__name = None
        self.__gender = None

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def running(self):
        if (self.__gender == "girl"):
            print("150mtr running")
        else:
            print("200mtr running")


manas = Athlete()
Athlete__name = 'manas'
Athlete__gender = 'boy'
