"""
Problem Statement

Write a python program to find out if a given classroom is present in the left wing of a university building. Implement the class, Classroom given below.


Method/Attribute description:

1. classroom_list: Static list which store the name of the class rooms in the left wing
2. search_classroom(class_room): Static method which search for the given class room in the
   classroom_list. If found, return "Found". Else, return -1
Note: Perform case insensitive string comparison

For testing:

- Invoke search_classroom(class_room) static method on class, Classroom by passing the name of the
  class room to be searched

- Display appropriate message based on the return value of search_classroom(class_room)
"""


class Classroom:
    classroom_list = ["a", "b", "c", "d"]

    @staticmethod
    def search_classroom(class_room):
        for classroom in Classroom.classroom_list:
            if classroom.lower() == class_room.lower():
                return "FOUND"
        return -1


x = Classroom()
if Classroom.search_classroom("a") == "FOUND":
    print("Classroon found in left wing")
else:
    print("Classroom not found in left wing")
