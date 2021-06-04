#_의 쓰임
#_1개 변수에 특별한 이름을 부여하고 싶지 않을때
for _ in range(10):
    print('a')
#_2개 : __ 특수한 예약 함수나 변수에 사용
#__str__ :클래스로 인스턴스를 생성했을 때 그 인스턴스자체를 print()함수로 화면에 출력하면 나오는 값
#__변수명 : 비공개 필드(속성)
#__메서드명() : 비공개 메서드


class Car:
    def __init__(self,speed=0,color='white'):
        self.__color = color #외부에서 직접 접근 불가
        # self.color = color
        self.speed = speed

#    def __str__(self):

    def getColor(self): #color 필드값 반환
        return self.__color

    def setColor(self,color): #color 필드값을 변경
        self.__color = color

    def __showColor(self): #비공개 메소드
        print(f'이 자동차의 색상은 {self.__color}')

    def showInfo(self):
        self.__showColor()
        print(f'이 자동차의 색상은 {self.__color}')

    def drive(self):
        print(f'{self.speed}로 주행중')


car1 = Car()
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())
car1.color = 'blue' #필드를 외부에서 직접 바꿀수있음
car1.showInfo()