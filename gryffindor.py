students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

sorted = []
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    sorted.append(gryffindor["name"])
print (*sorted)
