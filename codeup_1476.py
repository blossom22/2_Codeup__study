# Codeup_Python 기초5-3.2차원배열_1476: 2차원 배열 빗금 채우기 3-1

# 대각선내에서 행 인덱스와 열 인덱스의 합이 일정하다.

n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
a = 1
for i in range(0, n+m-1):
    for j in range(0, m):
        for k in range(0, n):
            if j+k == i:        # 행 인덱스와 열 인덱스의 합이 대각선 인덱스(i)와 일치해야한다
                matrix[k][j] = a
                a += 1
for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end=' ')
    print()