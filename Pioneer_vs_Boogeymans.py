def main():
    hp = 10
    the_end_of_game = False
    while not the_end_of_game:
        print('enemy is alive', hp, 'HP')
        damage = int(input())
        hp -= damage

        if hp <= 0:
            the_end_of_game = True
            print('All enemies are dead')


main()
