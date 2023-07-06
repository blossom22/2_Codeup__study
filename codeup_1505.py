# Codeup_Python 기초5-3.2차원배열_1505: 2차원 배열 채우기 3(달팽이 배열)

n = int(input())

# 달팽이 배열 초기화
arr = [[0] * n for _ in range(n)]

# 이동 방향 (우>하>좌>상)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_idx = 0

# 현재 위치(인덱스)
row = 0
col = 0

# 배열에 숫자 채우는 for문
for num in range(1, n**2 + 1):
    arr[row][col] = num

    # 다음 위치 계산 (현재위치+이동방향에 따른 row와 col의 변화량을 더한다)
    next_row = row + directions[direction_idx][0]
    next_col = col + directions[direction_idx][1]

    # 다음 위치가 배열 범위를 벗어나거나 이미 숫자가 채워져 있을 경우 방향 전환 (row나 col은 n*n배열에 한정되므로, idx값이 음수거나 n이상이면 안된다)
    # 숫자채우는 과정에서 거꾸로 왔던 길을 가려고 하면, 이동방향을 바꿔야 한다 (역주행을 막기 위해서는 이미 채워진(즉, 0이 아닌)길은 못가게 해야한다)
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or arr[next_row][next_col] != 0:
        direction_idx = (direction_idx + 1) % 4

    # 다음 위치로 이동
    row += directions[direction_idx][0]
    col += directions[direction_idx][1]

# 달팽이 배열 출력
for row in arr:
    print(*row)