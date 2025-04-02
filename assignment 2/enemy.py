import random
from character import Character

class Enemy(Character):  # Enemy also inherits from Character
    def __init__(self, combat_strength=None):
        super().__init__()
        self.combat_strength = combat_strength if combat_strength else random.randint(1, 6)
        self.health_points = random.randint(5, 20)  # Different health range from monster
        self.weapon = None

    def attack(self, target):
        """Enemy attacks and reduces the target's health."""
        if not isinstance(target, Character):
            print("Error: Target must be an instance of Character.")
            return

        if target.health_points > 0:
            damage = self.combat_strength
            target.health_points -= damage
            print(f"Enemy strikes! Hero takes {damage} damage. Hero's health: {target.health_points}")

            if target.health_points <= 0:
                print("Hero defeated!")

    def set_health(self, health_points):
        """Set the health points of the enemy."""
        self.health_points = max(0, health_points)  # Prevent negative health
        print(f"Enemy's health is: {self.health_points}")

    # Add monster_attacks using list comprehension
    def monster_attacks(self, target):
        """Enemy performs an attack on the target (Hero)."""
        print("Enemy attacks!")

        # List comprehension to apply attack damage for multiple attack attempts
        attacks = [
            self.attack(target) if target.health_points > 0 else "Target already defeated"
            for _ in range(random.randint(1, 3))  # Random number of attacks
        ]
        
        # Print results of all attacks
        for result in attacks:
            if isinstance(result, str):
                print(result)
