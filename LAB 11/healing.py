from decorator import Decorator

class Healing(Decorator):
    def abilities(self):
        abilities = super().abilities()
        abilities[3] += 1
        return abilities
    
    def constitution(self):
        return super().constitution() + 3
    
    def strength(self):
        return super().strength() - 4
    
    def wisdom(self):
        return super().wisdom() + 2
