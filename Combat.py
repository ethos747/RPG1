# Course: CS 30
# Period: 3
# Date created: 10/18/2021
# Date last modified: 11/25/2021
# Name: Ethan Behl
# Description: Text-based RPG Character Selection
# Controls combat in the game
try:
    import Inventory
    import Player
    import sys
except ModuleNotFoundError:
    print("Error, a module was imported incorrectly in Combat.")
    print("Game ended.")
    sys.exit()

# Enemy class that controls hp and dmg
class Enemy:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
Zombie = Enemy(10, 5)
Zombie_2 = Enemy(10, 5)
MutantZombie = Enemy(30, 20)
current_enemy = Zombie


def player_combat():
    """Allows the pleyr to enter, exit, and participate in combat"""
    global current_enemy
    if Player.current_room == "Garage":
        enemies = 1
    if Player.current_room == "Locker Room 2":
        enemies = 2
    if Player.current_room == "Dance Floor":
        enemies = 3
    if Player.current_room == "Storage":
        enemies = 1
        current_enemy = MutantZombie
    print("\nYou have entered combat!")
    while True:
        print("\nCurrent enemies ramaining: " + str(enemies))
        print("\nCurrent Health:" + str(Player.health) + "%")
        print("\nPistol Ammo:" + str(Player.pistol_ammo))
        if Player.Grenade >= 1:
            combat_input = input("""
What do you use?
[1] Use KNIFE
[2] Use Pistol
[3] Use GRENADE""")
        else:
            combat_input = input("""
What do you use?
[1] Use KNIFE
[2] Use PISTOL""")
        if combat_input == "1":
            Inventory.Knife.knife_attack()
            current_enemy.hp -= Inventory.dmg
        elif combat_input == "2":
            if Player.pistol_ammo >= 1:
                Inventory.Pistol.pistol_attack()
                Player.pistol_ammo -= 1
                current_enemy.hp -= Inventory.dmg
            else:
                print("The trigger clicks. You're out of ammo!")
        elif Player.Grenade >= 1:
            if combat_input == "3":
                Inventory.Grenade_Weapon.Grenade_Weapon_attack()
                Player.Grenade -= 1
                current_enemy.hp -= Inventory.dmg
        else:
            print("You chose nothing!")
        if current_enemy.hp <= 0:
            enemies -= 1
            current_enemy.hp = 10
            print("The zombie falls, splatting on the floor")
            if enemies >= 1:
                print("Another zombie rises and growls.")
        if enemies >= 1:
            Player.health -= current_enemy.damage
            print("The zombie deals " + str(current_enemy.damage) + " damage!")
            print("The zombie has " + str(current_enemy.hp) + "hp remaining.")
            if Player.health <= 1:
                print("You have died!")
                print("GAME OVER")
                sys.exit()
        elif enemies == 0:
            return False
