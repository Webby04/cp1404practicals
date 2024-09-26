MENU = ("1. Show the even numbers from x to y\n"
        "2. Show the odd numbers from x to y\n"
        "3. Show the squares of the numbers from x to y\n"
        "4. Exit the program")


def main():
    print("Welcome to the Number Sequence Program!")
    x = int(input("Enter the starting number (x): "))
    y = int(input("Enter the ending number (y): "))

    print(MENU)
    choice = int(input("Please choose an option (1-4): "))
    while choice != 4:
        if choice == 1:
            even_numbers(x, y)
        elif choice == 2:
            odd_numbers(x, y)
        elif choice == 3:
            square_numbers(x, y)
        else:
            print("Invalid choice. Please select a valid option.")
        print(MENU)
        choice = int(input("Please choose an option (1-4): "))
    print("Exiting the program. Goodbye!")


def even_numbers(x, y):
    print("Even numbers from", x, "to", y, "are:")
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def odd_numbers(x, y):
    print("Odd numbers from", x, "to", y, "are:")
    for i in range(x, y + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def square_numbers(x, y):
    print("Squares of the numbers from", x, "to", y, "are:")
    for i in range(x, y + 1):
        print(i ** 2, end=" ")
    print()


main()
