#이메일 주소를 입력받아서, 이메일 형식이 아니면 "이메일 형식이 아닙니다"출력
em = input('이메일 입력 : ')

if (em.find('@') == -1 or
        em.find('.') == -1 or
        em.index('@') > em.index('.') or
        em.index('.') - em.index('@') < 2 or
        em.index('@') == 0 or len(em) - em.index('.') <= 1 or
        em.count('@') >=2 or em.count('.') >=2):
    print('이메일 형식이 아닙니다.')
print('입력한 이메일 : %s' % em)

#생일
aa = input('생일 입력(연/월/일) : ')
aaL = aa.split('/')
print(f'당신은 {aaL[0]}년에 태어나셨군요 \n생일은 {aaL[1]}월 {aaL[2]}일 이네요.')

#주어진 데이터에서 점수만 추출하여 숫자화하고 총점과 평균을 구하라
data = '{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}'
aa = data.split(',')
score = avg = 0
for i in aa:
    score += int(i[4:6])
avg = score / len(aa)
print(f'총점 : {score}\n평균 : {avg}')

#다른방법
data = "{a1:30},{a2:50},{a3:20},{a4:70},{a5:40}"
data = [int(str(i)[1:-1].split(':')[1]) for i in data.split(',')]
total = sum(data)
print(f'총점: {total} / 평균: {total/len(data)}')

#문장을 입력하면 알파벳과 숫자, 공백, 그외 문자의 개수를 계산 출력
alpha = num = sp = r = 0
text = input('문장 입력 : ')
for i in text:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():
        sp += 1
    else:
        r += 1
print(f'문자의 개수 : {alpha}, 숫자의 개수 : {num}, 공백의 개수 : {sp}, 그외문자 개수 : {r}')

#다른 방법 아스키코드 이용
userInput = input("문장 입력")
asciiList = [ord(i) for i in list(userInput)]
counterDict = {'char': 0, 'digit': 0, 'space': 0, 'others': 0}

for charCode in asciiList:
    if 89 <= charCode <= 122:
        counterDict['char'] += 1
    elif 48 <= charCode <= 57:
        counterDict['digit'] += 1
    elif charCode == 32:
        counterDict['space'] += 1
    else:
        counterDict['others'] += 1

print(counterDict)
