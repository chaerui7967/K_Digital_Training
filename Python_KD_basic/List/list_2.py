#리스트 주요 메소드
#len 길이 계산
a = [1, 2, 3, 4, 5, 6]
print(len(a))
#리스트 요소 분류 count
a.count(3)
#리스트 요소 추가, 삽입 : append, insert
a.append(100)
a.append([1, 2, 3])
a.insert(2, 123)

#리스트 제거 : remove, pop
n=[1,2,3,4,1,1,1,7,8,9,10]
n.remove(1)
#활용
cnt = n.count(1)
n.remove(cnt)
#pop 지정하지 않으면 맨 마지막 데이터를 뽑아옴(제거), 인덱스를 지정해서 뽑아올 수 있음
da = n.pop() #가장 마지막 데이터를 뽑아옴 기존 리스트에선 제거

#리스트 확장 : extend <-append + insert
a=[3, 6, 9, 12, 15]
b=[2, 4, 6, 8, 10]
a.append(b) # 리스트 그 자체가 추가됨
a.insert(2, b)
a.extend(b) # 리스트의 요소들로 추가됨

#리스트 정렬 : sort, reverse<-현재 리스트의 순서를 바꿈
a.sort(reverse=True)
a.reverse()
#reverse()를 사용하지 않고 리스트 순서 바꾸기
b=list()
for i in range(len(a)-1,0,-1):
    b.append(a.pop())
print(b)
#sorted() 함수
c = sorted(a) #a는 변화하지 않음 c에 결과 저장
string = ['A','B','a','c','d']
string.sort(key=str.upper) #str.lower(소문자 기준) 대문자가 기본

#리스트 요소 찾기 : index(값) 값의 위치
a.index(3)
#리스트 요소 검색 : max, min
max(a)

#in /not in
if 2 not in a:
    print('dd')
else:
    print('xx')