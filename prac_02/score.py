"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    score = float(input("Enter score: "))
    result = score_status(score)
    random_number = random.randint(0, 100)
    random_result = score_status(random_number)
    print(f"{score:.2f}% is a {result} score")
    print(f"Random Score: {random_number:.2f}% is a {random_result} score")

def score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score < 50:
            return "Bad"
        elif score < 90:
            return "Passable"
        else:
            return "Excellent"

main()
