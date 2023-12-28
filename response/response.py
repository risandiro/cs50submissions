import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(email):
    if validators.email(email) != True
        return "Valid"



if __name__ == "__main__":
    main()
