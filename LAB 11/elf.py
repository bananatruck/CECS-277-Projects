from character import Character

class Elf(Character):
    def __init__(self, name):
        super().__init__(name + " the Elf")
    
    def abilities(self):
        return [1, 0, 0, 0]  # Initial abilities: Archery, Fighting, Fire, Healing
    
    def constitution(self):
        return 13
    
    def strength(self):
        return 10
    
    def wisdom(self):
        return 15
