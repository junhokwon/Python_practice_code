class Monster():
    description = 'pocketmon'
    hp = 100
    dash_damage = 10

    def __init__(self,name):
        self.name = name


    def attack(self,enemy):
        print('{}는 {}에게 {}피해를 줬다.'.format(self.name,enemy.name,self.dash_damage))
        enemy.hp = int(enemy.hp - self.dash_damage)
        return enemy.hp


class posion():
    hp = 10

    def __init__(self,name):
        self.name = name

    def drink(self,monster):
        monster.hp += self.hp
        print('{}은 {}을 먹어서 {}만큼 회복되었습니다.'
              .format(monster.name,self.name,self.hp))
        return monster.hp

ggobugi = Monster('ggobugi')
pikachu = Monster('pikachu')

#인스턴스(객체)를 pikachu에다 할당했기에

ggobugi.attack(pikachu)
# enemy 매개변수에 실행인자로 객체(pikachu)를 넣는다.
print(pikachu.hp)

redposion = posion('redposion')
redposion.drink(pikachu)
print(pikachu.hp)


