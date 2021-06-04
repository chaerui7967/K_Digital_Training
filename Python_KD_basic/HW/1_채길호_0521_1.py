
#회원이름을 입력받아 회원명단 리스트 생성 및 회원명단 리스트 내용 출력
names =[]
while True:
    name = input('회원 입력 : ')
    if name:
        names.append(name)
    else:
        break
print(f"회원 명단 : {' '.join(names)}")

#학생 수 입력 후 학생 수 만큼 점수를 입력받은 후 총점과 평균을 계산 , 80점 이상인 학생 수를 출력
co = int(input('학생 수 입력 : '))
SL =[]
Gd = 0
for i in range(co):
    score = int(input(f'학생{i+1} 점수 입력 : '))
    SL.append(score)
    if score >= 80:
        Gd +=1
hap = sum(SL)
avg = hap / co
print(f'총점 : {hap}\n평균 : {avg:.2f}\n80점 이상 학생 : {Gd}명')

#다른 방법
NS = int(input('학생 수 입력 : '))
Scorelist = list()

for i in range(NS):
    Scorelist.append(int(input(f"학생{i+1} 점수 입력 : ")))
Total = sum(Scorelist)
print(f'총점 : {Total}\n평균 : {Total / len(Scorelist)}\n80점 이상 학생 : '
      f'{len(list(filter(lambda x: x>= 80,Scorelist)))}명')

#상품 리스트에 추가하고 엔터키를 누름 입력이 종료, 등록된 상품 리스트를 출력
sa = []
while True:
    a = input('상품 등록 (엔터키 누르면 종료) : ')
    if a:
        sa.append(a)
    else:
        break
print(f"등록된 상품 : {' '.join(sa)}")