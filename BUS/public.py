class Bus:
    'doc string '
    def __init__(self, name, price, time, distance):
        self.name = name
        self.__price = price
        #private 설정 : 남이 건드릴 수 없게 설정
        self.time = time
        self.distance = distance

    def info(self):
        print('{}버스의 이동비용은 {}원이고, 시간은 {}시간 걸리고, 이동거리는 {}km 이다'.format(self.name, self.__price, self.time, self.distance))

    def total_fee(self,next_bus):
        self.next_bus = next_bus
        print('{}버스와 {}버스의 총 비용은 {}원입니다.'.format(self.name, self.next_bus.name, self.__price + self.next_bus.price))

    def total_distance(self,next_bus):
        self.next_bus = next_bus
        print('{}버스와 {}버스의 총 이동거리는 {}km입니다'.format(self.name,self.next_bus.name,self.distance + self.next_bus.distance))

    def total_time(self,next_bus):
        self.next_bus = next_bus
        print('{}버스와 {}버스의 총 이동시간은 {}시간입니다'.format(self.name,self.next_bus.name,self.time + self.next_bus.time))

    @property
    # 읽기전용
    def price(self):
        return self.__price

    @price.setter
    # 쓰기전용
    def price(self, new_price):
        self.__price = new_price
        print('set new price : ({}원)'.format(self.__price))