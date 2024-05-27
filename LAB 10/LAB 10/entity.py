# entity.py
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    def take_damage(self, dmg):
        self._hp = max(self._hp - dmg, 0)
        if self._hp == 0:
            return f"{self._name} has been defeated."
        return f"{self._name} now has {self._hp} HP remaining."

    def __str__(self):
        return f"{self._name} HP: {self._hp}"

    @abstractmethod
    def melee_attack(self, enemy):
        """Perform a melee attack on another entity. Must be overridden by subclasses."""
        pass
