def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    MIN_PASSWORD_LENGTH = 8

    while True:
        password = input("Enter a password: ")
        if len(password) < MIN_PASSWORD_LENGTH:
            print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long!")
        else:
            return password


main()
