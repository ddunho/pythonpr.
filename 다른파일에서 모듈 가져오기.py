'''import 모듈
from 모듈 import 변수,함수 또는 클래스''' #다른파일에서 모듈 가져오기

#예시가 있을때, 
good.job.py
def say():
    print('참 잘했어요')

import good.job #모듈을 가져와서 모듈에 포함된 모든 기능을 쓸수있도록한다
good.job.say()

from good.job import say #모듈중에서 say()함수만 가져다가 쓰겠다.
say()