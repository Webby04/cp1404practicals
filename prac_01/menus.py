"""
CP1404/CP5632 - Practical
This program prompts the user for their name and allows them to greet or say goodbye
using a menu until they choose to quit
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = (input("Enter name: "))
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")

