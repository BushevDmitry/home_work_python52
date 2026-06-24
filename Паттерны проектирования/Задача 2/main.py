from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_health(self):
        pass


class Goblin(Enemy):

    def attack(self):
        return 'атака ближняя'

    def get_health(self):
        return 50


class Dragon(Enemy):

    def attack(self):
        return 'атака огнём'

    def get_health(self):
        return 200


class Skeleton(Enemy):

    def attack(self):
        return 'атака стрелами'

    def get_health(self):
        return 80





class EnemyFactory(ABC):

    @abstractmethod
    def create_enemy(self):
        pass

class CreateGoblin(EnemyFactory):

    def create_enemy(self):
        return Goblin()

class CreateDragon(EnemyFactory):

    def create_enemy(self):
        return Dragon()

class CreateSkeleton(EnemyFactory):

    def create_enemy(self):
        return Skeleton()


class Spawner:
    def __init__(self, factory: EnemyFactory):
        self.factory = factory

    def spawn_wave(self, count):
        enemies = []
        for _ in range(count):
            enemies.append(self.factory.CreateEnemy())
        return enemies
