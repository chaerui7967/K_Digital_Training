#readlines 모든 행을 리스트형식으로 출력
#\n포함
f = open('test.txt', 'r', encoding = 'utf-8')
lines = f.readlines()
print(lines)
# #readlines 를 한줄씩 출력
# for i in lines:
#     print(i, end="")
# f.close()

#다른방법
# with open('test.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()
#     print(''.join(lines))


