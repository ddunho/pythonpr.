try:
    result=num1/num2
except ZeroDivisionError: #어떤 에러가 발생했는지 알  수있다.
    print('0으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err:
    print('에러가 발생했어요:', err)