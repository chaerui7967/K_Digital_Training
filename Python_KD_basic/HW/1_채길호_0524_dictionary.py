#학생들의 성적에 대한 총점과 평균을 계산하여 출력
students = [
   {"name" : "홍길동", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
   {"name" : "이몽룡", "korean" : 92, "math" : 98, "english" : 96, "science" : 98},
   {"name" : "성춘향", "korean" : 76, "math" : 96, "english" : 94, "science" : 90},
   {"name" : "변학도", "korean" : 98, "math" : 92, "english" : 96, "science" : 92},
   {"name" : "박지성", "korean" : 95, "math" : 98, "english" : 98, "science" : 98},
   {"name" : "류현진", "korean" : 64, "math" : 88, "english" : 92, "science" : 92}
]
print('이름\t총점\t평균')
for i in students:
    hap = sum(list(i.values())[1:5])
    print(f'{i["name"]}\t{hap}\t{hap/(len(i)-1):.2f}')

#사용자로부터 영어단어와 뜻을 입력받아 사전을 구성하고 사용자가 입력한 단어를 검색하여 뜻을 출럭하는 프로그램
dic1 = dict()
while True:
    a = input('영어 단어 등록 (종료는 quit) : ')
    if a == 'quit':
        break
    elif dic1.get(a):
        print(f'{a}는 이미 등록된 단어 입니다.')
        print()
        continue

    b = input(f'{a}의 뜻입력 (종료는 quit) : ')
    if b == 'quit':
        print()
        break
    dic1[a] = b
    print()
    
print()
    
while True:
    c = input('검색할 단어 입력 (종료는 quit) : ')
    if dic1.get(c):
        print(f'{c}의 뜻은 {dic1.get(c)}입니다')
        print()
    elif c=='quit':
        print()
        print('종료합니다')
        break
    else:
        print(f'{c}는 사전에 없는 단어 입니다.')
        print()

