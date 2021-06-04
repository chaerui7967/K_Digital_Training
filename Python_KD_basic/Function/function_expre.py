#재귀함수
def factorial(n):
    return n*factorial(n-1) if n>1 else 1

#lambda 식 함수내 새로운 변수 지정 불가 lambda x: y=10, x+y 불가
hap = lambda x, y : x+y
print((lambda x,y : x+y)(10,50))
print(hap(5,10))
hap3 = lambda x=10,y=20 : x+y
print(hap3())
print(hap3(2,3))

#람다 함수 이용
#리스트의 값에 각각 10을 더하는 람다함수
lsitA = [1,2,3,4]
list(map(lambda x : x+10,lsitA))

#활용
NS = int(input('학생 수 입력 : '))
Scorelist = list()

for i in range(NS):
    Scorelist.append(int(input(f"학생{i+1} 점수 입력 : ")))
Total = sum(Scorelist)
print(f'총점 : {Total}\n평균 : {Total / len(Scorelist)}\n80점 이상 학생 : '
      f'{len(list(filter(lambda x: x>= 80,Scorelist)))}명')


#내부함수
def outfunc(x,y):
    def infunc(a,b):
        return  a+b
    return  infunc(x,y)

