"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
else:
    if score < 50:
        score_status = "Bad"
    elif score < 90:
        score_status = "Passable"
    else:
        score_status = "Excellent"

    print(f"{score}% is a {score_status} score")
