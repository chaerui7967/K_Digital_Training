#타입변환

a=1234

print('나의 나이는 '+str(a)+'이다!')

num=input('숫자? ')

print(int(num)+100)
print(float(num)+100)

print(int('123',8)) #8진수 123 print시 10진수로 변환되서 출력
print(int('123',16))
print(int('111',2))