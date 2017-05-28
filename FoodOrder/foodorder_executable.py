from class_module.foodorder import*


mcdonals = Mcdonalds()
worker = Worker()
burger1 = Burger('불고기',4800)
burger2 = Burger('상하이',6000)
burger3 = Burger('빅맥',5800)




def game_start():
    print('==Mcdonalds Tycoon==')

    while True:
        choice = input('무엇을 하시겠습니까?\n1: 매장 생성/이름변경\n2: 직원 생성/이름변경\n3: 주문하기\n4: 시재 확인\n5: 종료\n>>')

        if choice=='1':
            if mcdonals.name ==None:
                shop_name = input('생성할 매장 이름을 입력해주세요.\n>>')
                mcdonals.name=shop_name
            else:
                shop_name = input('변경할 매장 이름을 입력해주세요. 현재 이름 : 맥도날드 {}\n>>'.format(mcdonals.name))
                mcdonals.name = shop_name

        elif choice=='2':
            if worker.name == None:
                worker_name = input('생성할 직원 이름을 입력해주세요.\n>>')
                worker.name = worker_name
            else:
                worker_name = input('변경할 직원 이름을 입력해주세요. 현재 이름 : 직원 {}\n>>'.format(worker.name))
                worker.name = worker_name

        elif choice=='3':
            if mcdonals.name is None or worker.name is None:
                print('매장과 직원을 먼저 생성해주세요')
            else:
                print('직원 {} : 어서오세요 맥도날드 {}점 입니다.'.format(worker.name,mcdonals.name))
                print('주문 하시겠습니까?')
                menu_num = input('1. {}\n2. {}\n3. {}\n>>'.format(burger1.name,burger2.name,burger3.name))
                if menu_num =='1':
                    menu_name = burger1.name
                    menu_price = burger1.price
                elif menu_num=='2':
                    menu_name = burger2.name
                    menu_price = burger2.price
                elif menu_num=='3':
                    menu_name = burger3.name
                    menu_price = burger3.price
                else:
                    print('잘못 고르셨습니다')
                    continue
                print('{}를 선택하셨습니다. {}원 입니다.'.format(menu_name,menu_price))
                mcdonals.money+=menu_price

        elif choice=='4':
            print('시재 확인하기\n현재 시재는 {}원 입니다.'.format(mcdonals.money))
        elif choice=='5':
            break


game_start()
