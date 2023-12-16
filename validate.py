 email = input("What's your email? ").strip()

# if this string is somewhere in another string, no matter where it is, return True
if "@" in email:
    print("Valid")
else:
   print("Invalid")
