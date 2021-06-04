#1번 람다식
f = lambda x,y:x**y

#2번
ex = [1,2,3,4,5]
al=list(map(lambda x:x**2,ex))
print(al)

#3번
#정답 ==> 3번 #개별 파일은 모듈

#4번
#정답 ==> 3번 #패키지 생성시 __init__.py 이 무조건 있어야함

#5번
#정답 ==> 2번 # import -- as 별칭(*불가)

#6번
#import fah_converter as fah #모듈을 불러와야 함수 사용가능

#7번
#from game import * #부모 디렉토리의 모든것을 불러옴

#8번  #수정후 추가됬기 때문에 'a'
# f= open('hello_python.txt','a')
# f.write('hello, python!')

#9번
#가) w
#나) a
#다) r

#10번
# from calculator import *
# 파일 내에서 함수를 바로씀

#11번
7
3
2
1
1
1
'종료되었습니다.'

#12번 #리스트의 요소를 하나씩 인덱스 0, 앞쪽부터 pop하므로 결국에는 빈리스트만 남게된다
#정답 ==> 5번

#13번 #enumerate로 인덱스와 zip으로 만들어진 튜플이 한쌍이 된다
# 따라서 처음에는 인덱스가 2가 되면 튜플안의 요소가 2개이므로 index오류가 난다
# 이번엔 분모가 튜플[0]이므로 처음 튜플에는 문자형이 들어있으므로 value오류가 난다
#정답 ==> 4번

#14번 #다 맞는것 같은데 잘 모르겟다,,
#==4번 #문법적으로 다를때, 오탈자도 변수로 인식하기 때문에

#15 #텍스트 파일 형태 그대로 컴퓨터에서 인식하지 못하는 걸로 알고있다.
#컴퓨터가 이해할수 있는 이진 형식으로 컴퓨터가 변환하고 해석하는 걸로 알고있다.
#정답 == >4번

#16
'숫자가 아닙니다'

#17
#1- NameError
#2- IOError
#3- RuntimeError
#4- KeyError

#18
'Not divided by 0'

#19
with open('i_have_a_dream.txt','r') as f:
    contents = f.read()
    print(contents)