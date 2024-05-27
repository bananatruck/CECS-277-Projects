import random
from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll

class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        if random.choice([True, False]):
            return BegGoblin()
        else:
            return BegTroll()