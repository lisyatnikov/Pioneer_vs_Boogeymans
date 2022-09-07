def main():
    enemy_list = [Boar('Pops'), Boar('Frank'), Hornet('Zuo')]

    the_end_of_game = False
    while not the_end_of_game:
        enemy = enemy_list[-1] # Activate enemy in the end of list
        enemy.health_status()
        damage = int(input())
        enemy.get_damage(damage)

        if not enemy.is_alive():
            enemy.dying_cry()
            enemy_list.pop() # Eresing the dead Enemy in the enemy list.




        if not enemy_list: # Checking is anyone enemy is alive
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
        print(self.enemy_id, ': ARRR!!!') # May you include damage cry?


    def health_status(self):
        print('enemy Boar', self.enemy_id, 'is alive', self.hp, 'HP')


    def dying_cry(self):
        print(self.enemy_id, ': #$%&*^@!!?')





class Hornet:
    def __init__(self, enemy_id):
        self.enemy_id = enemy_id
        self.hp = 1

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(self.enemy_id, ': WZZZ!!!') # May you include damage cry?

    def health_status(self):
        print('enemy hornet', self.enemy_id, ' is alive', self.hp, 'HP')

    def dying_cry(self):
        print(self.enemy_id, ': BzzzzzWooo!!?')





main()
