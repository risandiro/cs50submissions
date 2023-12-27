from validator_collection import validators

def main():
    print(validate(input("What's your email adress? ")))


def validate(email):
    email_address = validators.email(email)


if __name__ == "__main__":
    main()
