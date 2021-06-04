#퀴즈 1 5/18 키보드로부터 두개의 숫자를 입력받고 두수의 합과 평균을 구하시오.

a, b = map(int, input('두 정수를 입력(","로 구분) : ').split(','))
hap = a+b
avg = hap/2
print('두 정수의 합: %d , 두 정수의 평균: %.2f' % (hap, avg))

#format이용
print('두수의 합 {0}, 평균 {1}'.format(hap, avg))
print('두수의 합 {0:d}, 평균 {1:5.2f}'.format(hap, avg))
print(format(hap, '10.2f'))

# 현금이 5000원이 있고, 사탕 가격이 120원인경우 최대한 살수 있는 사탕 개수와 나머지 돈?
mo, sa = 5000, 120
num, r = mo // 120, mo % 120
print('사탕 개수: {0} , 나머지 돈 : {1}'.format(num, r))
