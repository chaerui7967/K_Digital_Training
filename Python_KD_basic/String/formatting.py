# formatting : %d %f %s %c
aa, dd = 10, 20
aasdf = 'ppp'
print('문자 : %d' %aa)
print('문자 : ', format(aa,'d'),'개')
print('문자 : {0}, 숫자: [1}'.format(aa,dd))
print('문자 : {aa}개, 숫자 : {dd}개'.format(aa=aa, dd=dd))
print('키 : {0:5.1f}'.format(aa))
#정렬
print('{0:<10}'.format(aasdf))
print('{0:>10}'.format(aasdf))
print('{0:^10}'.format(aasdf))
print('{0:-^10}'.format(aasdf))
print(aasdf.ljust(10))
print(aasdf.rjust(10))
print(aasdf.center(10))

#날짜, 시간 출력
from datetime import date, datetime, timedelta

today = date.today()
print(today.year)
print(today.month)
print(today.day)

cur_time = datetime.now().time()
print(cur_time.hour)
print(cur_time.minute)
print(cur_time.second)
print(cur_time.microsecond)

cur_time = datetime.now()
print(today + timedelta(days=-1)) #하루전
print(cur_time + timedelta(days=1, hours=2)) #내일 2시간 뒤

print(today.strftime('%Y-%m-%d %H:%M:%S'))