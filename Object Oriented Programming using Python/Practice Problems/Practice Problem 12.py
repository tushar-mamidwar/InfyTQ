"""
Problem Statement
A post office wants to automate the process of allocation of letters to different postmen based on
their allocated area.

Write a python program to implement the class diagram given below.


Class description
Letter class:
    1. Initialize static variable counter to 1
    2. Auto-generate attribute, letter_id starting from 1 in the constructor

PostMan class:
    1. Initialize static variable counter to 100
    2. Auto-generate attribute, postman_id starting from 101 prefixed by “P” in the constructor
    3. post_list_to_deliver: List of letter objects to be delivered by the postman

PostOffice class:
    1. area_list: List of names of areas under the post office
    2. postmen_list: List of postman objects working in the post office. There is one to one correspondence
       between the two lists – which means postman at index position 0 delivers letters in the area
       at index position 0 of area_list
    3. validate_letter(letter): Accept the letter and validate its receiver area. If letter.receiver_area
       is present in area_list, return the index position of that area in area_list. Else return -1
    4. allocate_posts(letter_list): Allocate letters in the letter_list to the appropraie postman
        a. For every letter in letter_list
            - Validate letter.receiver_area
            - If valid, append the letter to the corresponding postman's post_list_to_deliver
            - Else, add it to an invalid letter list
        b. Return invalid letter list

Perform case sensitive comparison.

Create objects of Letter class, PostMan class and PostOffice class, invoke appropriate methods and test
your program.
"""


class Letter:
    counter = 1

    def __init__(self, receiver_area, sender_area):
        self.letter_id = Letter.counter
        Letter.counter += 1
        self.__receiver_area = receiver_area
        self.__sender_area = sender_area

    def get_receiver_area(self):
        return self.__receiver_area

    def get_sender_area(self):
        return self.__sender_area


class PostMan:
    counter = 100

    def __init__(self, name):
        PostMan.counter += 1
        self.__name = name
        self.postman_id = 'P' + str(PostMan.counter)
        self.__post_list_to_deliver = []

    def get_post_list_to_deliver(self):
        return self.__post_list_to_deliver

    def get_name(self):
        return self.__name


class PostOffice:
    def __init__(self, area_list, postmen_list):
        self.__area_list = area_list
        self.__postmen_list = postmen_list

    def validate_letter(self, letter):
        if letter.get_receiver_area() in self.__area_list:
            return self.__area_list.index(letter.get_receiver_area())
        return -1

    def allocate_posts(self, letter_list):
        invalid_letter_list = []
        for letter in letter_list:
            index = self.validate_letter(letter)
            if index != -1:
                self.__postmen_list[index]._PostMan__post_list_to_deliver.append(letter)
            else:
                invalid_letter_list.append(letter)

        return invalid_letter_list

    def get_area_list(self):
        return self.__area_list

    def get_postmen_list(self):
        return self.__postmen_list


letter1 = Letter("sector1", "sector1")
letter2 = Letter("sector2", "sector1")
letter3 = Letter("sector10", "sector1")
letter4 = Letter("sector3", "sector1")
letter5 = Letter("sector1", "sector1")
postman1 = PostMan("name1")
postman2 = PostMan("name2")
postman3 = PostMan("name3")
postoffice = PostOffice(["sector1", "sector2", "sector3"], [postman1, postman2, postman3])
postoffice.allocate_posts([letter1, letter2, letter3, letter4, letter5])
print(postman1.get_post_list_to_deliver())
print(postman2.get_post_list_to_deliver())
print(postman3.get_post_list_to_deliver())
