#문자열의 기본
crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'
print(crawling, parsing, sep="\n")
print(type(crawling), type(parsing), sep='\n')

#문자열 연산가능 +*
print('a'+'b')
print('hi'*5)

#slicing 문자열의 일부분 추출
print(crawling[0])
print(crawling[-1])
print(crawling[1:5])
print(crawling[:-1])
print(crawling[-1:])
print(crawling[:])
print(crawling[0:10])

#in
string = 'Python programming'
print('python' in string)
if 'Python' in string:
    print('o')
else:
    print('x')

#예제
names = ['홍길동', '성춘향', '이몽룡', '변학도']
Name = input('input name: ')

if Name in names:
    print('oo')
else:
    print('no')
