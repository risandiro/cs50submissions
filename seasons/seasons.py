import sys
from datetime import date

def main():
    get_input()

def get_input():
    try:
        date = input("Date of Birth: ")
        day, month, year = date.split("-")
        print(day)
        
    except ValueError:
        sys.exit()



if __name__ == "__main__":
    main()
