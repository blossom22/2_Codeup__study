# Codeup_Python 기초5-3.2차원배열_1469: 2차원 배열 지그재그 채우기 2-2

a = int(input())
arr = [[0] * a for i in range(a)]
c = 1
for i in range(a):
    if i%2==1:
        for j in range(a):
            arr[i][j] = c
            c += 1
    else:
        for j in range(a-1,-1,-1):
            arr[i][j] = c
            c += 1
for i in arr:
    print(*i)
