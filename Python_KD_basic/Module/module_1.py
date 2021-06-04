#표준모듈
import sys #지정한 모듈 전체 참조 == from sys import *
bmodule = sys.builtin_module_names
print(bmodule)
#dir(sys) 해당모듈과 관련된 함수들 출력
#별명 import pandas as pd
#from 모듈명 import 변수명,... 모듈내에서 일부만 참조

#만든 모듈 사용 calculator 같은 폴더 내에
import calculator
a = calculator.add(1, 2)

#다른 폴더
import module.showInfo as dd
dd.show_name()

#라이브러리 path 설정
#setting -> 인터프리터
import showInfo
showInfo.show_name()

import calculator
print(calculator.add(1,2))

#main 모듈
import moduleMain as mm
print(mm.main())

from Module import *