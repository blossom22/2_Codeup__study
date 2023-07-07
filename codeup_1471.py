# Codeup_Python 기초5-3.2차원배열_1471: 2차원 배열 지그재그 채우기 2-4

n = int(input())
arr = [[0]*n for _ in range(n)]
a = 1
for i in range(n):
    if i%2==0:
        for j in range(n-1,-1,-1):
            arr[j][i] = a
            a+=1
    else:
        for j in range(n):
            arr[j][i] = a
            a+=1
for i in arr:
    print(*i)
