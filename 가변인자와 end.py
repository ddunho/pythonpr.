def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " : 이 문장을 출력하고, 이어서 밑문장을 출력 
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "" , "")

#언어가 늘어나거나, 적으면 항상 쳐줘야함 >> 가변인자 사용


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end=" ")
