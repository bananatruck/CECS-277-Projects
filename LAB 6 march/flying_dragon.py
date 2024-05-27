from dragon import Dragon
import random

class FlyingDragon(Dragon):
    def __init__(self, name, max_hp, swoops):
        super().__init__(name, max_hp)
        self.swoops = swoops

    def special_attack(self, hero):
        if self.swoops > 0:
            damage = random.randint(5, 8)
            hero.take_damage(damage)
            self.swoops -= 1
            return f"{self.name} hits you with a swooping attack for {damage} damage! Swoops remaining: {self.swoops}"
        else:
            return f"{self.name} tried to hit you with a swooping attack but failed! No Swoops remaining."

    def __str__(self):
        return super().__str__() + f" Swoop attacks remaining: {self.swoops}"
