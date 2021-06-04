#함수의 매개변수
#함수에 전달(입력)되는 값  <- 매개변수
#전달하는 값 < -인수

def showInfo(name, age): #매개변수
    print(f'이름은 {name}이고 나이는 {age}')

showInfo('홍길동',20) #인수

#매개변수에 기본값 지정
def showMessage(message): # (m='ㅁㄴㅇㄹ')가능
    print(message)

def showMessage2(name, message='hello'): #매개변수(디폴트,변수) 는 안됨 맨뒤
    print(name,message)

showMessage('hello')
showMessage2('ddd','dadf')
showMessage2('hi')

def showInfo(name,age=10,sex='F'):
    print(name, age, sex)
# 함수에 리스트 전달
def showNames(names):
    for name in names:
        print(name,end=" ")
names = ['a','b','c','d']
showNames(names)

#딕셔너리 전달
def showInfoStd(student):
    print(student)
    print('이름 : ', student['name'])
    print('나이 : ', student['age'])
    print('연락처 : ', student['phone'])

info_std = {'name':'kim','age':19,'phone':'010-1111-2222'}
showInfoStd(info_std)

# 가변길이 매개변수
# *args : arguments를 1개 이상 사용가능
# *kwargs : keywhord arguments를 사용 key = value 형식으로 사용

def mySum(*args):
    total = 0
    for x in args:
        total += x
    return total
mySum(1,2,3,4,5,6,7)
mySum(1,2,3)

def myShowInfo(**kwargs):
    for key in kwargs.keys():
        print(key,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")
    print()
    for item in kwargs.items():
        print(item)

myShowInfo(id=123,name='kim',add='seoul')

def calculator(operator, *args):
    pass

def studentInfo(name,age,sex):
    student = {'name':name,
               'age':age,
               'sex':sex}
    return student
studentInfo('ee', 30, 'a')
studentInfo(name='kim',age=30,sex='f') #키 지정 시 위치순서 변경가능,
#키 지정 방식 사용시 키 지정방식은 위치인수 뒤로 와야함

