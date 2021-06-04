#연습문제1
Id, Pw = 'flower', 1234
aa, bb = input('아이디 입력 : ') , input('비밀번호 입력 : ')

if(aa == Id and str(Pw) == bb):
    print('로그인 성공!')
else:
    print('로그인 실패!')

#입력받은 정수가 양수,음수,0

num = int(input('정수 입력 : '))

if num > 0:
    print('양수')
elif num < 0:
    print('음수')
else:
    print('0')

# 정수 3개 입력받아서 제일 큰 수를 출력
a, b, c = map(int,input('정수 3개 입력: ').split(','))
if (a>b and a>c):
    max_num=a
elif (b>c):
    max_num=b
else:
    max_num=c
print('제일 큰 수 : %d' %max_num)

# 컴퓨터와 게임
from random import randint
Cn= randint(1, 100)
Mn= randint(1, 100)

if Mn>Cn:
    print('Win')
else:
    print('Fale')

#연습문제2
# 도형을 선택해서 면적 구하기
sel = int(input('1:사각형, 2:삼각형, 3:원'))
if sel==1:
    W, H = int(input('가로 입력: ')), int(input('세로 입력: '))
    result = W*H
    print('사각형의 면적 = %d' %result)
elif sel==2:
    W, H = int(input('밑변 입력: ')), int(input('높이 입력: '))
    result = W * H /2
    print('삼각형의 면적 = %d' % result)
elif sel==3:
    R = int(input('반지름 입력: '))
    result = R * 3.1416
    print('원의 면적 = %f' % result)
else:
    print('1,2,3 중 하나를 선택')

