# Codeup_Python 기초5-3.2차원배열_1504: 지그재그 배열2

n = int(input())
array = [[0] * n for _ in range(n)]
num = 1
for j in range(n):
    if j%2==1:
        for i in range(n-1,-1,-1):
            array[i][j] = num
            num += 1
    else:
        for i in range(n):
            array[i][j] = num
            num += 1
for i in array:
    print(*i)