import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if rule_one(s) != True:
        return False
    elif rule_two(s) != True:
        return False
    elif rule_three(s) != True:
        return False
    elif rule_four(s) != True:
        return False
    else:
        return True

# --------------------------------------

def rule_one(s):
    try:
        if s[0].isnumeric() or s[1].isnumeric():
            return False
        else:
            return True
    except IndexError:
        return False


def rule_two(s):
    if 1 < len(s) < 7:
        return True
    else:
        return False


def rule_three(s):
    counter = 0
    for char in range(len(s)):
        if counter != 1:
            if s[char].isnumeric():
                if s[char] == "0":
                    return False
                counter += 1
                continue
        if counter == 1:
            if s[char].isnumeric() == False:
                return False
    return True


def rule_four(s):
    if any(char in string.punctuation for char in s):
        
        return False
    else:
        return True

# --------------------------------------

if __name__ == "__main__":
    main()
