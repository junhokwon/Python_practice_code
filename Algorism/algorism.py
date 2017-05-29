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


# (4) O와 X로 채워진 표가 있습니다.
# 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다.
# 표에서 O로 이루어진 가장 큰 정사각형을 찾아 넓이를 반환하는
# findLargestSquare 함수를 완성하세요.

    class Square:
        def __init__(self, board):
            self.width = len(board[0])
            self.height = len(board)
            self.board = board
            self.score = [[0] * self.width for row in range(self.height)]

        def get_char(self, x, y):
            return self.board[y][x]

        def set_score(self, x, y, value):
            self.score[y][x] = value

        def get_score(self, x, y):
            if x < 0 or y < 0:
                return 0

            return self.score[y][x]

    def findLargestSquare(board):
        s = Square(board)

        length = 0
        for y in range(s.height):
            for x in range(s.width):
                if s.get_char(x, y) == 'O':
                    s.set_score(
                        x, y,
                        min(s.get_score(x - 1, y - 1),
                            s.get_score(x - 1, y),
                            s.get_score(x, y - 1)) + 1)

                    length = max(length, s.get_score(x, y))

        print(s.score)

        return length * length
