from datetime import date

def main():


def get_input():
    try:
        date = input("Date of Birth:" )
        day, month, year = date.split("-")
        print(day)



if __name__ == "__main__":
    main()
