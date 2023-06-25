# Codeup_Python 기초5-3.2차원배열_1462: 2차원 배열 순서대로 채우기 1-3

n = int(input())
arr = [[0] * n for i in range(n)]
a = 1
for j in range(n):
    for i in range(n):
        arr[i][j] = a
        a += 1
for i in arr:
    print(*i)