# 정적메소드 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
# 매개변수에 self를 지정하지 않음
# @staticmethod

class Cals:
    @staticmethod
    def add(a,b):   return a+b

    @staticmethod
    def sub(a,b):   return a-b

print(Cals.add(1,2))