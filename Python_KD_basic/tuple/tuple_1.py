#집합적 자료형 :tuple
#삭제, 변경, 추가 작업 불가
#리스트 생성 : list(), []
#튜플 생성 : tuple() ,()
t1 = (1,2,3)
t2 = tuple() #tuple 생성가능 , list ->  tuple 변환 가능
t3 = t1,(5,6,7) # ((1,2,3),(5,6,7))
t4 = [1,2],[12,3] # 튜플 안의 리스트로 생성됨

#튜플 요소 다루기 요소변경,추가,삭제 불가
t1[2]
#튜플 제거 del
del(t1)
#tuple.index(), .count()
t1.count(3)
t1.index(1)
#slicing
t1[:]
#+, * 연산
t1+t3
t1*3