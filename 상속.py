#일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

#공격유닛
class Attackunit(unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  #Unit을 상속 >이전과 똑같이 상속
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))