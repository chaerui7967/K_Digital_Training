#1~10 정수 출력
a = 1
while a <= 10:
    print(a,end='\t')
    a += 1

#continue
x=0
while x<10:
    x+=1
    if x % 2 ==0:
        continue
    print(x)

#무한 loop
while True:
    print('반복시작')
    answer = input('끝내려면 x')
    if answer == 'x':
        break
print('반복종료')