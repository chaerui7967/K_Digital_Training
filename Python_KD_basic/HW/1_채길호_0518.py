# 1. 16진수 구분 코드 작성
num = input('16진수 한 글자 입력 : ').upper()
if(num >= 'A' and num <= 'F'):
    result = int(num, 16)
    print("10진수 ==> %d" %result)
elif (num >= '0' and num <= '9'):
    result = int(num)
    print("10진수 ==> %d" % result)
else:
    print("16진수가 아닙니다.")

# 2. 잔돈 교환 프로그래밍
ex = int(input('교환할 돈은 얼마?'))
co_50000 = ex // 50000
ex %= 50000
co_10000 = ex // 10000
ex %= 10000
co_5000 = ex // 5000
ex %= 5000
co_1000 = ex // 1000
ex %= 1000
co_500 = ex // 500
ex %= 500
co_100 = ex // 100
ex %= 100
co_50 = ex // 50
ex %= 50
co_10 = ex // 10
ex %= 10
r = ex % 10
print('50000원 %d장, 10000원 %d장, 5000원 %d장, '
      '1000원 %d장, 500원 %d장, 100원 %d장, 50원 %d장, 10원 %d장'
      %(co_50000, co_10000, co_5000, co_1000, co_500, co_100, co_50, co_10))
print('바꾸지 못한 돈 ==> %d' %r)

# 3. 주사위게임
from random import randint #randrange(1,7)도 가능
A_num = randint(1, 6)
B_num = randint(1, 6)
print('A의 주사위 숫자는 %d 입니다.' % A_num)
print('B의 주사위 숫자는 %d 입니다.' % B_num)
if A_num > B_num:
    print('A가 이겼습니다.')
elif A_num < B_num:
    print('B가 이겼습니다.')
else:
    print('비겼습니다.')

