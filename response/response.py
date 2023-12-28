import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    if validators.email(s) != True: return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()
