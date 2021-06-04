#리스트 내용 일치
list1 = [1,2,3]
list2 = [1,2,3]

# == , !=, <, >
print(list1 == list2)

# 2차원 리스트
list3 = [[1,2,3],[4,5,6],[7,8,9]]
#행렬 형식으로 출력
for i in list3:
    print(i)

for i in list3:
    for j in i:
        print(j, end="")
    print()