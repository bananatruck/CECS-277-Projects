from decorator import Decorator

class Fighting(Decorator):
    def abilities(self):
        abilities = super().abilities()
        abilities[1] += 1
        return abilities
    
    def constitution(self):
        return super().constitution() + 2
    
    def strength(self):
        return super().strength() + 2
    
    def wisdom(self):
        return super().wisdom() - 3
