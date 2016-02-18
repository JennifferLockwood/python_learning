from random import randint


class Dice:
    """A simple attempt to represent a die."""

    def __init__(self, sides, attempts):
        """Initialize attributes to describe a die."""
        self.sides = sides
        self.attempts = attempts

    def roll_die(self):
        print(str(self.attempts) + " attempts in a " +
              str(self.sides) + "-sided die:")
        for side in range(self.attempts):
            x = randint(1, self.sides)
            print(x)
        print()

six_sided_die = Dice(6, 10)
six_sided_die.roll_die()

ten_sided_die = Dice(10, 20)
ten_sided_die.roll_die()

twenty_sided_die = Dice(20, 10)
twenty_sided_die.roll_die()