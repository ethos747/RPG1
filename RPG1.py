# Course: CS 30
# Period: 3
# Date created: 9/15/2021
# Date last modified: 9/15/2021
# Name: Ethan Behl
# Description: Text-based RPG
#Game Mechanics
  #Menu system
    #Options for out of combat []Interact, []Explore, []Inventory, []Status
      #Interact
        #after room features have been listed, interactable options are given when this is chosen
        #Apropriate action happens based on player choice
      #Explore
        #Select this to change what room you are in out of combat
      #Inventory
        #Lists all items in inventory, [#] infront
          #Can view each items description by selectiong said [#], and use them
      #Status
        #List Health %/100, Ammo %/100
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
