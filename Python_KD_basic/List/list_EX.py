#기본 활용
numL = [1,3,4, [1,2]]
for x in numL:
    print(x)

for i in range(len(numL)):
    print(numL[i])

#활용
scores = []
for i in range(10):
    score = int(input('점수 : '))
    scores.insert(0, score) #최신 입력순
    #scores.append(score)
print(scores)

#2차원 리스트 퀴즈
#10명의 학생의 국어, 영어, 수학 점수가 2차원 리스트 형식으로 저장된 경우
#각 학생별 세 과목의 총점과 평균 점수를 계산하여 과목점수와 함께 출력
StuL = [[80,75,95],[70,75,95],[65,80,95],[80,90,95],[100,80,95],[80,65,40],
        [20,75,50],[45,75,45],[30,75,70],[50,75,50]]
for i in StuL:
    print(f'{i}, {sum(i)}, {sum(i)/len(i) : .1f}') #round(숫자, 반올림할 자리수)
