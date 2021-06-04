#파일 내에서 검색
#seek(offset, whence)
#offset : 상대위치
#whence : 위치 0:시작 ,1:현재 위치,2: 파윌끝
#파일안에서는 엔터키=\r\n 2바이트사용
#한글도 글자당 2바이트 사용

f = open('test2.txt','r+',encoding='utf-8')
# f.seek(0,0) # 시작위치 0행 0열
# f.seek(1,0) # 0행 1열
# f.seek(7,0) # 1행 0열
# f.seek(14,0) #
# f.seek(15,0) #오류발생 한글은 utf8 = 3바이트
# utf16은 2바이트씩 계산되기 때문에
lines = f.readlines()
f.seek(-0,2)
print(lines)
f.close()