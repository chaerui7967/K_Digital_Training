#with
#with open(파일명, 열기모드) as 파일객체:
#with 문이 종료되면 파일객체는 자동으로 close

# with open('test3.txt','w') as f:
#     f.write('hello\nhi')

filename = 'test3.txt'
data = '''나는 파이썬을 배우고 있습니다.
쉽지는 않지만
하나씩 내가 해내니 성취감이 느껴져 좋네요'''

with open(filename,'w',encoding='utf-8') as f:
    f.write(data)