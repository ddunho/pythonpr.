#구글에 pypi를 검색 > 코드를 선택 후 복사한다음에 Terminal에 붙여넣기 후 엔터
#Quick Start를 긁어온다
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

'''Terminal에 
pip list 를 치면 , 현재 설치되어있는 패키지 내용 확인가능
pip show 를 치면 , 현재 설치되어있는 패키지의 정보 확인 가능
pip install --upgrade beautifulsoup4를 치면 최신버젼 업그레이드
pip uninstall beautifulsoup4를 치면 패키지 삭제'''
