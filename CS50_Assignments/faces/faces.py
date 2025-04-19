def main():
    print(convert(input()))

def convert(s) -> str:
    value = str(s).replace(":)", "🙂")
    return value.replace(":(", "🙁")

if __name__ == "__main__":
    main()
