#readline : 1개의 행씩 읽어오는것 행끝에 \n이 포함
#readlines : 모든 행을 읽어 라인 단위별로 짤라서 리스트를 생성
#{...\n,...\n}
#read : 내용 전체를 한 문자열로 반환 "  "

# print('------첫번째 행 가져오기 -----')
#ansi형식
f = open('test.txt','r',encoding='utf-8')
line = f.readline()
print(line)
f.close()

#utf-8 저장 파일 : 오류발생
# f = open('test.txt','r')
# line = f.readline()
# print(line)
# f.close()
# 수정 encoding 지정
# f = open('test.txt','r',encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

# 여러줄 읽기
# f = open('test.txt','r', encoding='utf-8')
# line = f.readline() #기본적으로 \n이 붙어서 옴
# print(line, end="")
# line = f.readline()
# print(line, end="")
# f.close()

# 파일전체 읽기
# f = open('test.txt','r', encoding='utf-8')
# while 1:
#     try:
#         line = f.readline()
#         print(line, end="")
#     except Exception:
#         break #마지막은 빈문자열
# f.close()

## 다른 방법 while과 if만 사용
# f = open('test.txt', 'r', encoding = 'utf-8')
# line = f.readline()
# print(line, end = '')
# while True:
#     line = f.readline()
#     if(line == ''):
#         break
#     print(line, end = '')
# f.close()

#readlines 결과 만들기
# f = open('test.txt', 'r', encoding = 'utf-8')
# line = f.readline()
# newL = []
# print(line, end = '')
# while True:
#     line = f.readline()
#     if(line == ''):
#         print()
#         break
#     newL.append(line)
#     print(line, end = '')
# print(newL)
# f.close()
