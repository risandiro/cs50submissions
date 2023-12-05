# libraries
import sys # docs.python.org/3/library/sys.html
import json # docs.python.org/3/library/json.html

# packages
import requests

if len(sys.argv) != 2:
    sys.exit()

# pretending that we are a browser and loading a page from a url
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())  -> full json response
# print(json.dumps(response.json(), indent = 2))  -> more readable json response

o = response.json()

# we know that the response contains a key called "results" and that it a a list
# and that list contains only one song, because we set limit=1 in the url
for result in o["results"]:
    print(result["trackName"])

