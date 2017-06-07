#Level 1

# (1) x만큼 간격이 있는 n개의 숫자
# number_generator함수는 x와 n을 입력 받습니다.
# 2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
# [2,4,6,8,10]
#
# 4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
# [4,8,12]
#
# 이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.

# (1) for문 활용

def number_generator(x,n):
    list = []
    for i in range(n):
        #range(5) = 0,1,2,3,4
        data = x*(i+1)
        list.append(data)
    return list

# (2) 리스트컴프리헨션 활용

def number_generator(x,n):
    return [x*(i+1) for i in range(n)]

# (2) 핸드폰번호 가리기
# 예를들어 s가 "01033334444"면 "*******4444"를 리턴하고, "027778888"인 경우는 "*****8888"을 리턴하면 됩니다.

# a = "Life is too short"
# >>> a.replace("Life", "Your leg")
# replace(바뀌게 될 문자열,바꿀 문자열)

def hide_numbers(s):
    hide = len(s) - 4
    change = hide * '*'
    return s.replace(s[0:hide],change)

def hide_numbers(s):
    return '*'*(len(s)-4) + s[-4:]

# (3) def average(list):
# 함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
# 어떠한 크기의 list가 와도 평균값을 구할 수 있어야 합니다.

def average(list):
    avg = 0
    sum = 0

    for i in list:
        sum += i
        average = sum/len(list)
        return average()

def average(list):
    return (sum(list)/ len(list))

from functools import reduce
def average(list):
    return reduce(lambda x,y : x + y, list / len(list)
# reduce(함수,순서형 자료) : reduce함수는 원소들을 누적으로 함수에 적용시킨다.


# (4) evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.
# num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요.
# num은 0이상의 정수이며, num이 음수인 경우는 없습니다.

def evenOrOdd(num):
        s = ""
        if num % 2 ==0:
            s = 'Even'
        else:
            s ='Odd'
        return s

def evenOrOdd(num):
    s = ""
    if num % 2 ==0:
        s ='Even'
    if num % 2 ==1:
        s ='Odd'

    return s

def evenOrOdd(num):
    s = ""
    if not num % 2 ==1:
        s ='Even'
    else:
        s ='Odd'

    return s

def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"

def evenOrOdd(num):
    return 'Even' if num % 2 ==0 else 'Odd'


# (5) rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.
# mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.
# 예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.
# del 리스트 [오픈셋(순서)], 리스트.remove('값')

def rm_small(mylist):
    del(mylist[mylist.index(min(mylist))])
    return mylist

def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist
# (6) nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
# n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
# 예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.
# squr()메서드 : x의 제곱근을 반환(제곱근  ** (1/2))

import math
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:# (나머지가 0이라면)
        return (sqrt + 1) ** 2
    return 'no'

def nextSquare(n):
    from math import sqrt
    return 'no' if sqrt(n) % 1 ==0 else (sqrt(n)+1)**2

def nextSquare(n):
    for x in range(1,n):
        if x ** 2 == n:
            return (x+1) **2
        return 'no'

def nextSquare(n):
    x = n**(1/2)
    if x % 1 ==0:
        return (int(x)+1)**2
    else:
        return 'no'

#pow(2,3) 2의 3승 pow(2,3,4) = 2의 3승을 4로 나눈 나머지를 의미

def nextSqaure(n):
    sqrt = pow(n,0.5)
    return pow(sqrt +1,2) if sqrt == int(sqrt) else 'no'
# sqrt(제곱근) = int(sqrt):정수형이라면,

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));

# (7) sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
# 예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
# sum_digit함수를 완성해보세요.

def sum_digit(number):
    a = str(number)
    j = list(a)
    k = 0
    for i in j:
        k = k + int(i)
    return k

def sum_digit(number):
    return sum([int(i) for i in str(number)])
# 리스트 컴프리헨션 사용

def sum_digit(number):
    return sum(map(int,str(number)))

# map(함수,반복가능한자료형)으로  입력받은 자료형의 각 요소가 함수 f에 수행된 결과를 묶어서 리턴하는 함수

def sum_digit(number):
    if number < 10:
        return number
    return(number % 10) + sum_digit(number // 10)

#number =123일경우 , 123 % 10 = 3, sum_digit(함수로다시리턴) : 123 // 10 : 12 - 12 리턴값
# 12 리턴값 : 12%10 = 2, 12//10 = 1 (2+1) = 3
# 즉 3(123%10) + 3 (12리턴값) = 6

# (8) strToInt 메소드는 String형 str을 매개변수로 받습니다.
# str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요.
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

def strToInt(str):
    result = 0
    result = int(str)

    return result
#
# (9) water_melon함수는 정수 n을 매개변수로 입력받습니다.
# 길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요.
#
# 예를들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.

def water_melon(n):
    return ("수박"*n)[:-n]

# 튜플도 인덱싱과 슬라이싱이 가능하다. t =(1,5,10)
# 인덱스 : 리스트와 마찬가지로 한 요소를 리턴하는 인덱싱 second =t[1] =5 , last =t[-1] = 10 ,
# 슬라이싱 : 특정 부분집합을 리턴하는 슬라이싱 s =t[1:2] = 5(t[index]) , s=t[1:] : 5,10

# (10) findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.
#
# seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

def findKim(seoul):
    return "김서방은 {}에 있다.".format(seoul.index("Kim"))

def findKim(seoul):
    kimIdx = 0

    for kimIdx in range(len(seoul)):
        if(seoul[kimIdx] == "Kim"):
            break
        return "김서방은 {}에 있다.".format(kimIdx)

def findKim(seoul):
    kimIdx = 0
    for index,i in enumerate(seoul):
        if i == "Kim":
            kimIdx = index
    return "김서방은 {}에 있다.".format(kimIdx)

# (11) printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
# 다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
# printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.

def printTriangle(num):
    s = ""
    for i in range(1,num+1):#(1이상 num+1미만)
        s += "*"*i + "\n" # 문자열을 쓸때는 "" 큰쌍따음표를 사용한다.
    return s

def printTriangle(num):
    return ''.join(["*"*i + "\n" for i in range(1,num+1)])


# (12)alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.
# s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.
# 예를들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다
# try - except구문을 활용하여 값이 숫자가아닌문자가 들어있으면 valueError를 발생시킨다.

def alpha_string46(s):
    try:
        if ((len(s) == 4 or len(s) == 6 ) and int(s)):
            return True
        else:
            return False
    except ValueError:
        return False

# isdigit()는 숫자여부를 파악하며 모든 문자가 0에서 9까지의 숫자이면 True반, 리턴 : True,False

def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]

# 정규표현식으로 해결하기 import re

def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$"),s)
# bool 값은 true/false로 리턴
# re.match(문자열패턴(정규표현식),문자열)
# (\d{4} | \d{6} ) : 숫자가 4회 또는(|) 숫자가 6회

