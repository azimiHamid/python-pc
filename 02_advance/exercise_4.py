import random

class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        # Both return (x, y) and return x, y are correct and will return a tuple with the two values.
        # return (x, y)
        return x, y 
        
            
dice = Dice()
print(dice.roll())