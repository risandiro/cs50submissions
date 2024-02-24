stocks = {
    "AAPL": 187.31,
    "MSFT": 124.06,
    "FB": 183.50
    }

for key,value in stocks.items():
    print(key + " : " + str(value))

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students, start=1):
    print(i, student)
