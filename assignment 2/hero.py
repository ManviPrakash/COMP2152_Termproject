# hero.py

import random
from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(1, 20)

    def hero_attacks(self, monster_health):
        print("Hero attacks!")
        if self.combat_strength >= monster_health:
            print("The monster is defeated!")
            return 0  # Monster health becomes 0
        else:
            print(f"The monster's health is reduced to {monster_health - self.combat_strength}")
            return monster_health - self.combat_strength

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")

        class Player:
            def __init__(self, name):
                self.name = name
                self.inventory = []

            def add_to_inventory(self, item):
                self.inventory.append(item)
                print(f"{item} added to your inventory!")

            def show_inventory(self):
                print("\nYour Inventory:", ", ".join(self.inventory) if self.inventory else "Empty")


def choose_weapon(player):
    if not player.inventory:
        print("You have no weapons. Fighting bare-handed!")
        return "Fist"

    print("\nChoose a weapon to use:")
    for i, weapon in enumerate(player.inventory, 1):
        print(f"{i}. {weapon}")

    choice = int(input("Enter the number of your chosen weapon: ")) - 1
    if 0 <= choice < len(player.inventory):
        return player.inventory[choice]
    else:
        print("Invalid choice. Defaulting to Fist.")
        return "Fist"
