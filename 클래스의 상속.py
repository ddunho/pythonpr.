class BlackBox: #기본 블랙박스
    def __init__(self,name,price):
     self.name=name
     self.price=price

class TravelBlackBox: #여행 모드 지원 블랙박스
   def __init__(self,name,price):
      self.name=name
      self.price=price

   def set_travel_mode(self,min):
      print(str(min)+'분 동안 여행 모드 ON')

'''둘다 같은 def __init__(self,name,price): 함수를 쓰는데, 매번 쓰기가 번거로움
>>클래스의 상속 : 어떤 클래스로부터 사용한 모든 코드를 물려받아서 사용하고, 추가로 확장하여서 사용'''

class TravelBlackBox(BlackBox): #위와 똑같은 여행 모드 지원 블랙박스
   def set_travel_mode(self,min):
      print(str(min)+'분 동안 여행 모드 ON')

