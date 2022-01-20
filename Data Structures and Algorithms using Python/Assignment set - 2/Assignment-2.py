'''
The Montessari Public School has planned to organize a cultural evening. The Teacher has framed a schedule based on an idea given by the students.
Assume that the schedule is as below:

Name	  Rahul	    Sheema	   Gitu	       Tarun                Tom
Item	Solo Song	Dance	Plays Flute	  Gymnastics	        MIME
The teacher instructed the children to be ready by holding each other’s hands while standing on the stage and they have to come forward and perform when their turn comes. It is decided that Rahul would perform at the beginning and once again in the middle of the show. After Rahul’s first performance, he would join the other children, in his new position(after Gitu). After Rahul occupies the new position, Swetha would join the children at the end for delivering the vote of thanks.

Assume that there will always be odd number of children initially.

Use the Child class and children_list provided to implement the class Performance as given in the below class diagram.

1. In the constructor of Performance class, initialize children_list

2. Display the schedule

3. Change Rahul’s position after his performance and display the updated schedule

4. Add Swetha and display the updated schedule

__init__(children_list)         Initializes the children list

change_position(child)          Used to change the position of the child passed as the argument to 
                                the middle position

add_new_child(child)	        Used for adding a new child passed as the argument to the end of 
                                the schedule
'''
#lex_auth_0127438667235000321614

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
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        if self.__head.get_data()==data:
            if self.__head==self.__tail:
                self.__tail=None
                self.__head=None
            else:
                self.__head=self.__head.get_next()
        else:
            temp=self.__head
            node_before=None
            while(temp.get_data()!=data):
                node_before=temp
                temp=temp.get_next()
            node_before.set_next(temp.get_next())
            if self.__tail==temp:
                self.__tail=node_before

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
        
class Child:
    def __init__(self,name,item_to_perform):
        self.__name=name
        self.__item_to_perform=item_to_perform

    def __str__(self):
        return(self.__name+" "+self.__item_to_perform)

    def get_name(self):
        return self.__name

    def get_item_to_perform(self):
        return self.__item_to_perform


#Implement Performance class here
class Performance:
    def __init__(self,children_list):
        self.__children_list=children_list
    def change_position(self,child):
        temp=self.__children_list.get_head()
        temp1=self.__children_list.get_head()
        self.__children_list.delete(child)
        while(temp.get_next()!=None):
            temp1=temp1.get_next()
            temp=temp.get_next().get_next()
        self.__children_list.insert(child,temp1.get_data())
    def add_new_child(self,child):
        self.__children_list.add(child)
    def get_children_list(self):
        return self.__children_list
        
child1=Child("Rahul","solo song")
child2=Child("Sheema","Dance")
child3=Child("Gitu","Plays Flute")
child4=Child("Tarun","Gymnastics")
child5=Child("Tom","MIME")
#Add different values to the list and test the program
children_list=LinkedList()
children_list.add(child1)
children_list.add(child2)
children_list.add(child3)
children_list.add(child4)
children_list.add(child5)
performance=Performance(children_list)
print("The order in which the children would perform:")
performance.get_children_list().display()
print()
print("After Rahul's performance, the schedule would change to:")
performance.change_position(child1)
performance.get_children_list().display()
print()
child6=Child("Swetha","Vote of Thanks")
print("After Swetha has joined, the schedule is:")
performance.add_new_child(child6)
performance.get_children_list().display()