 email = input("What's your email? ").strip()

# if this string1 and string2 is somewhere in another string, no matter where it is, return True
if "@" in email and "." in email:
    print("Valid")
else:
   print("Invalid")
