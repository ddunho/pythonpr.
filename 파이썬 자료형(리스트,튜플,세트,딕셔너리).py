my_tuple =('오예스','몽쉘')
my_list = list(my_tuple) #튜플이 리스트형태로 바뀜
my_list.append('초코파이')
my_tuple=tuple(my_list) #리스트를 다시 튜플형태로 > 수정불가능한 튜플에 추가할수있는방법
print(my_tuple)

my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_set = set(my_list) #리스트를 세트형태로 바뀜 > 리스트는 중복허용,세트는 중복허용x 중복을 없애고싶을때 사용하는 방법
print(my_set) # 세트는 순서x > 랜덤으로 나옴, 순서를 지키고싶다면 딕셔너리 사용

my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_dic = dict.fromkeys(my_list) #key를 가지며, value값은 none 인것
print(my_dic)