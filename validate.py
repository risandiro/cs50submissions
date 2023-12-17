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
    [^]   set of characters not to allow

    \d    decimal digit (0-9)
    \D    not a decimal digit
    \s    whitespace characters (space, tab)
    \w    word character (upper and lower alphanumeric and underscore)
    \W    not a word character

    A|B   either A or B
    (...) a group
    (?:...) non-capturing version

    re.IGNORECASE   case insensitively
    re.MULTILINE
    re.DOTALL '''

# re.search(pattern #string #flag)

# backslash before means literally
# r" or raw string means to interpret any backslashes as a escape sequence
re.search(r"^.+@.+\.edu$", email):

# exclude "@" to both sides from the divider
re.search(r"^[^@]+@[^@]+\.edu$", email):

# include only alphanumeric and underscore
re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
re.search(r"^\w+@\w+\.edu$", email):

# more options
re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):

# include space in two variations
re.search(r"^(\w|\s)+@\w+\.(com|edu|gov|net|org)$", email):
re.search(r"^[a-zA-Z0-9_ ]+@\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):


