# Course: CS 30
# Period: 3
# Date created: 9/20/2021
# Date last modified: 9/22/2021
# Name: Ethan Behl
# Description: Text-based RPG menu assignment
#imports the system function allowing the "quit" option.
import sys

#Introduction to the menu and what to input
print("Welcome! To perform an action, select the number between the brackets.")
#The list of things a player can do;
menu_list = ("Interact[1]", "Explore[2]", "Inventory[3]","Status[4]","Quit[5]")
#Starting health and ammo
health = 100
pistol_ammo = 75
inv = ("Pistol[1]", "First Aid kit[2]")
#Defining the menu function
def menu ():
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
        inv_in = str(input (inv))
        if inv_in == "1":
            print("Standard issue 9mm pistol.")
        elif inv_in == "2":
            print("You can use this to heal 20% health")
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
