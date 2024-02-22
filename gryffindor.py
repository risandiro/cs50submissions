students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

gryffindor = [

    # add students "name" value to this list, when you iterate over every dictionary
    # in the list called students, if that dictionary has a key named "house" and
    # it's value is "Gryffindor"
    student["name"] for student in students if student["house"] == "Gryffindor"
]
