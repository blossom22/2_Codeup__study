# Codeup_Python 기초5-3.2차원배열_1483: 2차원 배열 빗금 채우기 3-8
# 1479번 문제랑 대각선 그리는 방향이 같다. 단, a를 n*m에서 빼주면 된다
n,m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]

a = n*m
for i in range(n+m-1):
    start = min(i, n-1)
    end = max(0,i-(m-1))
    for j in range(start, end-1, -1):
        k = i - j
        matrix[j][m-1-k] = a
        a -= 1

for i in matrix:
    print(*i)