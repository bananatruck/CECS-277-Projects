#CECS 277 
#LAB-10
#KESHAV JINDAL
# In this code, I followed the guidelines and instructions provided by the TA and Professor.
# I, Keshav, dedicated my efforts to developing the base, concepts, and design of this lab.
# I applied various concepts taught in class such as defining functions, using enumerate, reading files, importing from other files, using random, and more.
# I conducted several test runs to ensure the program is robust and handles incorrect inputs effectively.
# I also presented the code to our TA, who offered feedback and helped resolve an issue I encountered, enabling me to complete the lab successfully.

import random
from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory


def main():
    print("Monster Trials")
    hero_name = input("What is your name? ")
    hero = Hero(hero_name)
    factories = [BeginnerFactory(), BeginnerFactory(), ExpertFactory()]
    monsters = [factory.create_random_enemy() for factory in factories]

    while monsters and hero.hp > 0:
        print(f"\nYou will face a series of {len(monsters)} monsters, {hero.name}.\nDefeat them all to win.\n\nChoose an enemy to attack:")
        for idx, monster in enumerate(monsters):
            print(f"{idx + 1}. {monster.name} HP: {monster.hp}")
        
        choice = int(input("Enter Choice: ")) - 1
        print()
        monster = monsters[choice]
        
        attack_type = int(input(f"{hero.name} HP: {hero.hp}\n1. Sword Attack\n2. Arrow Attack\nEnter choice: "))
        if attack_type == 1:
            print(hero.melee_attack(monster))
        else:
            print(hero.ranged_attack(monster))
        
        if monster.hp > 0:
            print(monster.melee_attack(hero))
        else:
            print(f"You have slain the {monster.name}")
            monsters.remove(monster)
        
        if not monsters:
            print("\nCongratulations! You defeated all three monsters! Game Over")
        elif hero.hp <= 0:
            print("\nYou have been defeated. Game Over")
            
if __name__ == "__main__":
    main()
