#set 중복되지 않은 항목들이 모인것
#인덱스 사용 불가, 리스트 포함불가, 튜플가능
set1 = {1,2,3,4,1,2,1}
set1.add(5)
set2 = {(1,2,3),1}
set1.remove(5) #값을 삭제 없는 경우 에러
set1.discard(4) #값을 삭제 없는 경우 통과
set1.clear() #모든 요소 삭제
del set1 #객체 삭제
#집합 연산 함수: union(합), intersection(교), difference(차)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
#집합 연산 &(교집합), |(합집합), -(차집합)
set1 & set2
set1 | set2
set1 - set2

a=set('asdfassssssssaaaaaaa')#중복문자 삭제

#컴프리헨션
a={x for x in 'avasdfasdfsadf' if x not in 'abc'}

