from public import Bus

def start():
    print('= 버스 선택창입니다 =')

    seoul = Bus('서울', 1300, '2', '5')
    busan = Bus('부산', 1200, '1', '17')
    anyang = Bus('안양', 1000, '5', '11')


    while True:
        choice = input('어떤 버스를 선택하시겠습니까? \n 1:서울, 2:부산, 3:안양, 0:끝내기 \n 입력:  ')

        if choice == '0':
            break
        elif choice == '1':
            seoul.info()
        elif choice == '2':
            busan.info()
        elif choice == '3':
            anyang.info()
        else:
            print('선택이 되지 않았습니다.')
    print('= 버스 선택창을 종료하겠습니다. =')


start()