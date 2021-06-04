#파일을 쓰기모드로 열고, 파일객체를 생성 write 함수를 사용 내용을 덮어씀 기존내용 사라짐
data='hello'
f = open('file123.txt','w') #파일객체 생성
f.write(data)
f.close()
#utf-8 형식으로 저장 : 한글이 깨지지않음
data='안녕'
f = open('file123.txt','w', encoding='utf-8')
f.write(data)
f.close()