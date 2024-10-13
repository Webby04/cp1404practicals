"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load subject details from a file and display it in a formatted output."""
    data = load_data()
    display_subject_details(data)


def display_subject_details(data):
    """Display subject details in the required format"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} subjects")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


main()