class Monster():
    description = 'pocketmon'
    hp = 100
    dash_damage = 10

    def __init__(self,name):
        self.name = name


    def attack(self,enemy):
        self.enemy = enemy
        print('{}는 {}에게 {}피해를 줬다.'.format(self.name,self.enemy,self.dash_damage))
        enemy.hp = int(enemy.hp - (self.dash_dmage))
        return enemy.hp

class Item(Monster):
    hp = 10

    def __init__(self,name,item):
        super().__init__(name)
        self.item = item
        print('{}는 {}을 먹어서 체력이 {}만큼 회복되었습니다.'.format(self.name,self.item,self.hp))
        self.name.hp = int(self.name.hp + self.item.hp)




ggobugi = Monster('ggobugi')
ggobugi.attack('picakhu')
item = Item('ggobugi','물약')

