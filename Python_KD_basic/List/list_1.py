#리스트의 기본 개념
intL = [1,2,3,4,5]
floatL = [1.1,2.3,4.2]
nameL = ['홍길동', '성춘향', '변학도', '방자']
numL = [1,3,4, [1,2]]
samL = [1,2,3,.5,'gkgk']

a,b,c = floatL
print(a,b,c,sep='\n')

#인덱싱
numL[0]
numL[:]
numL[1:3]
numL[3][0]

#임의의 리스트 생성
allL = []
allL = list()

allL = [intL, floatL, nameL, numL]
allL[-1][-1][0]

#리스트 병합 및 연산
sumL = numL + samL
sumL
numL * 3

#리스트 내용 변경
numL[-1] = 10
numL[2:4] = []
numL

# 리스트 복사
# 얕은 복사 주소만 참조
score = [65, 70, 90, 89, 78]
value = score
print(score,"\n",value)

score[3] = 98
print(score,'\n',value)

value[0] = 100
print(score,'\n',value)

# 리스트 복사
# 깊은 복사 deep copy
value2 = score.copy()
print(score,value2,sep='\n')
score[0] = 50
print(score,value2,sep='\n')

value3 = list(score)
print(score,value3,sep='\n')
score[0] = 150
print(score,value3,sep='\n')

import copy
value4 = copy.deepcopy(score)