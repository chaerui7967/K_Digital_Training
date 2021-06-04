# 클래스 선언/ 구현: 메서드, 필드, 생성자 정의
# 변수 =  클래스 이름 >>객체, 인스턴스
# class 클래스 이름(슈퍼 클래스명) :
# 필드(속성)1
# 필드(속성)2
#       def~

# class Car:
#     pass
# car1 = Car() #인스턴스 생성

class Car:
    #메소드 정의
    def show(self):
        print('시험중입니다')

car1 = Car()
car2 = Car()
car3 = Car()

car1.show() #메소드 호출

#특정 클래스의 인스턴스인지 확인: isinstance(인스턴스명, 클래스명)
print(isinstance(car1,Car))
print(isinstance(car1,int))
a=True #True==1
print(isinstance(a, int)) #결과 True

#파이썬 기본 제공 = int,float,bool,str,,, => 클래스
#instance & object
#같은것을 가리키고 있음
#instance 는 클래스와 연관되어 이야기할 때 사용

#필드 추가 : 메소드 내에서 정의 후 사용
class Car:
    # speed = 0
    # color = 'black'
    def show(self):
        print('시험중입니다')
    def drive(self, speed):
        self.speed = speed # speed 필드
        print(f'{speed}로 주행중 ')

#메인 : 인스턴스를 생성 하고 이용
car1 = Car()
car1.drive(70)
car1.speed
print(car1.speed)
car1.speed =100

#인스턴스.필드 선언 or class 내에서 선언
car1.color = 'red'
car1.color

#클레스에서 필드 선언
class Car:
    speed = 0
    color = 'black'
    def show(self):
        print('시험중입니다')
    def drive(self):
        print(f'{self.speed}로 주행중 ')

mycar = Car() #<- 기본생성자
print(mycar.speed)
mycar.drive()

# 생성자 : 인스턴스를 생성해주는 함수
class Car:
    def __init__(self): #기본 생성자 : 인스턴스 호출=> 인스턴스명.클래스이름()
        self.color = 'white'
        self.speed = 0
    def drive(self):
        print(f'{self.speed}로 주행중')
    def showInfo(self):
        print(f'이 자동차의 색상은 {self.color}')

mycar = Car()
print(mycar.color)
mycar.speed=50
mycar.color='black'
mycar.showInfo()
mycar.drive()

# 매개변수가 있는 생성자
class Car:
    def __init__(self,color,speed): #매개변수 입력
        self.color = color
        self.speed = speed
    def drive(self):
        print(f'{self.speed}로 주행중')
    def showInfo(self):
        print(f'이 자동차의 색상은 {self.color}')

# mycar = Car() #오류// 변수 입력
mycar= Car('white',800)
print(mycar.color)
mycar.speed=50
mycar.color='black'
mycar.showInfo()
mycar.drive()

#여러개의 매개변수
class Car:
    def __init__(self,speed=0,color='white'): #기본 생성자 : 인스턴스 호출=> 인스턴스명.클래스이름()
        self.color = color
        self.speed = speed
    def drive(self):
        print(f'{self.speed}로 주행중')
    def showInfo(self):
        print(f'이 자동차의 색상은 {self.color}')

mycar = Car()
yourcar = Car(color='yellow')
car2 =Car(10,'blue')
mycar.showInfo()
yourcar.showInfo()
car2.showInfo()