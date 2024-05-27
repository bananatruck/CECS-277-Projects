from decorator import Decorator

class Fire(Decorator):
    def abilities(self):
        abilities = super().abilities()
        abilities[2] += 1
        return abilities
    
    def constitution(self):
        return super().constitution() - 3
    
    def strength(self):
        return super().strength() - 1
    
    def wisdom(self):
        return super().wisdom() + 5
