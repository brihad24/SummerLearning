import random

class Dice:
    def roll():
        x = random.randint(1, 6)
        y = random.randint(1, 6)

        dice_numbers = (x, y)
        return dice_numbers

output = Dice()
print(Dice.roll())