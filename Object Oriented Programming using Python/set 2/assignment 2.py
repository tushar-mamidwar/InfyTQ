"""
Problem Statement
A telecom company wants to generate reports on the call details of the customers.
The data of each call detail include the phone number which made the call, phone number which was
called, duration of the call and the type of call. Data of such calls are provided as a list of
comma separated string.

Problem Statement:

    -Complete the CallDetail class with necessary attributes
    -Complete the logic inside the parse_customer() method of the Util Class. This method should
     accepta list of string of the call details and convert it into a list of CallDetail object
     and assign this list as a value to the attribute of the Util class.
"""
#lex_auth_012727085763518464103
#Start writing your code here
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for call_detail in list_of_call_string:
            call_detail=call_detail.split(',')
            call=CallDetail(call_detail[0],call_detail[1],call_detail[2],call_detail[3])
            self.list_of_call_objects.append(call)
        print(self.list_of_call_objects)
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)