class Queue:
    def __init__(self, max_size):

        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append((str)(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before == None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() == None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


# Start writing your solution here
class Train:
    def __init__(
        self,
        train_name,
        source,
        destination,
        passenger_capacity_per_compartment,
        passenger_goods_ratio,
    ):
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__passenger_capacity_per_compartment = passenger_capacity_per_compartment
        self.__passenger_goods_ratio = passenger_goods_ratio
        self.__compartment_list = LinkedList()
        self.count = 0

    def get_train_name(self):
        return self.__train_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_passenger_capacity_per_compartment(self):
        return self.__passenger_capacity_per_compartment

    def get_passenger_goods_ratio(self):
        return self.__passenger_goods_ratio

    def get_compartment_list(self):
        return self.__compartment_list

    def add_passenger_compartments(self, no_of_passengers):
        while no_of_passengers >= self.__passenger_capacity_per_compartment:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count),
                self.__passenger_capacity_per_compartment,
                0,
            )
            no_of_passengers -= self.__passenger_capacity_per_compartment
            self.count += 1
            self.__compartment_list.add(new_compartment)
        if no_of_passengers != 0:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count), no_of_passengers, 0
            )
            self.count += 1
            self.__compartment_list.add(new_compartment)

    def add_goods(self, goods_list):
        total_goods = 0
        while not goods_list.is_empty():
            total_goods += goods_list.dequeue().get_quantity()
        goods_capacity = (
            self.__passenger_capacity_per_compartment // self.__passenger_goods_ratio
        )
        last_compartment = self.__compartment_list.get_tail().get_data()
        no_of_goods_vacant = (
            self.__passenger_capacity_per_compartment
            - last_compartment.get_no_of_passengers()
        ) // self.__passenger_goods_ratio
        if no_of_goods_vacant != 0:
            if no_of_goods_vacant <= total_goods:
                total_goods -= no_of_goods_vacant
                last_compartment.set_no_of_goods(no_of_goods_vacant)
            else:
                last_compartment.set_no_of_goods(total_goods)
                total_goods = 0
        while total_goods >= goods_capacity:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count), 0, goods_capacity
            )
            total_goods -= goods_capacity
            self.count += 1
            self.__compartment_list.add(new_compartment)
        if total_goods != 0:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count), 0, total_goods
            )
            self.count += 1
            self.__compartment_list.add(new_compartment)

    def __str__(self):
        pass


class Compartment:
    def __init__(self, name, no_of_passengers, no_of_goods):
        self.__name = name
        self.__no_of_passengers = no_of_passengers
        self.__no_of_goods = no_of_goods

    def get_name(self):
        return self.__name

    def get_no_of_passengers(self):
        return self.__no_of_passengers

    def get_no_of_goods(self):
        return self.__no_of_goods

    def set_no_of_goods(self, goods):
        self.__no_of_goods = goods

    def __str__(self):
        return self.__name+'  '+str(self.__no_of_passengers)+'  '+str(self.__no_of_goods)


class Goods:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        return self.__product + ":" + str(self.__quantity)
class TrainService:
    @staticmethod
    def transfer_goods(train1,train2):
        compartment_list=train1.get_compartment_list()
        temp=compartment_list.get_head()
        capacity=train2.get_passenger_capacity_per_compartment()//train2.get_passenger_goods_ratio()
        while temp.get_data().get_no_of_passengers()!=0:
            temp=temp.get_next()
        while temp!=None:
            train2.get_compartment_list().add(temp.get_data())
            temp=temp.get_next()
        # total_goods=0
        # while temp!=None:
        #     compartment_list.delete(temp.get_data())
        #     total_goods+=temp.get_data().get_no_of_goods()
        #     temp=temp.get_next()
        # while total_goods>=capacity:
        #     new_comartment=Compartment(train2.get_train_name()[0]+str(train2.count),0,capacity)
        #     total_goods-=capacity
        #     train2.count+=1
        #     train2.get_compartment_list().add(new_comartment)
        # if total_goods!=0:
        #     new_comartment=Compartment(train2.get_train_name()[0]+str(train2.count),0,total_goods)
        #     train2.count+=1
        #     train2.get_compartment_list().add(new_comartment)


goods_list=Queue(4)
fridge=Goods('Fridge',26)
sofaset=Goods('Sofaset',5)
table=Goods('Table',23)
chairs=Goods('Chairs',45)

goods_list.enqueue(fridge)
goods_list.enqueue(sofaset)
goods_list.enqueue(table)
goods_list.enqueue(chairs)

train1=Train('Lokmanya','Bangalore','Mumbai',60,5)
train2=Train('Rajdhani','Mumbai','Chandigarh',75,5)

train1.add_passenger_compartments(455)
train2.add_passenger_compartments(5)

train1.add_goods(goods_list)

compartment_list=train1.get_compartment_list()
compartment_list.display()

train_service=TrainService()
train_service.transfer_goods(train1,train2)
compartment_list_train2=train2.get_compartment_list()
compartment_list=train1.get_compartment_list()
compartment_list.display()
print()
compartment_list_train2.display()