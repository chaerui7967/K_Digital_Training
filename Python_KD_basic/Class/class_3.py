#인스턴스 변수와 클래스 변수
class Car:
    number = 0
    def __init__(self,speed=0,color='white'):
        self.color = color
        self.speed = speed
        Car.number +=1 #클래스 변수 몇개의 클래스가 만들어졌는지

    def __str__(self):
        return '끝'

    def showColor(self): #비공개 메소드
        print(f'이 자동차의 색상은 {self.color}')

    def showInfo(self):
        self.showColor()
        print(f'이 자동차의 색상은 {self.color}')

    def drive(self):
        print(f'{self.speed}로 주행중')

car1 = Car()
car2 = Car(10,'blue')
# 인스턴스 변수(필드)
print(car1.speed)
print(car2.speed)

#클래스 변수 공통된 변수
print(car1.number)
print(car2.number)

