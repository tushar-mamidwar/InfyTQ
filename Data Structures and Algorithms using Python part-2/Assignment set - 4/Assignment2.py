# lex_auth_0127667391112806403379


def find_matches(country_name):
    # Remove pass and write your logic here
    output_list = []
    for match in match_list:
        i = 0
        length = len(country_name)
        if country_name == match[:length]:
            output_list.append(match)
    return output_list


def max_wins():
    max_dict = {}
    for match in match_list:
        championship_name = ""
        matches_won = ""
        count = 0
        for character in match:
            if character == ":":
                count += 1
                continue
            if count == 1:
                championship_name += character
            elif count == 3:
                matches_won += character
        if championship_name in max_dict:
            if max_dict[championship_name] <= matches_won:
                max_dict[championship_name] = matches_won
        else:
            max_dict[championship_name] = matches_won
    output_dict = {}
    for match in match_list:
        championship_name = ""
        matches_won = ""
        country_name = ""
        count = 0
        for character in match:
            if character == ":":
                count += 1
                continue
            if count == 0:
                country_name += character
            elif count == 1:
                championship_name += character
            elif count == 3:
                matches_won += character
        if matches_won == max_dict[championship_name]:
            if championship_name in output_dict:
                output_dict[championship_name].append(country_name)
            else:
                output_dict[championship_name] = [country_name]
    return output_dict


def find_winner(country1, country2):
    # Remove pass and write your logic here
    country1_list = find_matches(country1)
    country2_list = find_matches(country2)
    matches_won_country1 = 0
    matches_won_country2 = 0
    for match in country1_list:
        count = 0
        matches_won = ""
        for character in match:
            if character == ":":
                count += 1
            elif count == 3:
                matches_won += character
        matches_won_country1 += int(matches_won)
    for match in country2_list:
        count = 0
        matches_won = ""
        for character in match:
            if character == ":":
                count += 1
            elif count == 3:
                matches_won += character
        matches_won_country2 += int(matches_won)
    if matches_won_country1 > matches_won_country2:
        return country1
    elif matches_won_country2 > matches_won_country1:
        return country2
    else:
        return "Tie"


# Consider match_list to be a global variable
match_list = [
    "AUS:CHAM:5:2",
    "AUS:WOR:2:1",
    "ENG:WOR:2:0",
    "IND:T20:5:3",
    "IND:WOR:2:1",
    "PAK:WOR:2:0",
    "PAK:T20:5:1",
    "SA:WOR:2:0",
    "SA:CHAM:5:1",
    "SA:T20:5:0",
]

# Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print(find_matches("AUS"))
print(max_wins())
print(find_winner("AUS", "IND"))
