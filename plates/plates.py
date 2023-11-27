def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
   if rule_two(s) == True:
        return True







def rule_one(s):
     ftl = s[0:2]
     if ftl.isnumeric() == True:
        return False
     else:
         return True

def rule_two(s):
    counter = 0
    for letter in s:
        if letter.isnumeric() == False:
            counter += 1
    if counter <= 2:
        return False
    else:
        return True





main()
