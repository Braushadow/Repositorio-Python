import random

'''class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

my_die = Die(6)'''

lottery = [1,2,3,4,5,6,7,8,9,10,'a', 'b', 'c', 'd', 'e']
print(lottery)
winner_ticket = random.sample(lottery, 4)
print(f"The winner ticket is {winner_ticket}")
