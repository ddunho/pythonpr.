'''class 클래스명:
    정의'''
class BlackBox: #대문자는 단어단위로 해주면됨
    pass
b1=BlackBox()
b1.name= '까망이'
print(b1.name)#실행결과 = 까망이
print(isinstance(b1,BlackBox))
#>실행결과 True이면 인스턴스가 맞는것.
