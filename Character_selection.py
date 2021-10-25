# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 10/20/2021
# Name: Ethan Behl
# Description: Text-based RPG Character Selection
# Dictionary for the characters
character_select = {
    "Officer Ornell": {"description": "Nick name:'Lucky'",
                       "bonus": """Increased chance to find items
when searching"""},
    "\nDeputy Bernard": {"description": "Big boy Bernard will mess you up",
                       "bonus": "Takes less damage from all sources"}}


def char_select_menu():
    """Allows the player to select their character using the dictionary"""
    # prints out charcter information
    for people in character_select:
        print(f"{people}: ")
        for item in character_select[people]:
                print(f"{item} - {character_select[people][item]}")
    # Input for the player to choose their character with apropriate text
    character_input = str(input("""Who are you?\n
[1] Officer Ornell
[2] Deputy Bernard\n"""))
    if character_input == "1":
        print("You are playing as Officer Ornell")
        character_select.pop("\nDeputy Bernard")
    elif character_input == "2":
        print("You are playing as Deputy Bernard")
        character_select.pop("Officer Ornell")
    else:
        print("Please choose a character.\n")
        char_select_menu()
