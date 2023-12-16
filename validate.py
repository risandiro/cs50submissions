 email = input("What's your email? ").strip()

# if "@" in email:

username, domain = email.split("@")

# if username: (True if username contains anything except None and "")
# if username and "." in domain: --> means --> if (username) and ("." in domain):

import re
# re.search(pattern #string)
re.search("@", email):
