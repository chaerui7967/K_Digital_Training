#회원명단을 입력받아 저장,출력,종료 프로그램 작성
def input_member(input_file):
    while True:
        inName = input('멤버를 입력하세요.(종료는 q) : ')
        if inName.lower() == 'q':
            break
        else:
            with open(input_file, 'a', encoding='utf-8') as i:  i.write(inName+'\n')
    print('저장되었습니다.')

def output_member(output_file):
    with open(output_file, 'r', encoding='utf-8') as out:
        print(out.read())

def main():
    while True:
        aa= input('저장 1, 출력 2, 종료 q : ')
        if aa == '1':
            inputfile = input('멤버 명단을 저장할 파일명을 입력하세요. : ')
            input_member(inputfile)
        elif aa == '2':
            outputfile = input('멤버 명단이 저장된 파일명을 입력하세요. :')
            output_member(outputfile)
        elif aa.lower() == 'q':
            break
        else:
            continue

if __name__ == '__main__':
    main()
#
# ##다른방법
# def input_member(inputFileName):
#     userList = list()
#     while True:
#         userInput = input("멤버를 입력하세요. (종료는 q): ")
#         if userInput.lower() != 'q':
#             with open(inputFileName, 'a', encoding='utf-8') as f:
#                 f.write(f"{userInput}\n")
#         else:
#             break
#
#
# def output_member(outputFileName):
#     with open(outputFileName, 'r', encoding='utf-8') as f: memberList = f.readlines()
#     for line in memberList: print(line)
#
#
# while True:
#     userInput = input("저장 1, 출력 2, 종료 q: ")
#     if userInput == "1":
#         fileName = input("멤버 명단을 저장할 파일명을 입력하세요.: ")
#         input_member(fileName)
#     elif userInput == "2":
#         fileName = input("멤버 명단이 저장된 파일명을 입력하세요.: ")
#         output_member(fileName)
#     elif userInput.lower() == "q":
#         break
#     else:
#         continue