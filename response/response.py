import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(email):
    return validators.email(email)

if __name__ == "__main__":
    main()
