import random

print('Welcome to Dice Rolling Simulator!')

roll_quantity = int(input("How many times would you like to roll the dice?\n"))
list_of_rolls = []

for _ in range(roll_quantity):
    roll_value = random.randint(1, 6)
    print("Rolled ", len(list_of_rolls), ":", roll_value)
    list_of_rolls.append(roll_value)

print("List of Rolls:", list_of_rolls)
print("Total rolls:", len(list_of_rolls))

