# beg_troll.py
import random
from entity import Entity

class BegTroll(Entity):
    def __init__(self):
        super().__init__("Troll", random.randint(8, 10))

    def melee_attack(self, enemy):
        damage = random.randint(5, 9)
        enemy.take_damage(damage)
        return f"Troll smashes {enemy.name} for {damage} damage."
