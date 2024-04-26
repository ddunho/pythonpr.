#내장함수에 대해 알아보기
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

#dir : 어떤 객체를 넘겨줬을 때 , 그 객체가 어떤 변수와 함수를 가지고있는지 표시
print(dir()) #
import random #외장 함수
print(dir())
import pickle
print(dir())

print(dir(random)) #random 모듈 내에서 사용할수있는것 표시
#random. 과 유사한 기능

lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name))

#구글에 list of pyhon builtins 검색 > 내장함수 확인 가능

