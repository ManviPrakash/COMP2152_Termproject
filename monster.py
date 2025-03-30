import random
from character import Character  # Import the Character class

class Monster(Character):
    def __init__(self, combat_strength=None):
        super().__init__()
        if combat_strength is None:  # If no combat strength is provided, generate randomly
            self.combat_strength = random.randint(1, 6)
        else:
            self.combat_strength = combat_strength  # Use the provided combat strength
        self.health_points = random.randint(10, 30)

    def monster_attacks(self, hero):
        """Monster attacks the hero and deals damage."""
        print("Monster strikes!!!")
        # Randomize damage based on combat_strength
        damage = random.randint(1, self.combat_strength)
        hero.health_points -= damage
        print(f"Hero takes {damage} damage. Hero's health after monster attack: {hero.health_points}")

        # Ensure health doesn't drop below 0
        if hero.health_points <= 0:
            print("Hero has been defeated!")
            hero.health_points = 0  # Make sure health doesn't go negative
        
        return hero.health_points  # Return updated health

    def increase_strength(self, magic_power):
        """Increase the monster's combat strength based on a magic power."""
        print(f"Monster's combat strength increased by {magic_power}!")
        self.combat_strength += magic_power
        print(f"Monster's new combat strength: {self.combat_strength}")

    def set_health(self, health_points):
        """Set the health points of the monster."""
        self.health_points = max(0, health_points)  # Prevent negative health
        print(f"Monster's health is now: {self.health_points}")
