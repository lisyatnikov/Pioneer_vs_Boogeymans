def main():
    boar = Boar()
    the_end_of_game = False
    while not the_end_of_game:
        damage = int(input())
        boar.get_damage(damage)
        boar.health_status()

        if not boar.is_alive():
            the_end_of_game = True
            print('All enemies are dead')


class Boar():
    def __init__(self, personal_id):
        self.personal_id = personal_id
        self.hp = 10

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def health_status(self):
        print('enemy is alive', self.hp, 'HP')

    def dying_cry(self):
        print('#$%&*^@!!?')



class Hornet():
    def __init__(self, personal_id):
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
