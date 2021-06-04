#파일 내에서 read함수를 이용하여 원하는 내용 검색
aa= input('검색 값 입력 : ')
f = open('test2.txt','r',encoding='utf-8')
data = f.read()
if aa in data:
    print(aa)
else:
    print('검색실패')
f.close()