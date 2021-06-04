#다중 for문
for y in range(3):
    for x in range(5):
        print(x, end="  ")
    print()

#숫자 순서대로 출력
for i in range(3):
    for j in range(1, 5):
        print('%3s' %(j + i*4), end=" ")
    print()

a = 0
for i in range(3):
    for j in range(4):
        a += 1
        print(a, end="\t")
    print()

#구구단 출력
for dan in range(2,10):
    for n in range(1,10):
        print('%d * %d = %d' %(dan, n, dan * n))
    print()
