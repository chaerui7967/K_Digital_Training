#try ~ ~~ except ~~(else~~ finally~~) ()생략가능
# try:
#     예외 발생 가능 문장
# except 예외 유형:
#     처리

try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
    print('어휴 ㅡㅡ ')
finally: #항상 나옴
    print('WW')

try:
    print('age'+2)
except TypeError as e:
    print(e)
finally: #항상 나옴
    print('WW')

#여러개의 예외처리 :제일 처음 오류난것만 처리함
try:
    print('age'+210)
    print(10/0)
except (ZeroDivisionError,TypeError) as e:
    print(e)
finally: #항상 나옴
    print('WW')


try:
    num = int(input('숫자 : '))
except ValueError:
    print('정수 ㄴ')
else:
    print(num)
finally:
    print('종료')