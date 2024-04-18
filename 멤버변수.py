class unit :
    def _init_(self, name,hp,damage):
        self.name= name #멤버변수
        self.hp = hp
        self.hp = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

#레이스 : 공중 유닛, 비행기, 클로킹(상대에게 보이지않음)
wraith = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage) )

#마인드 컨트롤 : 상대방 유닛을 내것으로 만듦
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clockin == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))


#wraith2에는 클로킹 가능하지만, wraith1은 x > 확장된 변수는 확장한 개체에 대해서만 적용됨