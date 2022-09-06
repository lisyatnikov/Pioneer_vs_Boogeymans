def main():
    boar_create()
    the_end_of_game = False
    while not the_end_of_game:
        print('enemy is alive', hp, 'HP')
        damage = int(input())
        boar_get_damage(damage)

        if not boar_is_alive():
            the_end_of_game = True
            print('All enemies are dead')


def boar_create():
    global hp
    hp = 10


def boar_is_alive():
    return hp > 0


def boar_get_damage(damage):
    global hp
    hp -= damage
    if hp < 0:
        hp = 0


main()
