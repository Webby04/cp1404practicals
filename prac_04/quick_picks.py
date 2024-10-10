import random

NUMBER_OF_COLUMNS = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    values = []

    number_of_rows = int(input("How many quick picks? "))
    for i in range(number_of_rows):
        current_column = []
        for j in range(NUMBER_OF_COLUMNS):
            number = (random.randint(MINIMUM, MAXIMUM))
            while number in current_column:
                number = (random.randint(MINIMUM, MAXIMUM))
            current_column.append(number)
        values.append(current_column)
        sorted_columns = sorted(current_column)
        print(" ".join(f"{numbers:2}" for numbers in sorted_columns))


main()
