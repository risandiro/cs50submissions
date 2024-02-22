students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

gryffindor = [

    # add student "name" value to this list, when you iterate over every key
    # in "students" list, if "house" value 

    student["name"] for student in students if student["house"] == "Gryffindor"
]
