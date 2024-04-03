#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
'''예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이훌 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 '''

url = "http://naver.com"
my_str = url.replace("http://", "") #규칙1
my_str = my_str[:my_str.index(".")] #규칙2 ; my_str에서 처음부터 . 전까지

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" #규칙3 : len, count는 정수로 나오기때문에, str로 감싸줌
print("{0}의 비밀번호는 {1} 입니다.".format(url, password)) #format은 변수출력을 위한 포맷팅


