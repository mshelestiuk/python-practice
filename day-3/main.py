print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input('You\'r at the crossroad, where do you want to go? Type "Left" or "Right": ').lower()
if choice_1 == 'left':
    choice_2 = input('The ship approaches to you. Do you want to swim or wait? Answer: ')
    if choice_2 == 'wait':
        choice_3 = input('The team welcomes you on board. You need to guess a captain\'s room. What door would you choose? Type "Red","Blue" or "Yellow": ').lower()
        if choice_3 == 'red':
            print("Burned by fire.Game Over.")
        elif choice_3 == 'blue':
            print("A drunk pirate thrown you overboard. Game over.")
        else:
            print("You Win! The captain took you to a treasure island.")
    else:
        print("Sharks ate you. Game Over.")
else:
    print("Fall into a hole. Game Over.")