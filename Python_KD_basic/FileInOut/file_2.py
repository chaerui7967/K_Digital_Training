#파일에 쓰기
#여러줄 단위로 데이터쓰기
f = open('file3.txt','w',encoding='utf-8')

for i in range(1,11):
    data = "%d행\n" %i
    f.write(data)

f.close()

#,로 구분해서 csv파일 생성가능
f = open('file4.csv','w',encoding='utf-8') #엑셀로 열때는 ansi로 인코딩하는게 좋음
for i in range(1,11):
    data = "%d행," %i
    f.write(data)
f.close()

#마지막 부분 ,빼기
f = open('file4.csv','w',encoding='utf-8')

for i in range(1,11):
    if i ==10:
        data = "%d행" %i
    else:
        data = "%d행," % i
    f.write(data)

f.close()