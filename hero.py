import random
from character import Character  # Import the Character class

class Hero(Character):
    def __init__(self, combat_strength=None):
        super().__init__()
        self.combat_strength = combat_strength if combat_strength else random.randint(1, 6)
        self.health_points = random.randint(10, 30)
        self.weapon = None
        self.belt = []  # Store collected loot items

    def set_weapon(self, weapon_roll, weapons):
        """Set the hero's weapon based on the dice roll."""
        if 0 < weapon_roll <= len(weapons):
            self.weapon = weapons[weapon_roll - 1]
        else:
            self.weapon = None
        print(f"Hero's weapon is: {self.weapon}")

    def set_health(self, health_points):
        """Set the health points of the hero."""
        self.health_points = max(0, health_points)  # Prevent negative health
        print(f"Hero's health is: {self.health_points}")

    def collect_loot(self, loot_options):
        """Collect loot for the hero and add it to the belt."""
        loot_item = random.choice(loot_options)  
        self.belt.append(loot_item)
        print(f"Hero collects: {loot_item}")

    def use_loot(self):
        """Use loot from the hero's belt to gain or lose health."""
        if self.belt:
            loot = self.belt.pop()  
            print(f"Hero uses: {loot}")

            if loot == "Health Potion":
                self.health_points += 5  
                print(f"Hero's health after using Health Potion: {self.health_points}")

            elif loot == "Poison Potion":
                self.health_points -= 5  
                print(f"Hero's health after using Poison Potion: {self.health_points}")

        else:
            print("No loot left to use.")

    def attack(self, target):
        """Hero attacks and reduces the target's health."""
        if not isinstance(target, Character):  
            print("Error: Target must be an instance of Character.")
            return

        if target.health_points > 0:
            damage = self.combat_strength
            target.health_points -= damage
            print(f"Hero attacks! Target takes {damage} damage. Target's health: {target.health_points}")

            if target.health_points <= 0:
                print("Target defeated!")
