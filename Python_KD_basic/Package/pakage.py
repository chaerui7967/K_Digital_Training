#파이참 이용을 안할시 __init__.py를 생성해야함
#import 패키지.모듈
#from 패키지.모듈 import 함수

import mypack.pack1.module11 as momo
momo.func11()
from mypack.pack1.module11 import *
func11() #함수 바로 사용가능
