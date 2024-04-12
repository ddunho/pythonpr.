#1 
gun = 10 


def checkpoint(soldiers): # 경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
    
#3
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
#checkpoint(2) #2명이 경계 근무를 나감
#2
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun)) #에러가 뜸 > gun은 지역변수이기 때문 ; def함수 밑에 gun =20을 쓰면 출력됨
#global gun 을 추가해도 출력됨



'''코드 전체 설명
1-gun = 10 이라는 변수 정의
2-변수를 넘겨서 내부에서 계산
3-변경된 값을 리턴'''
