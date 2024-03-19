drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == "시즌3":
        print('재미없대,건너뛰자')
        continue #동작을 이어서 건너뛰고싶을때 사용
    print(f'{x} 시청')
        