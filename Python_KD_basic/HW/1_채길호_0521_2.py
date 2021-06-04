
#학생들 점수를 내림차순 정렬 출력
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

SL.sort(reverse=True)
print(f'점수 내림차순 정렬 : {SL}')

#사자성어 맞추기 게임
from random import randint
qu = ['잘못을 고치고 옳은 길에 들어섬', '죽일 고비를 여러 번 겪으며 살아나다', '평범한 사람 가운데 뛰어난 사람',
      '아무짝에나 쓸모 없는 것', '고통과 즐거움을 함께 한다', '미리 준비해두면 근심 걱정이 없다',
      '사회적으로 인정받고 출세하여 이름을 세상에 드날림', '다른 사람의 학식이나 업적이 크게 진보한 것을 말함',
      '생사를 같이 할 수 있는 친밀한 벗', '상대 없이 혼자서는 어떤 일을 이룰 수 없다']
an = ['개과천선', '구사일생', '군계일학', '무용지물', '동고동락', '유비무환',
        '입신양명', '괄목상대', '막역지우', '고장난명']
print('사자성어 맞추기 게임을 시작합니다\n-----------------------------')
while True:
    bun = randint(1, len(qu))
    print(qu[bun])
    aa = input('이말의 사자성어는? : ')
    if aa == an[bun]:
        print('\n맞습니다.. 게임을 종료합니다')
        break
    else:
        print('\n틀렸습니다...다시 도전 !\n')
#다른 방법
from random import choice

print("사자성어 맞추기 게임을 시작합니다\n--------------------")

quoteDict = {"개과천선": "잘못을 고치고 옳은 길에 들어섬",
        "구사일생": "죽을 고비를 여러번 겪으며 살아나다",
        "군계일학": "평범한 사람 가운데 뛰어난 사람",
        "무용지물": "아무짝에나 쓸모 없는 것",
        "동고동락": "고통과 즐거움을 함께 한다",
        "유비무환": "미리 준비해두면 근심 걱정이 없다",
        "입신양명": "사회적으로 인정받고 출세하여 이름을 세상에 드날림",
        "괄목상대": "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",
        "막역지우": "생사를 같이 할 수 있는 친밀한 벗",
        "고장난명": "상대 없이 혼자서는 어떤 일을 이룰 수 없다"
        }

answerDict = {j:i for i,j in quoteDict.items()}


while (True):
    meaning = choice(tuple(quoteDict.values()))
    answer = answerDict[meaning]

    print(meaning)
    userAnswer = input("이 말의 사자성어는?")
    if userAnswer == answer:
        print("맞습니다.. 게임을 종료합니다.")
        break
    else:
        print("틀렸습니다...다시 도전 !")

