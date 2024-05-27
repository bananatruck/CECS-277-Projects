from entity import Entity
import random

class Dragon(Entity):
    def basic_attack(self, hero):
        damage = random.randint(3, 7)
        hero.take_damage(damage)
        return f"{self.name} smashes you with its tail for {damage} damage!"

    def special_attack(self, hero):
        damage = random.randint(4, 8)
        hero.take_damage(damage)
        return f"{self.name} slashes you with its claws for {damage} damage!"
