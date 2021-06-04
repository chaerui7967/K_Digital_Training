class Dog():
    def __init__(self,breed='name',size='Large',age=7,color='Black'):
        self.Breed = breed
        self.Size = size
        self.Age = str(age)+' years'
        self.Color = color
    def Eat(self):
        print('음식을 먹는다')
    def Sleep(self):
        print(f'{self.Breed}가 잠들었다')
    def Sit(self):
        print(f'{self.Breed}가 앉았다')
    def Run(self):
        print(f'{self.Breed}가 놀고있다')
    def showInfo(self):
        print(f'{self.Breed}는 {self.Size}의 '
              f'{self.Age}의 {self.Color}색 강아지입니다.')
    def __str__(self):
        return f'{self.Breed}는 {self.Size}의 {self.Age}의 {self.Color}색 강아지입니다.'
    def __lt__(self, other):
        return self.Age < other.Age
    def __eq__(self, other):
        return self.Age == other.Age

dog1 = Dog('Neapolitan Mastiff','Large',5)
dog2 = Dog('Maltese','Small',2,'White')
dog3 = Dog('Chow Chow','Medium',3,'Brown')
dogL = [dog1, dog2, dog3]
dog1.showInfo()
dog2.showInfo()
dog3.showInfo()
for i in dogL:
    print(i)
print(dog1<dog2)
print(dog1==dog3)

#클래스 상속
# 슈퍼 사람 클래스: Person
# 하위 학생 클래스 : Student

class Person():
    def __init__(self,age=0,name='',sex=''):
        self.age = age
        self.name = name
        self.sex = sex
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    #학교, 학과, 학번,공부하다()
    def __init__(self,age=0,name='',sex='',school='',hac='',num=''):
        super().__init__(age,name,sex)
        self.school = school
        self.hac = hac
        self.num = num
    def study(self):
        print('study....')
    def exam(self):
        print('exam..')
    def __str__(self):
        return f'{self.school}에 다니는 {self.hac}과 {self.num} {self.name}입니다.'

per1 = Student(school='abc대학',hac='컴퓨터공학',num='1234',name='홍길동')
print(per1)

