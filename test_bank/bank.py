def main():
    x = input("Greeting: ")
    x = x.strip()

def value(greeting):
    if greeting.startswith("hello") or greeting.startswith("Hello"):
        return int(0)
    elif greeting.startswith("h") or greeting.startswith("H"):
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()

