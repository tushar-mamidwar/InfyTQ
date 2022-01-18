'''
Problem Statement
Add a method, add(data) to the LinkedList class to add a new element to the end of the linked 
list as shown in the class diagram. Once done, represent Maria’s new list of items as a linked 
list and add the following items to the linked list:
    Sugar, Tea Bags, Milk and Biscuit 

- Modify the program to add a new method, display() which traverses through the linked list and 
  display the data in each node.
- Once done, display the items in Maria’s list.
'''
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        if self.__head==self.__tail==None:
            temp=Node(data)
            self.__head=temp
            self.__tail=temp
        else:
            temp=Node(data)
            self.__tail.set_next(temp)
            self.__tail=temp
        
        #Remove pass and write the logic to add an element
    def display(self):
        temp=self.__head
        while temp.get_next()!=None:
            print(temp.get_data())
            temp=temp.get_next()
        #Remove pass and write the logic to display the elements
    
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

list1=LinkedList()
list1.add("Sugar")
print("Element added successfully")
#Similarly add all the specified element(s)
list1.add('tea bags')
list1.add('milk')
list1.add('biscuits')
list1.display()
print(list1)