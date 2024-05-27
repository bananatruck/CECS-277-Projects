# LAB 11
# Keshav Jindal
# I created a role-playing character creation program following the Decorator pattern. 
# There are three base character types: Dwarf, Elf, and Halfling. Each character can be decorated with abilities like Archery, Fighting, Fire, and Healing. 
# The program displays the updated stats for the created character. Here's the UML diagram and class descriptions I followed to implement it.


# Importing character classes and abilities
from elf import Elf
from dwarf import Dwarf
from halfling import Halfling
from archery import Archery
from fighting import Fighting
from fire import Fire
from healing import Healing

# Function to create a character
def create_character():
    # Prompting user for character type and name
    print("Character Maker!")
    print("Choose your character:")
    print("1. Dwarf")
    print("2. Elf")
    print("3. Halfling")
    choice = int(input("Enter choice: "))
    name = input("\nWhat is your character's name? ")

    # Creating the base character based on user's choice
    if choice == 1:
        character = Dwarf(name)
    elif choice == 2:
        character = Elf(name)
    elif choice == 3:
        character = Halfling(name)

    # Displaying the base character
    print(character)

    # Loop to add abilities to the character
    for _ in range(5):
        print("Add an ability:")
        print("1. Archery")
        print("2. Fighting")
        print("3. Fire Magic")
        print("4. Healing")
        ability_choice = int(input("Enter ability: "))
        if ability_choice == 1:
            character = Archery(character)
        elif ability_choice == 2:
            character = Fighting(character)
        elif ability_choice == 3:
            character = Fire(character)
        elif ability_choice == 4:
            character = Healing(character)

        # Displaying the character with added abilities
        print(character)
    
    # Checking if character's stats are valid
    if character.constitution() <= 0 or character.strength() <= 0 or character.wisdom() <= 0:
        print("You have failed at making a character.")
    else:
        print("Congratulations! You have created your character.")

# Running the character creation function if this script is executed
if __name__ == "__main__":
    create_character()

