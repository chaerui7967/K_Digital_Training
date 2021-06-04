#1 실행결과 예측
mylist = ['apple', 'banana', 'grape']
result = list(enumerate(mylist))
# print(result)
print("1번--------- 내 예측---------\n3번 = [(0,'apple'), (1,'banana'),(2,'grape')]")
print('----------결과----------')
print(result)
print()

#2
cat_song = 'my cat has blue eyes, my cat is cute'
# print({i:j for j,i in enumerate(cat_song.split())})
print("2번--------- 내 예측---------\n4번 = {'my':5, 'cat':6, 'has':2,"
      " 'blue':3, 'eyes,':4, 'is':7, 'cute':8}")
print('----------결과----------')
print({i:j for j,i in enumerate(cat_song.split())})
print()

#3
colors = ['orange', 'pink', 'brown', 'white']
result = '&'.join(colors)
print("3번--------- 내 예측---------\norange&pink&brown&white")
print('----------결과----------')
print(result)
print()

#4
user_dict = {}
user_list = ['students', 'superuser', 'professor', 'employee']
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
# print(user_dict)
print("4번--------- 내 예측---------\n{'students':0, 'superuser':1,"
      " 'professor':2, 'employee':3}")
print('----------결과----------')
print(user_dict)
print()

#5
result = [i for i in range(10) if i%2==0]
# print(result)
print("5-1번--------- 내 예측---------\n"
      "[0,2,4,6,8]")
print('----------결과----------')
print(result)
print()
items = 'zero one two three'.split('two')
result = [i for i in range(10)]
# print(result)
print("5-2번--------- 내 예측---------\n"
      "[0,1,2,3,4,5,6,7,8,9]")
print('----------결과----------')
print(result)
print()
items = 'zero one two three'.split()
# print(items)
print("5-3번--------- 내 예측---------\n"
      "['zero', 'one', 'two', 'three']")
print('----------결과----------')
print(items)
print()
example = 'cs50.gachon.edu'
subdomain, domain, tID = example.split('.')
# print(subdomain)
print("5-4번--------- 내 예측---------\n"
      "cs50")
print('----------결과----------')
print(subdomain)
print()

#6
animal = ['Fox','Dog','Cat','Monkey','Horse','Panda','Owl']
# print([ani for ani in animal if 'o' not in ani])
print("6번--------- 내 예측---------\n"
      "['Cat','Panda','Owl]")
print('----------결과----------')
print([ani for ani in animal if 'o' not in ani])
print()

#7
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
join_student = ''.join(student)
# print(join_student[-4:] + split_name[1])
print("7번--------- 내 예측---------\n"
      "DongUniversity")
print('----------결과----------')
print(join_student[-4:] + split_name[1])
print()

#8
kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score,math_score,eng_score]
# print(midterm_score[0][2])
print("8번--------- 내 예측---------\n"
      "20")
print('----------결과----------')
print(midterm_score[0][2])
print()

#9
a=[1,2,3]
b=[4,5,]
c=[7,8,9]
# print(list([sum(k), len(k)] for k in zip(a,b,c)))
print("9번--------- 내 예측---------\n"
      "[(12,3),(15,3)]")
print('----------결과----------"zip타입으로 출력되어 list함수를 추가했음"')
print(list([sum(k), len(k)] for k in zip(a,b,c)))
print()

#10
week = ['mon','tue','wed','thu','fri','sat','sun']
rainbow = ['red','orange','yellow','green','blue','navy','purple']
list_data = [week,rainbow]
# print(list_data[1][2])
print("10번--------- 내 예측---------\n"
      "yellow")
print('----------결과----------')
print(list_data[1][2])
print()

#11
kor_score=[30,79,20,100,80]
math_score=[43,59,0,30,90]
eng_score=[49,72,48,67,15]
midterm_score=[kor_score,math_score,eng_score]
# print("score:",midterm_score[2][1])
print("11번--------- 내 예측---------\n"
      "score: 72")
print('----------결과----------')
print("score:",midterm_score[2][1])
print()

#12
alist=["a","b","c"]
blist=["1","2","3"]
abcd=[]

for a,b in enumerate(zip(alist, blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")
# print(abcd)
print("12번--------- 내 예측---------\n"
      "['a','2','error']")
print('----------결과----------')
print(abcd)
print()

#13
alist=['a1','a2','a3']
blist=['b1','b2','b3']
for a,b in zip(alist,blist):
    print(a,b)
print()
## 정답 zip

#14
alphabet = ["a","b","c","d","e","f","g","h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
# print(len(answer))
print("14번--------- 내 예측---------\n"
      "80")
print('----------결과----------')
print(len(answer))