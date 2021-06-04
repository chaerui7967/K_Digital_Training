#함수 내에 사용되는 변수 : 지역변수
#전체 코드에서 영향을 주는 변수 : 전역변수
def show():
    a = 'hello' #지역변수

a='wjsdur' #전역변수

#연습
def show2():
    print(a)

#함수 내에서 전역변수 사용
def show3():
    global a
    a = a +'H' #함수 내부에서 전역변수 변경
    print(a)
a='ggg'
show3()

