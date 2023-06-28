"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = 'Fin.'  # Change this line!


def final_strategy(score, opponent_score):
    return 0 if abs((score+10-opponent_score%10+opponent_score//10)%10-opponent_score%10)==opponent_score//10 and opponent_score>=score+10-opponent_score%10+opponent_score//10 else 2 if abs((score+10-opponent_score%10+opponent_score//10)%10-opponent_score%10)==opponent_score//10 and opponent_score<=score+10-opponent_score%10+opponent_score//10 else 0 if 10-opponent_score%10+opponent_score//10>=6 else 2