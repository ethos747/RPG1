# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 10/20/2021
# Name: Ethan Behl
# Description: Text-based RPG Text code


def text_intro():
    """Text and input for the beginning of the game"""
    # Introduction to the game,menu and what to input
    print("Welcome! To perform an action, select the key in the brackets.")
    print("This is a challenging game. Retry If you need.")
    # Begins the game and is followed by flavour text
    input(str("Continue [any key]"))
    print("""
It's 2:35 in the morning.
You, a police officer, pull up your car to an allyway near a nightclub.
After recieving a distress call from the near nightclub,
the station hit you up with the task of investigating the call.
You get out of the car and stare at the neon sign illuminating the ally.
"Moon Dark club"
You stare down at your badge.
""")
