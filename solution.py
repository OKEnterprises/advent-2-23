""" This module contains functions related to parsing text input and
evaluting it according to cube game rules. """

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def parse_turn(turn):
    """ This function returns a parsed score dict based on a text representation. """
    scores = map(str.strip, turn.split(","))

    scores_dict = {
        "red":0,
        "green":0,
        "blue":0
    }

    for score in scores:
        num, color = score.split(" ")
        if color == 'red':
            scores_dict['red'] = int(num)
        elif color == 'green':
            scores_dict['green'] = int(num)
        elif color == 'blue':
            scores_dict['blue'] = int(num)

    return scores_dict

def validate_turn(scores):
    """ This function returns True if a score dict is possible, False otherwise. """
    return (scores['red'] <= MAX_RED
            and scores['green'] <= MAX_GREEN
            and scores['blue'] <= MAX_BLUE)

def parse_line(line):
    """ This function parses and validates a line, returning the game ID if the game is valid, 
    0 otherwise. """
    head, tail = line.split(":")
    game_id = int(head[5:])
    turns = map(str.strip, tail.strip().split(";"))
    valid = True

    for turn in turns:
        scores = parse_turn(turn)
        if not validate_turn(scores):
            valid = False
            break

    return game_id if valid else 0

with open('advent-2-23/input.txt', 'r', encoding='utf-8') as f:
    sum_ids = sum(parse_line(line) for line in f)
    print(sum_ids)
