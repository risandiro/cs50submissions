def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
   if rule_three(s) == True:
        return True

# --------------------------------------

def rule_one(s):
     ftl = s[0:2]
     if ftl.isnumeric() == True:
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
    while counter != 0:

        counter += 1







main()
