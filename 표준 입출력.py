print("Python", "Java", sep=",") #sep를 통해 띄어쓸지, 안할지 지정할수있음
print("Pyhon", "Java", sep=",", end="?") #end를 통해 한번에 출력가능
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) #표준출력
print("Python", "Java", file=sys.stderr) #표준 에러

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items(): #.items : 키(subject)와 벨류(score)을 튜플로 보내줌
    print(subject, score)
    print(subject.ljust(8), str(score)) #ljust(8) 왼쪽으로부터 정렬하고, 8칸의 공간확보, rjust(8)은 오른쪽정렬
          
          
