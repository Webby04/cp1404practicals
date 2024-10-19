"""
Word Occurrences
Estimate: 22 minutes
Actual:   25 minutes
"""

def main():
    """Gathers user emails and names until blank, then displays results"""
    user_emails = {}
    email_input = input("Email: ")
    while email_input != "":
        name = extract_name(email_input)
        review = input(f"Is your name {name}? (Y/n) ").upper()
        if review not in "Y" and review not in "":
            name = input("Name: ")
        user_emails[email_input] = name
        email_input = input("Email: ")


def extract_name(email):
    pass


main()
