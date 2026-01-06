import random

# Birinchi tashlash
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

# K2 bo'lmaguncha davom ettirish
while total != 2:
    print("Nope")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print("Snake eyes!")
