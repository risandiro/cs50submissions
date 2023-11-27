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
     ftl = s[0:2]
     if ftl.isnumeric():
        return False
     else:
         return True


def rule_two(s):
    number_of_characters = len(s)
    if 2 <= number_of_characters <= 6:
        return True
    else:
        return False


def rule_three(s):
    counter = 0
    for char in s:
        if char.isnumeric():
            break
        counter += 1

    if counter <= 2:
        afd = s[counter:len(s)]
        if afd.isnumeric():
            return True
        else:
          return False
    else:
        return True


def rule_four(s):
    if any(char in string.punctuation for char in s):
        return False
    else:
        return True

# --------------------------------------

main()
