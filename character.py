import random

class Character:
    def __init__(self):
        # Rolling dice for combat strength between 1 and 6
        self._combat_strength = random.randint(1, 6)
        
        # Rolling dice for health points between 10 and 30
        self._health_points = random.randint(10, 30)

    @property
    def combat_strength(self):
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 0:  # Ensure combat strength is not negative
            self._combat_strength = value
        else:
            print("Combat strength cannot be negative.")

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        self._health_points = max(0, value)  # Prevent health from dropping below 0

    def __del__(self):
        print(f"{self.__class__.__name__} object destroyed.")
