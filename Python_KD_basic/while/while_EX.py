#1~100 모든 3의 배수의 합
a = 0
sum = 0
while a <= 100:
    if a % 3 == 0:
        sum += a
        a += 1
    else:
        a += 1
print(f'1부터 100까지의 모든 3의 배수의 합은 {sum}입니다.')

#if문 제거
while a <= 100:
    sum += a
    a += 3

#원하는 입력을 얻을때까지
while True:
    an = input('숫자 입력 : ')
    if an == "7":
        break
