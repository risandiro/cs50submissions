def main():
    x = input("Greeting: ")
    cash = value(x)
    print(f"${cash}")


def value(greeting):
    if greeting.lower().startswith("hello"):
        return int(0)
    elif greeting.lower().startswith("h"):
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()

