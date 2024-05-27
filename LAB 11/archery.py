from decorator import Decorator

class Archery(Decorator):
    def abilities(self):
        abilities = super().abilities()
        abilities[0] += 1
        return abilities
    
    def constitution(self):
        return super().constitution() - 2
    
    def strength(self):
        return super().strength() + 5
    
    def wisdom(self):
        return super().wisdom() - 2
