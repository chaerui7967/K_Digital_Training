for name in ['홍길동', '이몽룡', '성춘향', '변학도']:
    print(name)

for i in range(0, 10):  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(i, end="\t")

# range(start[시작값,생략가능 기본 0], stop, 간격) range(11)= 0~10
for i in range(10, 100, 20):
    print(i, end=", ")

# 1~10 사이 숫자합
sum = 0
for i in range(101):
    sum += i
print("1 ~ 100 합 : %d" % sum)

# 1~20 3의배수 출력 합계
n=0
for i in range(3,20,3):
    n += i
    print(i, end="\t")
print('합계 : %d' %n)

