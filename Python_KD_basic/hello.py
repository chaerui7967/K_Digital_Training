# 1번째 프로그램
'''
print('chae gil ho')

x,y,z= 10,20,30

x=10 ; y=20 ; z=30 ;
print(x,y,z)

x=y=z=100

print(x,y,z)

#swap

a,b=10,20

a,b=b,a

#변수 삭제 del 변수


#문자열 str() 형변환 함수
name = 'asdf'
age = 12

print(name,age)

address = 'qwer'

print(name+'='+address)

print(name+str(age)+address)
print(name+'=',age,'dd')

#연습문제

name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5

print('성명 : ' + name)
print('학번 :', no)
print('학년 :', year)
print('학점 : ' + grade)
print('평균 :', average)

#포맷 코드

name = '홍길동'
no = 2016001
year = 4
grade = 'A'
average = 93.5

print("성명 : %s" % name)
print("학번 : %d" % no)
print('학년 : %d' % year)
print('성적 : %s' % grade)
print('평균 : %10.2f' % average)

print('이름 %s, 학년 %d' %(name, year))

rate = 80
print('출석률 %d%%' %rate)

#예제 화씨 온도> 섭씨
fTemp = 90
cTemp = (fTemp -32) * 5/9
print(cTemp)

# %f는 기본 소숫점 6자리 10.2f <- 소숫점 포함 총 10자리

aa= format(cTemp, '10.2f')
print(aa)

#예제 포맷

kor,eng,math = 90,80,80
hap = kor+eng+math
avg = hap/3

print('총점: %d, 평균: %.2f' %(hap,avg))

#이자율 계산

INT_Rate = 0.03

deposit = 10000
interest = deposit * INT_Rate
balance = deposit + interest

print(balance,int(balance),sep='\n')

print(format(int(balance),','))

# 0b 2진수, 0o 8진수, 0x 16진수

a= 0b1010
b= 300
c= 0o123
d = 0x12fc
print(a,b,c,d)

#e5 <- 10^5

#행분리 \
a=1+2+\
   3
aa=(1+2+
    3)

#\n을 표현하기위해선 print(r"c:\info\name")가능 <-r

#sep =, end=(마지막 문자)
'''
'''
#연습문제2
1. 5
2. B++
3. 4
4. 4
5. 3
6.
    1)하하하
    2)300
    3)200 + 100
    4)300
7. 1,4
8. 3,4
9.
    1)10 / 4 = 2
    2)10 / 4 = 2.5
    3)10 / 4 =   2.5
    4)10 / 4 =     2
10.
    1)00543
    2)       파이썬
    3)123.5
'''

