"""

"FairyLand Multiplex" wants to automate ticket booking and seat allocation process.
Write a python program to implement the class diagram given below.



Assumptions:

1. Multiplex has two screens having different seating capacity

2. Two movies will be screened everyday (one show/movie)

3. Booking will be opened every day morning for that day’s shows

4. Movie name, total tickets available, ticket price and last seat number allocated for both movies are
   stored in lists having one to one correspondence. Details of first movie will be available at the 0th
   index and second movie at the 1st index of these lists

Method description:

1. check_seat_availability(movie_index,number_of_tickets): Checks seat availability for the given movie.
   Refer the code given in starter code
2. calculate_ticket_price(movie_index,number_of_tickets): Calculates total ticket price for the given movie.
   Refer the code given in starter code
3. generate_seat_number(movie_index,number_of_tickets): Allocate required number of seats for the given movie.
    1. Seat numbers should be auto-generated as mentioned below:
        1.Seat numbers should be generated starting from 1, prefixed by "M1-" for movie-1 and "M2-" for movie 2
        2. Examples movie-1: M1-1, M1-2, M1-3 etc, movie-2: M2-1,M2-2 etc
4. Update total number of tickets available for the given movie in list_total_tickets
5. Update last seat number allocated for the given movie in list_last_seat_number
6. Return the list of generated seat numbers
7. book_ticket(movie_name,number_of_tickets): Book tickets for the given movie.
8. Return 0, if movie name is invalid
9. Return -1, if enough tickets are not available for the given movie
10.Else,
    1. Generate seat numbers
    2. Initialize attribute, seat_numbers with the list of generated seat numbers
    3. Calculate total ticket price

Perform case sensitive string comparison.
"""


# lex_auth_012751902958862336276
class Multiplex:
    __list_movie_name = ["movie1", "movie2"]
    __list_total_tickets = [100, 60]
    __list_last_seat_number = ["M1-23", None]
    __list_ticket_price = [150, 200]

    def __init__(self):
        self.__seat_numbers = None
        self.__total_price = None

    def calculate_ticket_price(self, movie_index, number_of_tickets):
        self.__total_price = (
            Multiplex.__list_ticket_price[movie_index] * number_of_tickets
        )

    def check_seat_availability(self, movie_index, number_of_tickets):
        if Multiplex.__list_total_tickets[movie_index] < number_of_tickets:
            return False
        else:
            return True

    def get_total_price(self):
        return self.__total_price

    def get_seat_numbers(self):
        return self.__seat_numbers

    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name not in Multiplex.__list_movie_name:
            return 0
        index = Multiplex.__list_movie_name.index(movie_name)
        if not self.check_seat_availability(index, number_of_tickets):
            return -1
        else:
            self.__seat_numbers = self.generate_seat_number(index, number_of_tickets)
            self.calculate_ticket_price(index, number_of_tickets)

    def generate_seat_number(self, movie_index, number_of_tickets):
        seat_numbers = []
        if Multiplex.__list_last_seat_number[movie_index] == None:
            last_ticket = 0
        else:
            last_ticket = int(Multiplex.__list_last_seat_number[movie_index][3:])
        for i in range(1, number_of_tickets + 1):
            seat_numbers.append("M" + str(movie_index + 1) + "-" + str(i + last_ticket))
        Multiplex.__list_last_seat_number[movie_index] = seat_numbers[-1]
        Multiplex.__list_total_tickets[movie_index] -= number_of_tickets
        return seat_numbers


booking1 = Multiplex()
status = booking1.book_ticket("movie1", 10)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2 = Multiplex()
status = booking2.book_ticket("movie2", 6)
if status == 0:
    print("invalid movie name")
elif status == -1:
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())
