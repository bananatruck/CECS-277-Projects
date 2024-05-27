from character import Character

class Halfling(Character):
    def __init__(self, name):
        super().__init__(name + " the Halfling")
    
    def abilities(self):
        return [0, 0, 0, 1]  # Initial abilities: Archery, Fighting, Fire, Healing
    
    def constitution(self):
        return 15
    
    def strength(self):
        return 10
    
    def wisdom(self):
        return 13
