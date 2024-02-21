def total(galleons, sickles, knuts, pennies=0):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")


def f(*args):
    print("Numbers:", args)

f(100,50,25)

def f(**kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)

