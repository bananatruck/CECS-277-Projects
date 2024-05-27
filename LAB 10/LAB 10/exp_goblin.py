# exp_goblin.py
import random
from entity import Entity

class ExpGoblin(Entity):
    def __init__(self):
        super().__init__("Angry Goblin", random.randint(12, 15))

    def melee_attack(self, enemy):
        damage = random.randint(5, 8)
        enemy.take_damage(damage)
        return f"Angry Goblin slashes {enemy.name} for {damage} damage."
