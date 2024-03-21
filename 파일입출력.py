f=open('list.txt','r',encoding='utf8') #읽기모드로 파일 열기
for line in f:
    print(line, end='') #파일을 한줄씩 읽기, end=''빈칸으로 설정해주지않으면, 불필요한 줄이 생길수있음
f.write('김xx\n') #문장 입력하기
f.close() #파일 닫기

'''파일입출력에서, w(write)=쓰기, r(read)=읽기, a(append)=이어서 쓰기
   open(파일명,열기 모드,encoding='인코딩')이며, 파일명이 없을때는 새로 생성함'''

