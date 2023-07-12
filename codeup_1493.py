# Comatrixeup_Python 기초5-3.2차원배열_1493: 2차원 누적 합 배열 만들기 5-2

# 2차원 배열을 입력하는 코드
n, m = map(int, input().split())
matrix = []
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)

# 누적 합 배열 생성
cumulative_sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cumulative_sum[i][j] = cumulative_sum[i - 1][j] + cumulative_sum[i][j - 1] - cumulative_sum[i - 1][j - 1] + matrix[i - 1][j - 1]
        # (0, 0)~(i - 1, j)까지 합 + (0, 0)~(i, j - 1)까지 합 - (0, 0)~(i-1,j-1)까지 합(중복되니까 한번빼줌) + 현재위치인 matrix에서 (i-1, j-1) 에 있는 요소의 값 
# 누적 합 배열 출력
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(cumulative_sum[i][j], end=' ')
    print()