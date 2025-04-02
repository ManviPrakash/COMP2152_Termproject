# crafting.py

def craft_item(player_inventory):
    # defining the craftable items and what's required
    craftable_items = {
        "wooden sword": ["wood", "stone"],
        "stone axe": ["stone", "wood"],
        "health potion": ["herb", "water"],
        "magic wand": ["wood", "magic essence"]
    }

    crafted_items = []

    # checking craftable items
    for item, requirements in craftable_items.items():
        # Check if the player has all required materials
        if all(req in player_inventory for req in requirements):
            crafted_items.append(item)

    # Informing crafted items
    if crafted_items:
        print("You can craft the following items:")
        for i, crafted_item in enumerate(crafted_items, 1):
            print(f"{i}. {crafted_item}")

        # choosing the item
        choice = int(input("Enter the number of the item you want to craft: ")) - 1
        if 0 <= choice < len(crafted_items):
            crafted_item = crafted_items[choice]
            # Remove the required materials from the inventory
            for req in craftable_items[crafted_item]:
                player_inventory.remove(req)
            # Add the crafted item to the inventory
            player_inventory.append(crafted_item)
            print(f"\nYou crafted a {crafted_item}!")
        else:
            print("Invalid choice.")
    else:
        print("You do not have the required materials to craft any items.")


if __name__ == "__main__":
    # Example player inventory
    player_inventory = ["wood", "stone", "health potion", "herb"]

    # Call the crafting function
    craft_item(player_inventory)