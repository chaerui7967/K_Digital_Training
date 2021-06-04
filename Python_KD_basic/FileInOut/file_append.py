# append 모드
# f = open('test2.txt','a',encoding='utf-8')
# data = '\n\nPython programming'
# f.write(data)
# f.close()

#읽기 모드로 파일 열어서 내용 출력
f = open('test2.txt','a',encoding='utf-8')
data = 'Python programming\n'
f.write(data)

f = open('test2.txt','r',encoding='utf-8')
print(f.read())
f.close()