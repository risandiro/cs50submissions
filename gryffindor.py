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

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# I want a list, inside of that list I want a dictionary with key "name",
# containing a value of each iteration of the students list, and another
# key "house", containing a fixed string "Gryffindor"

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)
