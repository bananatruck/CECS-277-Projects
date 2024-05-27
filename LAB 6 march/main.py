# Keshav Jindal
# Sahil Patel
# CECS 225
# Lab 6

from hero import Hero
from dragon import Dragon
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
import random

def attack_dragon(hero, dragons):
    for i, dragon in enumerate(dragons, start=1):
        print(f"{i}. Attack {dragon.name}: {dragon.hp}/{dragon._max_hp}")
        if isinstance(dragon, FireDragon):
            print(f"Fire Shots remaining: {dragon.f_shots}")
        elif isinstance(dragon, FlyingDragon):
            print(f"Swoop attacks remaining: {dragon.swoops}")
    choice = int(input("Choose a dragon to attack: ")) - 1
    attack_method = int(input("Attack with:\n1. Arrow (1D12)\n2. Sword (2D6)\nEnter weapon: "))
    if attack_method == 1:
        message = hero.arrow_attack(dragons[choice])
    else:
        message = hero.sword_attack(dragons[choice])
    print(message)

def dragon_response(hero, dragons):
    attacker = random.choice(dragons)
    if random.randint(0, 1) == 0:
        print(attacker.basic_attack(hero))
    else:
        print(attacker.special_attack(hero))

def game_loop(hero, dragons):
    while dragons and hero.hp > 0:
        print(f"\n{hero}\n")
        attack_dragon(hero, dragons)
        dragons = [d for d in dragons if d.hp > 0]
        if dragons:
            dragon_response(hero, dragons)
    if hero.hp > 0:
        print("Congratulations! You have defeated all the dragons and passed the trials!")
    else:
        print("You have been defeated. Better luck next time.")

def main():
    hero_name = input("What is your name, challenger?\n")
    hero = Hero(hero_name, 50)
    dragons = [
        Dragon("Deadly Nadder", 10),
        FireDragon("Gronckle", 15, 3),
        FlyingDragon("Timberjack", 20, 5)
    ]
    print(f"Welcome to dragon training, {hero_name}")
    print("You must defeat 3 dragons.")
    game_loop(hero, dragons)

if __name__ == "__main__":
    main()
