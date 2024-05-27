# beg_goblin.py
import random
from entity import Entity

class BegGoblin(Entity):
    def __init__(self):
        super().__init__("Goblin", random.randint(7, 9))

    def melee_attack(self, enemy):
        damage = random.randint(4, 6)
        enemy.take_damage(damage)
        return f"Goblin bites {enemy.name} for {damage} damage."
