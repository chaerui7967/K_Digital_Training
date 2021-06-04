#gbb game
from random import randint

def gbb_game(you_n):
    com_n = randint(1,3)
    if com_n-you_n ==1 or com_n-you_n ==-2:
        result = 1 #1인경우 com win
    elif com_n-you_n == 0:
        result = 2 #2인경우 비김
    elif you_n>3 or you_n<0:
        print('다시입력')
        return
    else:
        result = 3 #3인경우 my win
    return result,com_n

def input_num():
    while True:
        my_n = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
        if my_n>3 or my_n<0:
            print('다시입력')
            continue
        else:
            break
    result,com_n = gbb_game(my_n)
    if result ==1:
        print(f'컴퓨터가 이겼습니다.\nCOM : {com_n}')
    elif result == 2:
        print(f'비겼습니다.\nCOM : {com_n}')
    else:
        print(f'당신이 이겼습니다.\nCOM : {com_n}')