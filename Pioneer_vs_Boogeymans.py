def main():
    enemy = Boar('Pops')

    the_end_of_game = False
    while not the_end_of_game:
        enemy.health_status()
        damage = int(input())
        enemy.get_damage(damage)

        if not enemy.is_alive():
            the_end_of_game = True
            print('All enemies are dead')


class Boar:
    def __init__(self, enemy_id):
        self.enemy_id = enemy_id
        self.hp = 10

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def health_status(self):
        print('enemy Boar', self.enemy_id, 'is alive', self.hp, 'HP')

    def dying_cry(self):
        print('#$%&*^@!!?')



class Hornet:
    def __init__(self, enemy_id):
        self.hp = 1

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def health_status(self):
        print('enemy is alive', self.hp, 'HP')

    def dying_cry(self):
        print('BzzzzzWooo!!?')



main()
