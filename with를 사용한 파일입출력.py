f=open('list.txt','w',encoding='utf8')
#with를 사용하면 파일을 자동으로 닫아줌
with open('list.txt','w',encoding='utf8')as f: #f는 변수
 f.write('김xx\n')
#파일을 안닫아도 됨