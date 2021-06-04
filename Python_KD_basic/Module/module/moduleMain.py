#main Ex

print(__name__) #파일 내에서 호출시 main 출력 ,, 파일 외에서 해당 모듈을 호출하여 보일때는 모듈명이 호출됨
name = ''
def inputName():
    global name
    name = input('이름 입력 : ')

def getName():
    if name=='':
        return print('무명')
    else:
        return print(name)

def main():
    inputName()
    getName()

#__name__ : import 하는 파일명을 저장
if __name__ == '__main__':
    main()