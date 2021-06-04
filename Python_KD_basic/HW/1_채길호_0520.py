# 1번 1)문제
for i in range(5, 0, -1):
    for j in range(i):
        print('☆', end='')
    print()
# 다른 방법
for i in range(5): print('*' * (5-i))

# 1번 2)문제
for i in range(6):
    for j in range(5, i, -1):
        print(' ', end="")
    for z in range(i*2-1):
        print('☆', end='')
    print()
# 다른 방법
for i in range(1, 6):
    char = '*' * (2*i -1)
    print(f'{char : ^9s}') # ^9s 중앙 정렬 9자 문자열
# 다른 방법
for i in range(1,6):
    print(' '*(5-i) + '*'*(2*i-1))

# 2번 문제

an = input('숫자 입력 : ')
while True:    
    if an == "7":
        print('7 입력! 종료')
        break
    an = input('다시 입력 : ')

# 다른 방법
userInput = int(input('숫자 입력 : '))
while (userInput != 7):
    userInput = int(input('다시 입력 : '))
print('7 입력! 종료')


# 3번 문제
mo, s, c = 10000, 2000, 0
while mo > 0:
    c += 1
    print(f'노래를 {c}곡 불렀습니다.')
    if mo > 0:
        mo -= s
        if mo == 0:
            print('잔액이 없습니다. 종료합니다.')
            break
        else:
            print(f'현재 {mo}원 남았습니다.')
#다른 방법
f, balance, numSong = 2000, 10000, 0
while (balance >0):
    numSong += 1
    print(f'노래를 {numSong}곡을 불렀습니다.')
    if balance > 0:
        balance -= f
        if balance == 0:
            print('잔액이 없습니다. 종료합니다.')
            break
        else: print(f'현재 {balance}원 남았습니다.')
