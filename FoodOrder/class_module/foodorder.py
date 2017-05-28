class Mcdonalds:
    '''맥도날드 매장'''
    def __init__(self,name=None):
        self.__name = name
        self.money = 1000000

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        print('매장 이름 : 맥도날드 {}'.format(self.name))

class Worker:
    '''직원'''
    def __init__(self, name=None):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name
        print('직원 이름 : {}'.format(self.name))

class Burger:
    ''''''
    def __init__(self,name,price):
        self.name = name
        self.price = price


