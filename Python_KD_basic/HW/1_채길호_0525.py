#1 비트코인 문자열을 화면에 출력하는 함수정의
def print_coin():    print('비트코인')

#2
print_coin()
'''
#3
for i in range(100):    print_coin()

#4
def print_coins():    for i in range(100): print('비트코인')
'''
#5
#==> 사용자 정의 함수가 정의되기 전에 호출해서 에러가 발생합니다.
##수정코드
def hello():    print('Hi')
hello()
print()

#6
print('6번----------내 예측---------\nA\nB\nC\nA\nB')
print('----------결과------------')

def message():
    print('A')
    print('B')
message()
print('C')
message()
print()

#7
print('7번----------내 예측---------\nA\nA\nC\nB')
print('----------결과------------')

print('A')
def message():
    print('B')
print('A')
print('C')
message()
print()

#8
print('8번----------내 예측---------\nA\nC\nB\nE\nD')
print('----------결과------------')

print('A')
def message1():
    print('B')
print('C')
def message2():
    print('D')
message1()
print('E')
message2()

#9
print('9번----------내 예측---------\nB\nA')
print('----------결과------------')

def message1():
    print('A')
def message2():
    print('B')
    message1()

message2()
print()

#10
print('10번----------내 예측---------\nB\nC\nB\nC\nB\nC\nA')
print('----------결과------------')

def message1():
    print('A')
def message2():
    print('B')
def message3():
    for i in range(3):
        message2()
        print('C')
    message1()
message3()
print()

#11
def mul():
    a, b = int(input('숫자1 :')),int(input('숫자2 :'))
    return a*b
print(f'11번 결과 = {mul()}')
print()

#12
def Upper(ticker):    return ticker.upper()
print(f'ticker 대문자 변환 -> {Upper("ticker")}')
print()

#13
def pickup_even(numL):
    Num = []
    for i in numL:
        if i%2 ==0:
            Num.append(i)
    return Num
aa = [1,2,3,4,5,6,7,8,9]
print(f'{aa}에서 짝수만 추출\n -> {pickup_even(aa)}')

##다른 사람 코드 수정
def sootja():
    e=[]
    while 1:
        n= input('숫자를 입력하세요.(엔터키 누르면 종료) : ')
        if n:   e.append(int(n))
        else:   break
    return e

def pickup_even():
    e = sootja()
    f = []
    for i in e:
        if i % 2 == 0:    f.append(i)
    return f
print(pickup_even())
