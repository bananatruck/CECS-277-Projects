from character import Character

class Dwarf(Character):
    def __init__(self, name):
        super().__init__(name + " the Dwarf")
    
    def abilities(self):
        return [0, 1, 0, 0]  # Initial abilities: Archery, Fighting, Fire, Healing
    
    def constitution(self):
        return 13
    
    def strength(self):
        return 15
    
    def wisdom(self):
        return 10
