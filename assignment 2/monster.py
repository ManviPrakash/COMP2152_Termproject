# monster.py

import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.combat_strength = random.randint(1, 6)
        self.health_points = random.randint(1, 20)

    def monster_attacks(self, hero_health):
        print("Monster attacks!")
        if self.combat_strength >= hero_health:
            print("The hero is defeated!")
            return 0  # Hero health becomes 0
        else:
            print(f"The hero's health is reduced to {hero_health - self.combat_strength}")
            return hero_health - self.combat_strength

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")