from entity import Entity
import random

class Hero(Entity):
    def sword_attack(self, dragon):
        damage = random.randint(1, 6) + random.randint(1, 6) # 2D6
        dragon.take_damage(damage)
        return f"You slash the {dragon.name} with your sword for {damage} damage."

    def arrow_attack(self, dragon):
        damage = random.randint(1, 12) # 1D12
        dragon.take_damage(damage)
        return f"You hit the {dragon.name} with an arrow for {damage} damage."
