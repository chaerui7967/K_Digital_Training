# ## 클래스 내에서 변수 변경
# class Car:
#     def __init__(self,speed=0,color='white'):
#         self.color = color
#         self.speed = speed
#     def drive(self):
#         print(f'{self.speed}로 주행중')
#     def showInfo(self):
#         print(f'이 자동차의 색상은 {self.color}')
#     def upSpeed(self, up):
#         self.speed +=up
#     def downSpeed(self, down):
#         self.speed -= down
#         if self.speed<0:
#             self.speed=0
#
# car1=Car()
# car1.upSpeed(20)
# car1.drive()
# car1.downSpeed(5)
# car1.drive()

#__str__ : 클래스로 인스턴스를 생성했을 때, 그 인스턴스 자체를 print()함수로 화면에 출력하면 나오는 값
#__repr__ : 인스턴스를 print문으로 출력할때 실행
#__del__ : 소멸자, 인스턴스 삭제
#__add__ : 인스턴스 사이의 덧셈
#__lt__ : 두 인스턴스 사이의 대소 a(내꺼)<b
#__le__
#__gt__
#__ge__
#__eq__ : 두 인스턴스가 같은지
#__ne__

class Line:
    def __init__(self,length=0):
        self.length = length
        print(f'{self.length} 길이의 선이 생성')

    # def __del__(self):
    #     print(f'{self.length} 길이의 선이 소멸')

    def __repr__(self): #__str__도 동일
        return '선의 길이 : '+str(self.length)

    def __add__(self, other):
        return self.length + other.length

    def __eq__(self, other):
        return self.length == other.length
    def __ne__(self, other):
        return self.length != other.length #다름 연산자사용가능
    def __lt__(self, other):
        return self.length < other.length #내가 작음

line1 = Line()
line2 = Line(10)
print(line1)
# print(line1.__add__(line2))
print(line1+line2)
if line1 == line2:
    print('같음')
else:
    print('다름')

