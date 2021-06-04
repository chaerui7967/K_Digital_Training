#클래스메소드 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
#self 대신 cls를 사용
#@classmethod ##--> 매개변수에 cls를 지정
#클래스 변수를 이용하는 메소드를 정의할 때

class Person:#(object)생략가능
    count = 0 #클래스 변수

    def __init__(self):
        Person.count+=1

    @classmethod
    def showCount(cls):
        print(f'{cls.count}명 태어남')

    def greeting(self): #<-인스턴스 메소드
        print('인사')

for i in range(10):
    Person()
Person.showCount()

kim = Person()
Person.showCount()
lee = Person()
Person.showCount()