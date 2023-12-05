# import random
from random import choice, randint, shuffle

# random.choice -> choice
coin = choice(["heads", "tails"])
# print(coin)

number = randint(1, 10)
# print(number)

# it doesn't just return a value, it shuffles the whole list
cards = ["jack", "queen", "king"]
shuffle(cards)
for i in cards:
    print()
