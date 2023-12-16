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
   {m,n}  m-n repetitions

    ^     matches the start of the string
    $     matches the end of the string just before the newline at the end of the string

    []    set of characters to allow
    [^]   set of characters not to allow '''

# re.search(pattern #string)

# backslash before means literally a dot, not a dot from the list above
# r" or raw string means to not interpret any backslashes as a escape sequance
re.search(r"^.+@.+\.edu$", email):

# exclude "@" to both sides from the divider
re.search(r"^[^@]+@[^@]+\.edu$", email):

# include only alphanumeric and underscore
re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
