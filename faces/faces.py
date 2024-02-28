def main():
    print(convert(input()))

def convert(s) -> str:
    value = str(s).replace(":)", "🙂")
    value.replace(":(", "🙁")
    return value

if __name__ == "__main__":
    main()
