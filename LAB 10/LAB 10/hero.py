# hero.py
import random
from entity import Entity

class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, 25)  # Default HP for the hero

    def melee_attack(self, enemy):
        damage = random.randint(2, 12)  # 2D6 damage
        enemy.take_damage(damage)
        return f"\n{self.name} slashes a {enemy.name} with a sword for {damage} damage."

    def ranged_attack(self, enemy):
        damage = random.randint(1, 12)  # 1D12 damage
        enemy.take_damage(damage)
        return f"\n{self.name} pierces {enemy.name} with an arrow for {damage} damage."
