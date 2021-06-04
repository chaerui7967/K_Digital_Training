#함수의 반환값 : return 없는 경우 None 출력
def sum():
    a = int(input('숫자1 입력 : '))
    b = int(input('숫자2 입력 : '))
    return a+b
print(sum())
res = sum()
print('%d' %res)
print('%d' %sum())

#연습
#삼각형의 넓이 계산 함수 get_triangle_area()
#높이와 밑변길이를 입력받음
def get_triangle_area():
    a = int(input('높이 : '))
    b = int(input('밑변 : '))
    return a*b/2 #여러개의 반환값을 가질수 있음
print('삼각형의 면적 : %d' %get_triangle_area())

#반환값이 여러개일 경우 반환값이 튜플형태로 출력 return이 여러개일경우 맨 위 return만 출력
def get_triangle_area():
    a = int(input('높이 : '))
    b = int(input('밑변 : '))
    return a,b,a*b/2

print(f'삼각형의 면적 : {get_triangle_area()}')

#리스트 반환값
def getName():
    names=[]
    for i in range(3):
        name = input('이름 입력 : ')
        names.append(name)
    return  names

nameL = getName()
print(nameL)