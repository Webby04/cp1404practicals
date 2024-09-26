def main():
    password_limit = 5

    password_guess = get_password(password_limit)
    convert_password_to_asterisk(password_guess)


def convert_password_to_asterisk(password_guess):
    for i in range(len(password_guess)):
        print('*', end="")


def get_password(password_limit):
    password_guess = input('Enter a password: ')
    while len(password_guess) < password_limit:
        print(f"Password need to be more than {password_limit} characters long")
        password_guess = input('Enter a password: ')
    return password_guess


main()
