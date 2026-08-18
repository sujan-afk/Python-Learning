import random 

name = random.choice(["Sujan", "Kristina", "Sudip", 'Sabitra', "Chakai"])
print(name)

print(random.randint(1,10))
cards = ["Ace", "2", "Jack", "Queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)