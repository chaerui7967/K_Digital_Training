#내장 함수 ~~all(내용) 내용이 모두 참일때 true, any() 내용이 하나라도 참이면 true
all(['','123',1])
any([0,1,2,3])
#아스키코드 chr
chr(65)
#문자를 아스키코드
ord('A')
#eval() 주어진 표현식을 계산해서 출력
eval('4+5')
#함수설명 help(함수)
#pow() 거듭제곱
pow(2,3) #8
#min , max
#divmod 몫과 나머지를 튜플형태 출력
divmod(7,3) #(몫,나머지)
#sum
#round() 반올림
round(9.87,1)
#abs 절댓값
#enumerate() 리스트 앞에 인덱스를 생성
aa=enumerate(['1','2','3'],start=1) #start 기본값은 0
#출력
for i, item in aa:
    print(i,item)

aa1 = ['Spring', 'Summer', 'Fall', 'Winter']
enumA1 = list(enumerate(aa1))
print(enumA1)

#filter(함수, iteroble자료형) : 반복가능한 자료형 요소에 반환값이
# 참,거짓인 함수를 적용하여 반환값이 참인것의 변수 값 출력
def positive(x):    return x>0
result = filter(positive,[-10,0,3,-1])
print(list(result))

# enumerate를 객체 주소로 받는 경우 __next()__나 __iter__()를 통해서 구성요소를 참조할때마다
# 삭제 그래서 각각 1회 참조할수있다고 합니다.
enum = enumerate(['apple', 'banana', 'melon'])
aa = ['apple', 'banana', 'melon']
for e in enum: #해결방법은 대입한 변수 대신 직접 함수를 집어넣으면 됨 for e in enumerate(~~)
    print(e)

print(enum)
print(list(enum))

#list()
#sorted(iterable, key=none,reverse=False)
print(sorted([10,-3,-2],reverse=True))
print(sorted("flower"))
print(sorted("flowEr", key=str.lower))
#range
#open(파일이름, (모드[파일용도r읽기(기본),w쓰기,a추가,b바이러니])
#zip(*iterable) : 각 iterable객체에서 동일한 인덱스를 묶어 출력
zip([1,23,4,5],[-1,-23,-4,-5])
print(list(zip([1,23,4,5],[-1,-23,-4,-5])))

#map(함수, iterable)
a = [1.2, 2.3, 12.3]
a = list(map(int, a))
print(list(map(str, a)))

#lambda 식
def add(a,b):   return a+b

