# enemy_factory.py
from abc import ABC, abstractmethod

class EnemyFactory(ABC):
    @abstractmethod
    def create_random_enemy(self):
        """Creates and returns a random enemy."""
        pass
