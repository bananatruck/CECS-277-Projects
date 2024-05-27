import random
from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll

class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        if random.choice([True, False]):
            return ExpGoblin()
        else:
            return ExpTroll()