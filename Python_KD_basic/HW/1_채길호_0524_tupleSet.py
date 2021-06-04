# 1. my_variable 이름의 비어있는 튜플을 만들라.
my_variable = tuple()

# 2. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#  t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
#  ==> 튜플의 요소는 변경할수 없다

# 3. 숫자 1 이 저장된 튜플을 생성하라.
t1 = (1,)

# 4. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
#   ==> 튜플

# 5. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
tt = list(t)
tt[0] = 'A'
t = tuple(t)

# 6. 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)

# 7. 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)

# 8. 파티에 참석한 사람이 다음과 같을 때 집합을 생성하고, 아래 조건에 맞게 출력하시오.
# partyA : "Park","Kim","Lee"
# partyB : "Park","길동","몽룡"
partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}
# 1) 파티에 참석한 모든 사람은?
print(partyA | partyB)
# 2) 2개의 파티에 모두 참석한 사람은?
print(partyA & partyB)
# 3) 파티 A에만 참석한 사람
print(partyA - partyB)
# 4) 파티 B에만 참석한 사람
print(partyB - partyA)


