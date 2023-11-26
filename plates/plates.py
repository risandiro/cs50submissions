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





main()
