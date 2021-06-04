# 서브클래스 (슈퍼클래스)

class Car:
    number = 0
    def __init__(self,speed=0,color='white'):
        self.speed = speed
        self.color = color
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


class Truck(Car): #서브클래스
    def __init__(self,speed,color,load):
        super().__init__(speed,color) #부모 객체 사용
        self.load = load
    #메소드 재정의 : 오버라이딩
    def showLoad(self):
        print(self.load)

    def showInfo(self):
        print(f'속도는 {self.speed}, 적재양 {self.load}')

class SportCar(Car):
    def __init__(self, speed, color, seat):
        super().__init__(speed,color)
        self.seat = seat

    def showInfo(self):
        print(f'{self.speed} , {self.color}, {self.seat}')

car1 = Car()
car2 = Truck(0,'blue',1000)
car3 = SportCar(0,'red',2)
# car1.showInfo()
# car2.showInfo()
# car2.showLoad()
# print(car2)
#
# print(isinstance(car2,Car))
# print(issubclass(Truck,Car))
# print(issubclass(bool,int))
# car3.showInfo()
