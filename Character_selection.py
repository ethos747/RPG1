# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 11/25/2021
# Name: Ethan Behl
# Description: Text-based RPG Character Selection
# Dictionary for the characters
try:
    import Player
except ModuleNotFoundError:
    print("Error, a module was imported incorrectly in Character_selection.")
    print("Game ended.")
    sys.exit()
# Character variables
char_des = None
char_bonus = None
char = None

# Character classes
class Character:
    def attributes():
        print(str(char))
        print("Description: " + str(char_des))
        print("Bonus: " + str(char_bonus))


class Officer_Ornell(Character):
    def Character_attributes_OO(self):
        global char_bonus
        global char_des
        global char
        char = "OFFICER ORNELL"
        char_des = "Always prepared"
        char_bonus = "Starts with bonus pistol ammo (+4)"


class Deputy_Bernard(Character):
    def Character_attributes_DB(self):
        global char
        global char_bonus
        global char_des
        char = "DEPUTY BERNARD"
        char_des = "Big boy Bernard will mess you up"
        char_bonus = "Starts with bonus health (+20%)"


OO = Officer_Ornell()
DB = Deputy_Bernard()


def char_select_menu():
    """Allows for character slection"""
    OO.Character_attributes_OO()
    Character.attributes()
    DB.Character_attributes_DB()
    Character.attributes()
    # Input for the player to choose their character with apropriate text
    character_input = str(input("""Who are you?\n
[1] Officer Ornell
[2] Deputy Bernard\n"""))
    if character_input == "1":
        Player.pistol_ammo += 4
    elif character_input == "2":
        Player.health += 20
    else:
        print("Please choose a character.\n")
        char_select_menu()
