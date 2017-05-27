def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a * b
def div(a,b):
    return a//b
def rem(a,b):
    return a%b

def start():
    print('계산기 시작')
    while True:
        choice = int(input('1.더하기 2.빼기 3. 곱하기 4. 나누기 5. 나머지구하기 6. 나가기 '))
        if (choice <=5):
            numberA = int(input("첫번째 숫자를 입력하시오 : "))
            numberB = int(input("두번째 숫자를 입력하시오 : "))
            if(choice == 1):
                result = sum(numberA,numberB)
                print(result)
            elif(choice ==2):
                result = sub(numberA,numberB)
                print(result)
            elif(choice ==3):
                result = mul(numberA,numberB)
                print(result)
            elif(choice == 4):
                result = div(numberA,numberB)
                print(result)
            elif(choice == 5):
                result = rem(numberA,numberB)
                print(result)
        elif(choice == 6):
            break
        else:
            print('잘못입력하셨습니다. 다시 입력해주세요')
    print('계산기 종료')


start()
