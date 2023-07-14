# Codeup_Python 기초5-3.2차원배열_1482: 2차원 배열 빗금 채우기 3-7

n,m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]

a = n*m
for i in range(n+m-1, -1,-1):
    start = min(i, n-1)
    end = max(0,i-(m-1))
    for j in range(start, end-1, -1):   # 대각선을 채울때, 아래있는 것 먼저 채워서 for문을 역순으로 함
        k = i - j
        matrix[n-1-j][k] = a
        a -= 1

for i in matrix:
    print(*i)

# 1478번 문제랑 대각선 그리는 방향이 같다. 단, a를 n*m에서 부터 빼주면 된다. 
n,m = map(int, input().split())
matrix = [[0]*m for _ in range(n)]

a = n*m
for i in range(n+m-1):
    start_col = max(0, i-(m-1))
    end_col = min(i, n-1)
    for j in range(start_col, end_col+1):
        k = i - j
        matrix[j][m-1-k] = a
        a -= 1

for i in matrix:
    print(*i)