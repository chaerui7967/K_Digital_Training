#텍스트파일을 읽어와서 계산 후 계산 결과 파일로 출력
def sum(input,result):
    with open(result, 'w', encoding='utf-8') as result:
        with open(input, 'r', encoding='utf-8') as f:
            data = f.read().split().copy()
            for i in range(len(data)):
                if i%2 == 0:
                    if int(data[i+1])<0:
                        sic = data[i] + data[i+1]
                        sum_result = str(int(data[i])+int(data[i+1]))
                        result.write(sic + '=' + sum_result + '\n')
                    else:
                        sic = data[i] + '+' + data[i + 1]
                        sum_result = str(int(data[i]) + int(data[i + 1]))
                        result.write(sic + '=' + sum_result + '\n')

if __name__ == '__main__':
    sum('sum_test.txt','sum_result.txt')

# ##다른방법
# def sumFile(inputFileName, outputFileName):
#     with open(inputFileName, 'r', encoding='utf-8') as inputFile:
#         textFile = inputFile.readlines()
#         with open(outputFileName, 'a', encoding='utf-8') as outputFile:
#             for line in textFile:
#                 numberList = [int(i) for i in line.split(' ')]
#                 x, y = numberList[0], numberList[1]
#                 outputFile.write(f"{x}+{y}={x + y}\n")
#
#
# def main():
#     sumFile('numbers.txt', 'calculated.txt')
#
# main()