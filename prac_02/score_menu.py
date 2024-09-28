""" Complete program, following structure
menu:
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = get_valid_score()
    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("> ").upper()
    print("Farewell! :)")


def get_valid_score():
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter a valid score (0-100): "))
    return score


def print_result(score):
    result = determine_result(score)
    print(f"{score:.2f}% is a {result} score")


def determine_result(score):
    if score < 50:
        return "bad"
    elif score < 90:
        return "passable"
    else:
        return "excellent"


def show_stars(score):
    print('*' * score)


main()
