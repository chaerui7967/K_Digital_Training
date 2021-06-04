#dictionary
#키와 값으로 구성 {키:값}
d = {1:'a', 2:'b'}

#요소 접근시 키값을 사용
d[1]

#딕셔너리 요소 추가
d[4] = "f"

# keys(), values(), items()
d.items() #키와 값은 튜플로 묶여있고 묶음이 리스트형식
d.keys()
d.values()

d1=d.keys() #d1의 타입은 dict_keys
list(d1)[1] #key값의 요소 하나를 불러오기

#get(key값,없을경우 메세지) 없는 경우 none을 출력or 설정한 메세지 출력
# d[]의 경우 오류메세지
d.get(3,'not exist') #key값에 맞는 value값을 가져옴

#활용
k='link'

if d.get(k) is None:
    print(k+'에 대한 데이터 없음')

#in/ not in
if 1 in d:
    print('dd')

2 not in d

d.popitem() #마지막 아이템을 뽑아냄
#.pop(key값)
#for문 축약, 컴프리헨션
[x**2 for x in (1,2,3)]
a= {x: x**2 for x in (2,3,4)}

#zip
a = ['1','2']
b = ['asdf','qwer']
for i,j in zip(a,b):
    print(i,j)

for k,v in d.items():
    print(k+'1',v)
