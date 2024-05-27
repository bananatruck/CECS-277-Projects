from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @abstractmethod
    def abilities(self):
        pass

    @abstractmethod
    def constitution(self):
        pass

    @abstractmethod
    def strength(self):
        pass

    @abstractmethod
    def wisdom(self):
        pass

    def __str__(self):
        return f"\n{self.name} \n- Abilities -\n- Stats -\nCon: {self.constitution()}\nStr: {self.strength()}\nWis: {self.wisdom()}"
