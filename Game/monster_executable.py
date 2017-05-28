
from class_module.monster_game import*



def game_start():
    print('게임 시작')

    ggobugi = Monster('ggobugi')

    while True:
        choice = input('1.싸우기 2.아이템사용 3. 도망치기 4.나가기')

        if choice == 1:
            ggobugi.attack('pikachu')
        elif choice == 2:
            ggobugi.item()
        elif choice ==3:
            ggobugi.run()
        elif choice ==4:
            break


game_start()
