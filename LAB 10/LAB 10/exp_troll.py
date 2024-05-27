# exp_troll.py
import random
from entity import Entity

class ExpTroll(Entity):
    def __init__(self):
        super().__init__("Horrible Troll", random.randint(15, 18))

    def melee_attack(self, enemy):
        damage = random.randint(8, 12)
        enemy.take_damage(damage)
        return f"Horrible Troll slams {enemy.name} for {damage} damage."
