f = open('test2.txt','r',encoding='utf-8')
data =f.read()
print(data)
print(type(data))
print(len(data))

for ch in data:
    print(ch)
f.close()