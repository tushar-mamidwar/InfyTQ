"""
Little Puppy Kennel sells dogs of different breeds. They want to automate their selling process.
Write a python program to implement the class diagram given below.

Class Description:
    1. dog_breed_dict: Static dictionary which contains the breed of the dog as key and the number of
    dogs available as value. Initialize it with the sample data given.

        Breed               Labrador Retriever          German Shepard              Beagle
    Number of Dogs                  5                         12                      10

    2. Initialize static variable counter to 100
    3. breed_list: List of dog breeds required by the customer. Initialize it in the constructor
    4. dog_id_list: List of dog ids. Initialize it to an empty list in the constructor
    5. price: Total price to be paid by the customer. Initialize it to 0 in the constructor
    6. accessories_required: Boolean value – True indicated accessories are required and False indicated accessories are not required.                          Initialize it in the constructor
    7. validate_breed(): Return true if all the breeds required by the customer are available. Else return false
    8. validate_quantity(): Return true if one dog/breed is available for all the breeds requested by the customer. Else return false
    9. generate_dog_id(breed): Accept the breed of the dog for which dog id should be generated.                                                                                Auto-generate dog id starting from 101 prefixed by the first character of the breed
    10, get_dog_price(breed): Return the price of the dog whose breed is passed to the method
    11. calculate_total_price(): Calculate the total price of all the dogs required by the customer.
        a. Validate breed and quantity of all the dogs required by the customer
        b. If valid,
            a. For every breed in breed_list,
                a. Update quantity in dog_breed_dict
                b. Auto-generate dog id and append it to attribute, dog_id_list
                c. Add price to attribute, price
            b. If accessories are required, add 350 to attribute, price
            c. If price is more than 1500, provide 5% discount on price
        c. If any breed is not available, return -1
        d. If quantity is not available for any breed, return -2

                        Breed                       Price
                  Labrador Retriever                 800
                   German Shepherd                   1230
                        Beagle                       650

Perform case sensitive string comparison

For testing:

- Create objects of Dog class
- Invoke calculate_total_price() on Dog objects
- Display the details

"""


class Dog:
    counter = 100
    dog_breed_dict = {"Labrador Retriever": 5, "German Shepherd": 12, "Beagle": 10}

    def __init__(self, breed_list, accessories_required):
        self.__dog_id_list = []
        self.__breed_list = breed_list
        self.__accessories_required = accessories_required
        self.__price = 0

    def get_dog_id_list(self):
        return self.__dog_id_list

    def get_breed_list(self):
        return self.__breed_list

    def get_price(self):
        return self.__price

    def get_accessories_required(self):
        return self.__accessories_required

    def get_dog_price(self, breed):
        price_dict = {"Labrador Retriever": 800, "German Shepherd": 1230, "Beagle": 650}
        return price_dict[breed]

    def generate_dog_id(self, breed):
        Dog.counter += 1
        return breed[0] + str(Dog.counter)

    def validate_breed(self):
        for each_breed in self.__breed_list:
            if not each_breed in Dog.dog_breed_dict:
                return False
        return True

    def validate_quantity(self):
        for each_breed in self.__breed_list:
            if not Dog.dog_breed_dict[each_breed]:
                return False
        return True

    def calculate_total_price(self):
        if self.validate_breed():
            if self.validate_quantity():
                for each_dog in self.__breed_list:
                    Dog.dog_breed_dict[each_dog] -= 1
                    self.__dog_id_list.append(self.generate_dog_id(each_dog))
                    self.__price += self.get_dog_price(each_dog)
                if self.__accessories_required:
                    self.__price += 350
                if self.__price > 1500:
                    self.__price *= 0.95
                return
            return -2
        return -1


dog = Dog(["Labrador Retriever", "Beagle"], True)
print(dog.calculate_total_price())
print(dog.get_price())
