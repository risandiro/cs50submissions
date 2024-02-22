students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

sort = []
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    sort.append(gryffindor["name"])
print (*sort, sep="\n")
