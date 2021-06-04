#함수 - 특정 작업을 수행하는 코드 집합
#내장 함수 print, input, type ...
#문자열.sort ... 메소드
#사용자 지정 함수 def + 간단한 활용
def printHello():
    print('hello')

def printName(name):
    print(name)

def area_sqaure(width, height):
    area = width * height
    return area
w=10
h=20
area = area_sqaure(w,h)
print(area)
printHello()
printName('chae')

#연습문제
def show_info():
    print('채길호\n500\n010-5000-5050')

show_info()

#연습2 sum()
def sum():
    a, b= eval(input('숫자1 입력 : ')), eval(input('숫자2 입력 : '))
    print(f'합 : {a+b}')

sum()