# character.py
import random

class Character:
    def __init__(self):
        self.__combat_strength = 0
        self.__health_points = 0

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        self.__combat_strength = value

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        self.__health_points = value

        def roll_dice(sides=6):
            return random.randint(1, sides)

        # Existing game functions

        def use_loot(hero, loot_item):
            if loot_item == "Health Potion":
                hero.health += 20
                print("You used a Health Potion! +20 HP.")
            elif loot_item == "Strength Elixir":
                hero.strength += 5
                print("You used a Strength Elixir! +5 Strength.")
            hero.inventory.remove(loot_item)

        # Crafting System

        # Crafting recipes: {Item: {Required Materials}}
        CRAFTING_RECIPES = {
            "Iron Sword": {"Iron Ore": 2, "Wood": 1},
            "Healing Potion": {"Herbs": 3, "Water": 1},
            "Steel Armor": {"Iron Ore": 5, "Leather": 2}
        }

        def craft_item(hero, item_name):
            """Attempt to craft an item if materials are available."""
            if item_name not in CRAFTING_RECIPES:
                print(f"{item_name} is not a craftable item.")
                return

            recipe = CRAFTING_RECIPES[item_name]

            # Check if hero has enough materials
            for material, amount in recipe.items():
                if hero.inventory.get(material, 0) < amount:
                    print(f"Not enough {material} to craft {item_name}.")
                    return

            # Deduct materials from inventory
            for material, amount in recipe.items():
                hero.inventory[material] -= amount
                if hero.inventory[material] == 0:
                    del hero.inventory[material]

            # Add crafted item to inventory
            hero.inventory[item_name] = hero.inventory.get(item_name, 0) + 1
            print(f"Successfully crafted {item_name}!")

            return item_name

