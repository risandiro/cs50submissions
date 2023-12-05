# libraries
import sys # docs.python.org/3/library/sys.html
import json # docs.python.org/3/library/json.html

# packages
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())  -> full json response
# print(json.dumps(response.json(), indent = 2))  -> more readable json response

o = response.json()
# for every key("results" is a list that contains a dictionary)
for result in o["results"]

