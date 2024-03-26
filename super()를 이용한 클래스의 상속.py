class BlackBox: #기본 블랙박스
    def __init__(self,name,price):
        self.name=name
        self.price=price

class TravelBlackBox(BlackBox): #기본블랙박스에게 상속받음
    self.sd=sd #새로운 확장 ; sd카드 추가

'''기본 블랙박스에서는 name과 price를 받아서 멤버변수를 정의해주고있고, 여행모드블랙박스에서는 기존 블랙박스+ 추가로 sd카드 데이터를 정의해주는것이다.
   이 때, name과 price부분을 기존의 것을 사용하는게 좋을텐데, 이는 밑으로 나타낼 수 있다.'''

class TravelBlackBox(BlackBox):
    def __init__(self,name,price,sd):
     BlackBox.__init__(self,name,price)  #이것은 super().__init__(name,price)로 나타낼 수 있다. super() : 부모클래스에서 호출하고자할떄 사용,  self 필요 x
     self.sd=sd

