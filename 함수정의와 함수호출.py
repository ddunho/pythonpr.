def get_price(is_vip): #함수정의, 괄호안은 불리안 형태 > true이면 단골, false이면 일반손님
    if is_vip == True:
        return 10000 #단골손님
    else:
        return 15000 #일반손님
#반환값은 여러개 반환가능하고, 반환되는 즉시 함수 탈출
price = get_price(True) #함수 호출

print(f'커트 가격은 {price}원 입니다')