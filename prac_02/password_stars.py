password_limit = 5

password_guess = input('Enter a password: ')

while len(password_guess) < password_limit:
    print(f"Password need to be more than {password_limit} characters long")
    password_guess = input('Enter a password: ')
for i in range(len(password_guess)):
    print('*', end="")