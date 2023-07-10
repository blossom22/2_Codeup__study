# Codeup_Python 기초5-3.2차원배열_1477: 2차원 배열 빗금 채우기 3-2

# 대각선내에서 행 인덱스와 열 인덱스의 합이 일정하다.

n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
a = 1
for i in range(n+m-1):
    for k in range(0, n):
        for j in range(0, m):
            if j+k == i:        # 행 인덱스와 열 인덱스의 합이 대각선 인덱스(i)와 일치해야한다
                matrix[k][j] = a
                a += 1
for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end=' ')
    print()

# 이런 풀이도 가능하다.
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
a = 1
for i in range(n + m - 1):              # i는 대각선 인덱스 (대각선의 개수는 (n+m-1)개 즉, 인덱스는 0~(n+m-2)까지 나옴)
    start_row = max(0, i - m + 1)       # strat_row는 현재 대각선에서 값이 할당되어야 하는 행의 시작점 인덱스
    # i < m-1(열의 최대인덱스) 이면, 대각선이 행의 범위 벗어나지 않아서 start_row = 0 
    # i >= m-1이면, 대각선이 행의 범위 벗어날 수 있다. 이때는 대각선 시작 인덱스는 i-(m-1)
    end_row = min(i, n - 1)
    # i < n-1(행의 최대인덱스)이면, 대각선이 행의 범위 벗어나지 않아서 end_row = i
    # i >= n-1 이면, 대각선이 행의 범위 벗어날 수 있다. end_row = n-1

    # start_row랑 end_row는 현재 대각선에 해당하는 행의 시작과 끝
    for j in range(start_row, end_row + 1):
        k = i - j       # k는 현재 대각선에 해당하는 열의 인덱스 / 대각선내에서 행인덱스와 열인덱스의 합이 일정한 것을 이용함
        matrix[j][k] = a
        a += 1
for row in matrix:
    print(*row)

