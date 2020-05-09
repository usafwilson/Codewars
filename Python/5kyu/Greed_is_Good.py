# Greed is a dice game played with five six-sided dice.
# Your mission, should you choose to accept it, is to score a throw according to these rules.
# You will always be given an array with five six-sided dice values.

def score(dice):

    curr_score = 0

    if dice.count(1) == 3:
        curr_score += 1000
    elif dice.count(1) > 3:
        curr_score += 1000 + (100 * (dice.count(1) - 3))

    elif 0 < dice.count(1) < 3:
        curr_score += dice.count(1) * 100

    if dice.count(5) == 3:
        curr_score += 500
    elif dice.count(5) > 3:
        curr_score += 500 + (50 * (dice.count(5) - 3))

    elif 0 < dice.count(5) < 3:
        curr_score += dice.count(5) * 50

    if dice.count(6) >= 3:
        curr_score += 600
    if dice.count(4) >= 3:
        curr_score += 400
    if dice.count(3) >= 3:
        curr_score += 300
    if dice.count(2) >= 3:
        curr_score += 200

    return curr_score