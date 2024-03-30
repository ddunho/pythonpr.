from random import *

print(random()) #0.0이상 1.0미만의 임의의 값 생성
print(random() *10) #0.0이상 10.0 미만의 임의의 값 생성
print(int(random() *10)) #0이상 10 미만의 임의의 정수값 생성
print(int(random()*10)+1)  #1이상 10미만의 임의의 정수값 생성

print(int(random()*45)+1) #1이상 45 이하의 임의의 정수값 생성 : 로또번호
print(randint(1,45)) #위와 같음
print(randrange(1,46)) #위와 같음;46인것에 주의 44.25