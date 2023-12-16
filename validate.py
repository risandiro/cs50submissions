 email = input("What's your email? ").strip()

# if "@" in email:

username, domain = email.split("@")

# if username: (True if username contains anything except None and "")
# if username and "." in domain: --> means --> if (username) and ("." in domain):

import re

''' .     any character except a newline
    *     0 or more repetitions
    +     1 or more repetitions
    ?     0 or 1 repetition
   {m}    m repetitions
   {m,n}  m-n repetitions '''

# re.search(pattern #string)
re.search("..*@.+.edu", email):
