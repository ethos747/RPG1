# For testing code ONLY


def inventory_input():
    inv_input = str(input("""What do you want to look at?
[1] Items
[2] Weapons"""))
    # Item section display
    if inv_input == "1":
        print("Available Items:")
        nLists(Items)
        # Item section selection
        inv_input_items = str(input("Which do you inspect?"))
        # Health kit selection, with and additional option to use it
        if inv_input_items == "1":
            print("You can use this to heal 20% health.")
            print("You have " + str(kits) + " remaining")
            if kits == 0:
                print("You did not use a first aid kit.")
            else:
                kit_input = input("""Would you like to use it?
[1] Yes
[2] No""")
            # Adjusts to number of health kits and increases health if used
                if kit_input == "1":
                    kits -= 1
                    health += 20
                    print("You used a first aid kit and healed to:")
                    print(str(health) + "%")
                else:
                    print("You did not use the first aid kit")
    # Weapon slection list
    if inv_input == "2":
        print("Available Weapons")
        nLists(Weapons)
        inv_input_weapons = str(input("Which do you view?"))
        # Shows weapon and description out of combat, "view" only
        if inv_input_weapons == "1":
            print("Combat knife usable in a variety of situations.")
            print("Hit chance: 50%")
        elif inv_input_weapons == "1":
            print("Standard issue 9mm pistol.")
            print("Hit chance:90%")
        else:
            print ("Please choose an available option")
    else:
        print ("Please choose an available option")
