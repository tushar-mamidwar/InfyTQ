"""
Problem Statement
The central library at Mysore has a set of very interesting books and journals. The books are 
arranged in the alphabetical order of their author names. So it is very easy for the readers to search 
for the book.

The library has got a set of new books. The librarian wants to arrange them in order too. As some 
books are already arranged in the order, find a suitable way of arranging the new set of books amidst 
them.

Write a python program to arrange all the books in the alphabetical order of the author names.

sort_item_list_by_author(): Accepts the new list of books and returns it sorted in the alphabetical 
    order of their author names.

add_new_items(): Accepts the new list of books, sorts it and merges it with the existing books in the 
    library.
    Hint - Use sort_item_list_by_author() method for sorting the books.

sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of 
    their published years. If there are multiple items that are published in the same year, then sort 
    them based on the alphabetical order of their author names.

Note: While sorting the author names in alphabetical order, ignore the special characters including 
space, if there are any.
"""
# lex_auth_0127667335697694723476

# Implement Item class here


class Item:
    def __init__(self, item_name, author_name, published_year):
        self.__item_name = item_name
        self.__author_name = author_name
        self.__published_year = published_year

    def get_item_name(self):
        return self.__item_name

    def get_author_name(self):
        return self.__author_name

    def get_published_year(self):
        return self.__published_year

    def __str__(self):
        return (
            self.__item_name
            + "  "
            + self.__author_name
            + "  "
            + str(self.__published_year)
        )


# Implement Library class here


class Library:
    def __init__(self, item_list):
        self.__item_list = item_list

    def get_item_list(self):
        return self.__item_list

    def sort_item_list_by_author(self, new_item_list):
        for i in range(len(new_item_list)):
            author_name = new_item_list[i].get_author_name()
            high = len(author_name)
            k = 0
            author_name2 = ""
            while k < high:
                if author_name[k].isalnum():
                    author_name2 += author_name[k]
                k += 1
            min = author_name2.lower()
            min_index = i
            for j in range(i, len(new_item_list)):
                author_name = new_item_list[j].get_author_name()
                high = len(author_name)
                k = 0
                author_name2 = ""
                while k < high:
                    if author_name[k].isalnum():
                        author_name2 += author_name[k]
                    k += 1

                author_name2 = author_name2.lower()
                if author_name2 < min:
                    min = author_name2
                    min_index = j
            temp = new_item_list[i]
            new_item_list[i] = new_item_list[min_index]
            new_item_list[min_index] = temp
        return new_item_list

    def add_new_items(self, new_item_list):
        self.__item_list += new_item_list
        self.sort_item_list_by_author(self.__item_list)

    def sort_items_by_published_year(self):
        length = len(self.__item_list)
        for i in range(length):
            min = self.__item_list[i].get_published_year()
            min_index = i
            for j in range(i, length):
                if self.__item_list[j].get_published_year() < min:
                    min_index = j
                    min = self.__item_list[j].get_published_year()
            temp = self.__item_list[i]
            self.__item_list[i] = self.__item_list[min_index]
            self.__item_list[min_index] = temp
        i = 0
        high = length - 1
        temp_list = []
        sub_list = []
        while i <= high:
            sub_list = []
            repetition = False
            while (
                i < high
                and self.__item_list[i].get_published_year()
                == self.__item_list[i + 1].get_published_year()
            ):
                sub_list.append(self.__item_list[i])
                i += 1
                repetition = True
            sub_list.append(self.__item_list[i])
            i += 1
            if repetition:
                self.sort_item_list_by_author(sub_list)
            print("sub_list", sub_list)
            temp_list += sub_list
        self.__item_list = temp_list


# Use different values for item and test your program
item1 = Item("A Mission In Kashmir", "Andrew Whitehead", 1995)
item2 = Item("A Passage of India", "E.M.Forster", 2012)
item3 = Item("A new deal for Asia", "Mahathir Mohammad", 1999)
item4 = Item("A Voice of Freedom", "Nayantara Sehgal", 2001)
item5 = Item("A pair of blue eyes", "Thomas Hardy", 1998)

item_list = [item1, item2, item3, item4, item5]
library = Library(item_list)
print("The current items in the library are:")
for item in library.get_item_list():
    print(item)

item11 = Item("Broken Wing", "Sarojini Naidu!", 2012)
item12 = Item("Guide", "Joseph Smith", 2001)
item13 = Item("Indian Summers", "J@ohn Mathews", 2001)
item14 = Item("Innocent in Death", "J.D.Robb", 2010)
item15 = Item("Life of Pi", "Josephine", 2010)
item16 = Item("Sustainability", "Johny", 2016)
item17 = Item("Look Ahead", "E.M.Freddy", 2012)

new_item_list = [item11, item12, item13, item14, item15, item16, item17]
print()
print("The new items to be added are:")
for item in new_item_list:
    print(item)

new_item_list_sorted = library.sort_item_list_by_author(new_item_list)
print()
print("The new items after sorting based on the author name are:")
for item in new_item_list_sorted:
    print(item.get_author_name())

library.add_new_items(new_item_list_sorted)
print()
print("The final set of items after adding the new item list are:")
for item in library.get_item_list():
    print(item)

library.sort_items_by_published_year()
print()
print("The items sorted based on the increasing order of their published year:")
for item in library.get_item_list():
    print(item)
