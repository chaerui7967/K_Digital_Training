#eval() -> 입력된 문자열에 해당하는 숫자형으로 변환

num1 = eval(input('num1: '))
num2 = eval(input('num2: '))
total = num1 + num2
print('합은 {}'.format(total))
print(eval(input())) # 3+2(계산식 가능)
