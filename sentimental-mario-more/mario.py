def main():
    while True:
        try:
            height = int(input("Height: "))
            if 0 < height <= 8:
                break
            raise
        except:
            print("Enter a number between 1 and 8 inclusive")

