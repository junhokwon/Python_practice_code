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

# (13) numPY함수는 대문자와 소문자가 섞여있는 문자열 s를 매개변수로 입력받습니다.
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 리턴하도록 함수를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
# 예를들어 s가 "pPoooyY"면 True를 리턴하고 "Pyy"라면 False를 리턴합니다.

def numPY(s):
    if s.lower().count('p') == s.lower().count('y'):
        return True
    else:
        return False

# (14) strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
# strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.
#
# 예를들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 결과는 ["car", "bed", "sun"]이 됩니다.
# strange_sort함수를 완성해 보세요.

def strange_sort(strings,n):
    return sorted(strings,key=lambda stirngs:strings[n])

# sorted(문자열,key) 입력한 값을 정렬하고, 결과값을 list로 출력해주는 함수, 정렬후 ->list출력
# 딕셔너리 {}에 있는 key값은 strings:strings[n]기준을 세우는것인데 , strings를 불러와서
# strings의 [n]번째 기준으로 하겠다.

# 제곱수가 가장 작은 순서대로 정렬하고 싶다면, a = [ -1, -8, 3, -4, 2, 5, -7]일때
# a.sorted(key=lambda 매개변수 x : x*x(표현식),reverse=True)

# (15) 딕셔너리는 들어있는 값에 순서가 없지만, 키를 기준으로 정렬하고 싶습니다. 그래서 키와 값을 튜플로 구성하고, 이를 순서대로 리스트에 넣으려고 합니다.
# 예를들어 {"김철수":78, "이하나":97, "정진원":88}이 있다면 각각의 키와 값을
#
# ("김철수", 78)
# ("이하나", 97)
# ("정진원", 88)
# 과 같이 튜플로 분리하고 키를 기준으로 정렬해서 다음과 같은 리스트를 만들면 됩니다.
# [ ("김철수", 78), ("이하나", 97), ("정진원", 88) ]
#
# 다음 sort_dictionary 함수를 완성해 보세요.

def sort_dictionary(dic):
    return sorted(tuple(dic.items()))

def sort_dictionary(dic):
    return sorted(dic.items(),key=lambda x : x[0])

# x[0] : 키 x[1] : 값 (key=lambda 매개변수 x : x*x(표현식)

# (16) no_continuous함수는 스트링 s를 매개변수로 입력받습니다.
#
# s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.
# 예를들어 다음과 같이 동작하면 됩니다.
#
# s가 '133303'이라면 ['1', '3', '0', '3']를 리턴
# s가 '47330'이라면 [4, 7, 3, 0]을 리턴
# (1) 순서를 유지하면서(list는 순서가 있다.) , (2) 중복된 요소를 제거해야하 한다.

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
        return a
        # 리스트에 요소추가할경우 , append를 사용한다 append(x) : 마지막에 x를 추가하는 함수


def no_continuous(s):
    result = []
    for idx,num in enumerate(s):
        if idx == 0:
            result.append(num)
        else:
            if num == result[-1]:
                # 맨마지막의 리스트의 index[-1] 값이 숫자와 같으면 계속 continue
                # else: 그렇지않다면, num을 계속 추가해줘라.
                continue
            else:
                result.append(num)
        return result

# (17) getMiddle메소드는 하나의 단어를 입력 받습니다. 단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요. 단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
# 예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.

def string_middle(str):
    if len(str) % 2 == 1:
        return str[len(str)//2]
    else:
        return str[len(str)//2 -1 : len(str)//2 + 1]

# (18) 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환해주는
# gcdlcm 함수를 완성해 보세요. 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 gcdlcm(3,12) 가 입력되면, [3, 12]를 반환해주면 됩니다.
# 최대 공약수는 12와 18이 있을때 18을 12로 나눈 나머지 6
# 12를 6으로 나눈 나머지 0
# 그러므로 최대 공약수는 6, 최소공배수는 두수의 곱을 최대 공약수로 나눠주기만 하면 된다.

def gcdlcm(a,b):
    c,d = max(a,b), min(a,b)
    t = 1
    while t >0:
        t = c % d
        c,d = d,t
    answer = [c, int(a*b/c)]

    return answer

def gcdlcm(a,b):
    if a<b:
        (a,b) = (b,a)
    while b!=0:
        (a,b) = (b, a%b)
        (c,d) = (a,b)
    answer = [c, int(a*b/c]


def gcdlcm(a,b):
        c,d = max(a,b),min(a,b)
        t = 1
        while t>0:
            t = c%d
            (a,b) = (b,a%b)
            (c,d) = (a,b)
        answer = [c,int(a*b/c)]


# (19) 행렬의 덧셈은 행과 열의 크기가 같은
# 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬을 입력받는 sumMatrix 함수를 완성하여
# 행렬 덧셈의 결과를 반환해 주세요.
# 예를 들어 2x2 행렬인
# A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면,
# 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다.
# 예를들면 A[0] = [1,2]이고 , A[0]=C, C[0] =1
# A[0] =[1,2]
# A[0] =C
# C[0] =1
# A[0][0] =1 , B[0][0] =3
# A[0][0] + B[0][0] = 4

def sumMatrix(A,B):
    answer = []
    for i range(len(A)):
        temp=[]
        for j in range(len(A[0])):
            temp.append(A[i][j] + B[i][j])
        answer.append(temp)
    return answer

# len(A) : 리스트안에 리스트가 있고,
# 정방행렬이므로 len(A): 전체길이는 2이다. 전체길이가 2이라는 것은
# (0,1) 2가지의 인덱스값이 들어간다.
# for i range(len(A)):
# 일단 temp라는 빈 리스트를 만들어준다. 밖의 리스트를 의미(리스트안에 리스트가 있기 때문에)
# i까지의 의미는 A=[[1,2],[2,3]]에서 [1,2]앞의 것만 꺼낸것을 의미
# len(A[0]= [1,2]에서 j인덱스의 j[0],j[1]값을 할당해줘야 한다. 그러므로
# for문에 for문을 돌려야 한다.
# for j in range(len(A[0])):
# 정방행렬의 경우 더할때는 자릿값이 일치하므로,
# temp 빈리스트에 넣어준다. ex) A[i][j] + B[i][j]에서 A,B에서 i값과 j값이 같기 떄문에
# 자릿값이 일치한대로 값을 더해줄 수 있다.
# 경우의수
# A00 + B00/A01 + B01/ A10+B10/ A11 +B11
# i[0]일경우 j의 인덱스는 j[0],j[1]이 되기 때문에
# for문을 2번돌린 결과는 A00+B00/A01+B01 값이 2개 산출된다.
# temp빈리스트에 일단 [4,6],[7,9]가 오면
# answer이라는 빈리스트에 또 추가하여 리스트를 감싸준다.
# [[4,6],[7,9]]





