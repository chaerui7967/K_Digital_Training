#len
string = "python prograMming"
len(string)
#count 문자열에서 찾고자하는 문자의 개수
string.count('python')
#find 잇으면 위치, 없으면 -1 , rfind(오른쪽부터 탐색)
string.find('program')
#index 있으면 위치, 없으면 오류 tuple, dict, string 사용, rindex
string.index('p')
#split 지정된 문자로 문자열을 리스트값으로 분할함
token = string.split()
token2 = string.split('a')
#join
a='aa'
print(a.join('bbb')) #a가 bbb사이에 들어감
#list join => 문자열로 반환
numpers = ['10', '20', '30', '40', '50']
sep = ','
result = sep.join(numpers)
print(result)
#replace
string.replace('python', 'C++')
#upper/lower/capitalize() <- 맨 앞문자만 대문자/ title <- 시작하는 단어 대문자
string.upper()
string.lower()
string.title()
string.capitalize()
#swapcase 대소문자 변환
string.swapcase()
#공백문자 제거 strip(), lstrip, rstrip
string='          Apython          '
string.strip()+'11'
string.lstrip()+'11'
string.rstrip()+'11'

#https://docs.python.org/ko/3/ 이용
