import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(email):
    try:
        return validators.email(email)
    except ValidationError


if __name__ == "__main__":
    main()
