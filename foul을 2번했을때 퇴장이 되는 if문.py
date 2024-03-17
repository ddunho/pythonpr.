yellow_card = 0
foul = True
if foul:
    yellow_card +=1
    if yellow_card ==2 :
        print('경고 누적 퇴장')
    else: #yellow_card가 2가아닐때
        print('휴 조심해야지')

else : #foul이 아닐때
    print('주의')
