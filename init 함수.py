class BlackBox:
    def __init__(self,name,price): #이 클래스는 name과 price라는 변수를 가지고있다. init함수는 객체가 생성될때 자동으로 실행됨
        self.name=name
        self.name=price
        
b1=Blackbox('까망이',200000)
print(b1.name,b1.price)
b2=Blackbox('하양이',100000)
print(b2.name,b2.price)