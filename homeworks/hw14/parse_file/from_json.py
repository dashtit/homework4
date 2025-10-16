import json


def get_club_with_most_wins(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        clubs = json.load(file)
    clubs_wins = []
    for club in clubs:
        clubs_wins.append(club['wins'])
    winners = []
    for club in clubs:
        if club['wins'] == max(clubs_wins):
            winners.append(club)
    return winners
