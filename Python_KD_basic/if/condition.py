#키보드로 입력받은 정수가 짝수 인지 아닌지 확인
aa= int(input("정수 입력 : "))
bb= aa%2
cc= bb!=1
print('짝수?'+str(cc))

#조건문 if elif else
if(aa % 2 == 0):
    print('짝수')
else:
    print('홀수') #pass 아무것도 수행하지 않음

#반복문 for, while
