import random
import os
import platform
from hero import Hero
from monster import Monster

# Define Dice, Weapons, Loot, and Powers
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
monster_powers = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}

# Function to save the number of monsters killed to a file
def save_game_data(monsters_killed):
    try:
        with open('game_data.txt', 'w') as file:
            file.write(f"Monsters Killed: {monsters_killed}")
        print("Game data saved successfully.")
    except Exception as e:
        print(f"Error saving game data: {e}")

# Function to load the number of monsters killed from a file
def load_game_data():
    try:
        with open('game_data.txt', 'r') as file:
            data = file.read().strip()
            monsters_killed = int(data.split(":")[-1].strip())
            print(f"Loaded game data. Monsters killed: {monsters_killed}")
            return monsters_killed
    except FileNotFoundError:
        print("No saved game data found. Starting new game.")
        return 0
    except Exception as e:
        print(f"Error loading game data: {e}")
        return 0

# Show system and Python version information
print("System Information:")
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python Version: {platform.python_version()}")

# Load previous game data (monsters killed)
monsters_killed = load_game_data()

# Initialize variables
num_stars = 0
input_invalid = True
i = 0

# Input Validation for Combat Strength
while input_invalid and i < 5:
    print("    ------------------------------------------------------------------")
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    if not combat_strength.isnumeric() or not m_combat_strength.isnumeric():
        print("Invalid input. Please enter numbers only.")
        i += 1
        continue

    combat_strength, m_combat_strength = int(combat_strength), int(m_combat_strength)

    if combat_strength not in range(1, 7) or m_combat_strength not in range(1, 7):
        print("Enter a number between 1 and 6.")
        i += 1
        continue

    input_invalid = False

if not input_invalid:
    hero = Hero(combat_strength)
    monster = Monster(m_combat_strength)

    # Roll for weapon
    input("Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)
    hero.set_weapon(weapon_roll, weapons)

    # Roll for health points
    input("Roll for your health points (Press enter)")
    hero.set_health(random.choice(big_dice_options))

    input("Roll for the monster's health points (Press enter)")
    monster.set_health(random.choice(big_dice_options))

    # Collect Loot
    print("    ------------------------------------------------------------------")
    input("Roll for first item (Press enter)")
    hero.collect_loot(loot_options)

    input("Roll for second item (Press enter)")
    hero.collect_loot(loot_options)

    print(f"Your belt: {sorted(hero.belt)}")

    # Use Loot
    hero.use_loot()

    # Monster Power Roll
    input("Roll for Monster's Magic Power (Press enter)")
    power_roll = random.choice(list(monster_powers.keys()))
    monster.increase_strength(monster_powers[power_roll])

    # Fight Sequence
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while hero.health_points > 0 and monster.health_points > 0:
        input("Roll to see who strikes first (Press enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 != 0:
            input("You strike (Press enter)")
            hero.attack(monster)
            if monster.health_points == 0:
                num_stars = 3
                break
            input("The monster strikes (Press enter)")
            monster.monster_attacks(hero)
        else:
            input("The Monster strikes first (Press enter)")
            monster.monster_attacks(hero)
            if hero.health_points == 0:
                num_stars = 1
                break
            input("You strike back!! (Press enter)")
            hero.attack(monster)

    winner = "Hero" if monster.health_points == 0 else "Monster"

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        hero_name = input("Enter your Hero's name (two words): ")
        name = hero_name.split()

        if len(name) != 2 or not name[0].isalpha() or not name[1].isalpha():
            print("Please enter a valid two-word name.")
            tries += 1
        else:
            short_name = name[0][:2] + name[1][0]
            print(f"I'm going to call you {short_name} for short")
            input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print(f"Hero {short_name} gets <{stars_display}> stars")

    # Save game data after the battle
    monsters_killed += 1 if monster.health_points == 0 else 0
    save_game_data(monsters_killed)
