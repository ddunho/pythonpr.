def profile(name, age, main_lang):
    print(name, age,main_lang)

profile("유재석", 20, "파이썬")
profile(name="유재석", main_lang ="파이썬", age=20)
profile(main_lang = "자바", age=25, name="김태호")
'''함수에서 전달받는 매개변수의 값을 키워드로 이용해서 호출하면, 키워드 = 값을 입력해주면 순서가 달라도 출력이 된다.'''