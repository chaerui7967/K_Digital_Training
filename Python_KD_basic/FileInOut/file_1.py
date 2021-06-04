#open
#변수명 = open('파일명','r') =open('--','w') 기본은 r
#r+ 읽기/쓰기 겸용 ,a 쓰기모드 (이어쓰기 append),t 텍스트모드 텍스트파일 처리 기본값, b 이진모드
#변수.close() :파일 닫기
#file 생성
f = open('file1.txt','w') #상대 경로
f.close()
#경로 수정 #폴더 이름이 다르면 오류
f = open("c:/Python_KD/file2.txt",'w') #절대경로
f.close()
#\사용시 경로 오류: / 또는 \\
f= open("c:\\Python_KD\\file2.text",'w')
f.close()
#상대 경로표시 .. <-현재보다 상위폴더
f= open("../file2.text",'w')
f.close()

