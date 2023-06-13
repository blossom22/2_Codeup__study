# Codeup_Python 기초4-2.중첩반복문_1371: 마름모 출력하기

n = int(input("자연수를 입력하세요: "))
for i in range(n-1,-1,-1):
    print(' '*i+'*'+' '*2*(n-1-i)+'*')
for j in range(n):
    print(' '*j+'*'+' '*2*(n-1-j)+'*')