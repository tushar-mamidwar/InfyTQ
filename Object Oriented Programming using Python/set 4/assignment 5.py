"""

"WonderLand" water theme park wants to generate tickets for its customers.
Complete the implementation of the requirement based on the given class diagram and code.


Class Description:
Theme Park class: Complete the class based on comments given in starter code

Ticket class: Complete the class based on comments given in starter code

Customer class:
1. Initialize points_earned, food_coupon and ticket to 0, "No" and a Ticket object respectively in the constructor
2. play_game():
    a. Calculate total points based on the list of games played by the customer
    b. Update attribute, points_earned with the calculated value
    c, ThemePark allows a free ride on Game 2 if the customer has opted for Game 3. If this is satisfied, add "Game2" to list_of_games and include its points to total points
3. update_food_coupon(): They provide food coupon to a customer who has opted Game 4 and has earned more than 15 points.
    a. Update attribute, food_coupon status to "Yes" if the above rule is satisfied
4. book_ticket():
    a. Calculate ticket amount
    b. If amount can be calculated, generate ticket id, play game, update food coupon and return true
    c. Else, return false
Note: Perform case sensitive string comparison

"""
# lex_auth_012753076922499072323
# This class represents ThemePark
class ThemePark:
    # dict_of_games contains the game name as key, price/ride and points that can be earned by customer in a list as value
    dict_of_games = {
        "Game1": [35.5, 5],
        "Game2": [40.0, 6],
        "Game3": [120.0, 10],
        "Game4": [60.0, 7],
        "Game5": [25.0, 4],
    }

    @staticmethod
    def validate_game(game_input):
        if game_input in ThemePark.dict_of_games:
            return True
        return False
        # Remove pass and write the logic here
        # If game_input is present in ThemePark, return true. Else, return false.

    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games[game_input][1]
        # Remove pass and write the logic here
        # Return the points that can be earned for the given game_input.

    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games[game_input][0]
        # Remove pass and write the logic here
        # Return the price/ride for the given game_input


# This class represents ticket
class Ticket:
    __ticket_count = 200

    def __init__(self):
        self.__ticket_id = None
        self.__ticket_amount = 0

    def generate_ticket_id(self):
        Ticket.__ticket_count += 1
        self.__ticket_id = Ticket.__ticket_count
        # Remove pass and write the logic here
        # Auto-generate ticket_id starting from 201

    def calculate_amount(self, list_of_games):
        for game in list_of_games:
            if not ThemePark.validate_game(game):
                self.__ticket_amount = 0
                return False
            self.__ticket_amount += ThemePark.get_amount(game)
        return True
        # Remove pass and write the logic here
        """Validate the games in the list_of_games.
        If all games are valid, calculate total ticket amount and assign it to attribute, ticket_amount and return true. Else, return false"""

    def get_ticket_id(self):
        return self.__ticket_id

    def get_ticket_amount(self):
        return self.__ticket_amount


class Customer:
    def __init__(self, name, list_of_games):
        self.__points_earned = 0
        self.__food_coupon = "No"
        self.__ticket = Ticket()
        self.__name = name
        self.__list_of_games = list_of_games

    def play_game(self):
        if "Game3" in self.__list_of_games:
            self.__list_of_games.append("Game2")
        for game in self.__list_of_games:
            self.__points_earned += ThemePark().get_points(game)

    def update_food_coupon(self):
        if "Game4" in self.__list_of_games and self.__points_earned > 15:
            self.__food_coupon = "yes"

    def book_ticket(self):
        if not self.__ticket.calculate_amount(self.__list_of_games):
            return False
        self.__ticket.generate_ticket_id()
        self.play_game()
        self.update_food_coupon()
        return True

    def get_food_coupon(self):
        return self.__food_coupon

    def get_ticket(self):
        return self.__ticket

    def get_list_of_games(self):
        return self.__list_of_games

    def get_name(self):
        return self.__name

    def get_points_earned(self):
        return self.__points_earned

    # Remove pass and implement class Customer here


"""Represent customers and display all details of the customer, if he is able to book the ticket and play the game. Else, display appropriate error message """
