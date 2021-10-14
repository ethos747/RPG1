# Course: CS 30
# Period: 3
# Date created: 9/15/2021
# Date last modified: 9/27/2021
# Name: Ethan Behl
# Description: Text-based RPG
#imports the system function allowing the "quit" option.
import sys

#Introduction to the menu and what to input
print("Welcome! To perform an action, select the number between the brackets.")
print("This is a challenging game. Retry If you need.")
input(str("Continue[any key]"))
print("""It's 2:35 in the morning.
You, a police officer, pull up your car to an allyway near a nightclub.
After recieving a distress call from the near nightclub,
the station hit you up with the task of investigating the call.
You get out of the car and stare at the bright neon sign illuminating the ally.
"Moon Dark club"
""")
#The list of things a player can do;
menu_list = ("""Interact[1] 
Explore[2]
Inventory[3]
Status[4]
Quit[5]""")
#Starting health and ammo

def nLists(lists):
    """Assign and print numerical values to items in a list"""
    for item in lists:
        print(f"{lists.index(item)+1}. {item}")
Items = ["9mm Pistol", "Knife", "First aid kit"]
def inv_list():
    print("Available Items:")
    nLists(Items)
#Defining the menu function
def menu ():
    health = 80
    pistol_ammo = 75
    kits = 1
    #Player input is attatched to a variable to determine later response
    menuu = str(input (menu_list))
    #Various options based on the response
    if menuu == "1":
        #Interact options menu
        room_1 = ("Light Switch [1]", "Closet[2]")
        room_1_in = str(input (room_1))
        if room_1_in == "1":
            print("You flick on the light switch but the bulb is broken!")
        elif room_1_in == "2":
            print("You found nothing!")
        else:
            print ("Please choose an available option")
    elif menuu == "2":
        print("You are locked in the room!")
    elif menuu == "3":       
        #Inventory inspect options
        inv_list()
        inv_input = str(input("What do you want to look at?"))
        if inv_input == "1":
            print("Standard issue 9mm pistol.")
            print("Hit chance:90%")
        elif inv_input == "2":
            print("Combat knife usable in a variety of situations.")
            print("Hit chance: 50%")
        elif inv_input == "3":
            print("You can use this to heal 20% health.")
            print("You have " + str(kits) + " remaining")
            kit_input = input("""Would you like to use it?
            1. Yes
            2. No
            """)
            if kits == 0:
                print("You have no first aid kits left.")
            elif kit_input == "1":
                kits -= 1
                print("You used a first aid kit and healed to" + str(health) + "%")
            else:
                print("You did not use the first aid kit")
        else:
            print ("Please choose an available option")
    elif menuu == "4":
        print("Current Health:" + str(health) + "%")
        print("Pistol Ammo:" + str(pistol_ammo) + "%")
    #Exits the game
    elif menuu == "5":
        print("Game ended.")
        sys.exit()
    #Message for if the player choses a non-available option
    else:
        print ("Please choose an available option")
#Allows the menu to loop
while True:
    menu() 




#Game Mechanics
  #Menu system
    
    #Options for in-combat []Attack, []Dodge, []Inventory, []Status
      #Attack
        #give options of various weaponry
          #Player selects weapon, triggers weapon damage stat
      #Dodge
        #List chance to dodge [%]
        #Option for the player to do so
      #Inventory
        #Same as lsited, except certain objects cannot be used, message displayed
      #Status
        #Same as last description
      
  #Game mechanics
    #Combat
      #Turn-based, rotate enemies with player
        #Enemy turn
          #If alive, enemies will have a turn, doing their listed attack at a %, damaging the player
    #Weapons
      #List; Pistol, Enhanced pistol, Shotgun, Assault Rifle, Knife
        #Each weapon will have a hit%, damage %, ammo %
        #Knife has no ammo, lower % to hit on turn during combat
    #Obtainable items
      #List; First Aid Kit, Ammo refill of weapon %, Pistol grip, Pistol Magazine
        #First aid kit
          #Heal % health
        #Ammo refill
          #Increase ammo of the appropriate weapon by %
        #Pistol Grip
          #Increase % of pistol hitting
        #Pistol Magazine
          #Increase max ammo for pistol by %
    #Status
      #List; Health, Ammo, appropriate items
#Gameplay
  #Plot
    #You play as a police officer investigating a nightclub after recieving a distess call
  #Rooms
    #List room features, calls back to #Plot
      #Interactions
        #List of possible interaction appropriate to room; Search (object), View (object)
          #Search Object; Cabinet, Drawer, Locker
          #View Object; Locked door, event
      #enemy/npc encounters
        #How many enemies? What kind?
  #Events
    #flavour and descriptions of appropriate events, based on story plot





print ("Hello")
