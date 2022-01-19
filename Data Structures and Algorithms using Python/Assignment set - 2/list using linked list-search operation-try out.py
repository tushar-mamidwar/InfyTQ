'''
Modify the program to add a new method, find_node(data) to find a node with the given 
data in the linked list as shown in the class diagram. If found, the method should 
return the node, otherwise, it should return None.

Once done, invoke the method to find out whether the below mentioned items are present 
in Maria’s list or not:
    Milk, Salt, Biscuit, Apple Juice, Pomegranate, Watermelon

Note: Use the program written earlier for including display() method and enhance it for 
      the above requirement.
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
        #Remove pass and copy the code you had written to add an element.
        temp=Node(data)
        if self.__head==self.__tail==None:
            self.__head=temp
            self.__tail=temp
        else:
            
            self.__tail.set_next(temp)
            self.__tail=temp
    
    def display(self):
        temp=self.__head
        while(temp!=None):
            print(temp.get_data())
            temp=temp.get_next()
    
    def find_node(self,data):
        temp=self.__head
        while(temp!=None):
            if temp.get_data()==data:
                return temp
            temp=temp.get_next()
        return None
                                            
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
#Add all the required element(s)
list1.add('Milk')
list1.add('Salt')
list1.add('Biscuits')
list1.add('Apple juice')
list1.add('Sugar')
#Search for the required node
node=list1.find_node("Sugar")
if(node!=None):
    print("Node found")
else:
    print("Node not found") 
list1.display()