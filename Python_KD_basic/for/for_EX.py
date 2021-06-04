# 1~20 3의배수 출력 합계 range step(X)
sum=0
for i in range(20):
    if i % 3 == 0:
        sum += i
print('합계 : %d' % sum)

# 두 숫자 입력 두 숫자 사이의 합
sum=0
a, b = int(input('첫번째 숫자 : ')), int(input('두번째 숫자 : '))
for i in range(a, b+1):
    sum += i
print('합계 : %d' % sum)

# 단 수를 입력받아 해당 구구단 출력
d = int(input('단 수 입력 : '))
for i in range(10):
    print('%d * %d = %d' % (d, i, d*i))

# 카운트다운 프로그램
start = int(input('시작 숫자를 입력하시오 : '))
for i in range(start,0,-1):
    print(i, end="\t")
print('발사')

#numpy활용 한줄 작성

inputList = list()
for i in range(1,3):
    inputList.append(int(input(f'숫자 {i} 입력: ')))
inputList.sort()

import numpy as np
total = np.sum([i for i in range(inputList[0], inputList[1]+1)])
print(f'{inputList[0]}과 {inputList[1]} 사이의 합은 {total}')

#숫자 10개를 입력 받아서 양,음,0 갯수
p_c = m_c = z_c = 0
for i in range(10):
    a = int(input(f'숫자{i+1}입력 : '))
    if a > 0:
        p_c += 1
    elif a < 0:
        m_c += 1
    else:
        z_c += 1
print('-----------------')
print('양의 개수 : %d' % p_c)
print('음의 개수 : %d' % m_c)
print('0의 개수 : %d' % z_c)

# 이름 리스트에 해당하는 이름이 있는 경우 이름이 있음을 출력
names = ['홍길동', '이몽룡', '성춘향', '변학도']
in_name = input('이름입력 : ')

for i in names:
    if in_name == i:
        flag = True
        break
    else:
        flag = False

if flag:
    print('명단에 있습니다.')
else:
    print('명단에 없습니다.')

#☆출력1
for i in range(4):
    for j in range(5):
        print('☆', end=' ')
    print()

#☆2
for i in range(5):
    for j in range(i+1):
        print('☆', end=' ')
    print()

#☆3
for i in range(5, 0, -1):
    for j in range(i):
        print('☆', end='')
    print()

#☆4
mon='☆'
sp='  '
for i in range(5):
    for j in range(5, i, -1):
        print('%s' % sp, end="")
    for z in range(i*2-1):
        print('%s' % mon, end='')
    print()

