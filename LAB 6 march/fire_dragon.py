from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self, name, max_hp, f_shots):
        super().__init__(name, max_hp)
        self.f_shots = f_shots

    def special_attack(self, hero):
        if self.f_shots > 0:
            damage = random.randint(5, 9)
            hero.take_damage(damage)
            self.f_shots -= 1
            return f"{self.name} engulfs you in flames for {damage} damage! Fire Shots remaining: {self.f_shots}"
        else:
            return f"{self.name} tried to engulf you in flames but failed! No Fire Shots remaining."

    def __str__(self):
        return super().__str__() + f" Fire Shots remaining: {self.f_shots}"
