#상품가격, 주문수량 입력, 주문액을 출력 order()
def order():
    a=eval(input('상품가격 입력 : '))
    b=eval(input('주문수량 입력 : '))
    print('---------------')
    return a,b,a*b
aaa=order()
print(f'상품가격 : {aaa[0]}원\n주문수량 : {aaa[1]}개\n주문액 : {aaa[2]}원')

#이름과 나이를 입력받아서 딕셔너리 형식으로 반환
def myInfo():
    info=dict()
    name, age = input('이름, 나이 입력(","로 구분) : ').split(',')
    info['name'] = name
    info['age'] = int(age)
    return info
infoD = myInfo()
print(infoD)
#키값을 모를경우
print(infoD[list(infoD.keys())[0]])

for key, value in infoD.items():
    print(key,':',value)

for key in infoD.keys():
    print(key,':',infoD[key])

#사칙연산을 수행하는 함수들을 정의하여 호출
#add, sub, mul, div
def add(x,y): return x+y
def sub(x,y): return x-y
def mul(x,y): return x*y
def div(x,y): return x/y

x,y = int(input('숫자 1 입력 : ')), int(input('숫자 2 입력 : '))
print(f'{x} + {y} = {add(x,y)}\n{x} - {y} = {sub(x,y)}'
      f'\n{x} * {y} = {mul(x,y)}\n{x} / {y} = {div(x,y)}')

#order() 상품가격과 주문수량을 전달 주문액과 할인액, 지불액을 계산하여 반환
def order(a,b):
    cho, hal = a * b, 0
    if cho >= 100000:
        hal = cho*0.1
    elif cho >= 50000:
        hal = cho*0.05
    gi = cho - hal
    return cho, hal, gi

for i in range(3):
    price, amount = int(input('상품가격 입력 : ')), int(input('주문수량 입력 : '))
    print('-'*20)
    qty, discount, total = order(price, amount)
    print(f'주문액 : {qty:,}원\n할인액 : {int(discount):,}원\n지불액 : {int(total):,}원\n')
#오른쪽 정렬 format().rjust(문자수)

order=order(price,amount)
print('%s' %format(order[0],',').rjust(10))

#딕셔너리활용
def order(a,b):
    cho, hal = a * b, 0
    if cho >= 100000:
        hal = cho*0.1
    elif cho >= 50000:
        hal = cho*0.05
    gi = cho - hal
    dic = {'price':a,'qty':b,'amount':cho,'discount':hal,'total':gi}
    return dic
price, amount = int(input('상품가격 입력 : ')), int(input('주문수량 입력 : '))
print('-'*20)
orders = order(price, amount)
print(orders)
for i in orders.keys():
    print(f'{i} : {orders[i]}')

# 실습문제
def sub(x,y):
    global a
    a=7
    x,y = y,x
    b=3
    print(a,b,x,y)

a,b,x,y = 1,2,3,4
sub(x,y)
print(a,b,x,y)

#리스트는 함수에서 수정시 수정된다 주소값이 동일
def showList(mylist):
    mylist[0] = 100
    print(mylist)

mylist = [1,2,3,4]
showList(mylist)
print(mylist)

#실습
def getProduct(prdList):
    name = prdList['name']
    price = prdList['price']
    return {'name':name,'price':price}

productL = [{'name' : '노트북','price':123000, 'maker': 'LG'},
            {'name' : '노트','price':111000, 'maker': 'LG'},
            {'name': '북', 'price': 222000, 'maker': 'LG'}]

for pro in productL:
    prdInfo = getProduct(pro)
    print(prdInfo)

# 팩토리얼 함수정의
# n! = n*(n-1)*...
def factorial(n):
    a=n
    for i in range(a-1,0,-1):
        a*=i
    return a
print(factorial(4))

#다른방법 재귀함수
def factorial(n):
    return n*factorial(n-1) if n>1 else 1

#연습 filter 사용 짝수 반환 함수
def even(x):    return x%2==0
result = list(filter(even, [2,3,4,5,6,7]))
print(result)

#다른방법
def isEven(inputData):
    if isinstance(inputData, list) or isinstance(inputData, tuple):
        result = filter(lambda x: x%2 == 0, inputData)
        if isinstance(inputData, list): result = list(result)
        else: result = tuple(result)
        return result
    else:
        raise Exception

# TEST
from random import randint
testData = [randint(0, 100) for i in range(10)]
print(f"Test data created: {testData}\nFiltered result: {isEven(testData)}")

#재귀함수 연습
aa = int(input('숫자입력 : '))
def sun(aa):
    print(aa, end=" ")
    if aa>0:
        return sun(aa-1)
    else:
        return
sun(aa)

#다른
def count(num):
    if num:
        print(num, end=' ')
        return count(num-1)

count(49)

a=10
def selfcall():
    global a
    a-=1
    print('ha', end='')
    if a < 1:
        return
    return selfcall()

#두개의 리스트의 같은 인덱스 요소의 값을 더해서 하나의 리스트를 출력
#1 def 함수 정의
listA = [1,2,3,4]
listB = [10,20,30,40]
def result1(a,b):
    newL = []
    for i in range(len(a)):
        newL.append(a[i]+b[i])
    return newL
print(result1(listA,listB))

#다른 방법
def hap(a,b):    return [x+y for x, y in zip(a,b)]


#2 lambda 표현식 정의
print(list(map(lambda x,y : x+y,listA,listB)))

##다른 방법
from random import randint

list1 = [randint(1,10) for i in range(4)]
list2 = [randint(11,40) for i in range(4)]

def addList(list1, list2):
    resultList = list()
    for i, j in zip(list1, list2): resultList.append(i+j)
    return resultList

# OR

addList = lambda x,y: [i+j for i,j in zip(x,y)]

addList(list1, list2)