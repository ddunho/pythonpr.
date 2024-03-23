class BlackBox:
    def __init__(self,name,price): #클래스
        self.name=name
        self.price=price
    def set_travel_mode(self): #메소드
        print('여행 모드 ON')

    b1=BlackBox('까망이',200000)
    b1.set_travel_mode() #>실행결과 : 여행모드On

    def set_travel_mode(self,min): #여행모드시간(분)> 전달값
        print(str(min)+'분 동안 여행모드 ON')

    b1=BlackBox('까망이',200000)
    b1.set_travel_mode(20) #20분만 작동>실행결과 : 20분동안 여행 모드 ON
    