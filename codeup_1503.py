# Codeup_Python 기초5-3.2차원배열_1503: 지그재그 입력(2차원 배열)

n = int(input())
array = [[0] * n for i in range(n)] 
num = 1
for i in range(n):
    if i%2==0:
        for j in range(n):
            array[i][j] = num
            num += 1
    else:
        for j in range(n-1,-1,-1):
            array[i][j] = num
            num += 1
for i in array:
    print(*i)