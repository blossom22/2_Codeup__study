# Codeup_Python 기초4-2.중첩반복문_1369: 빗금 친 사각형 출력하기

def ddd(n, k):
    for i in range(n):          # 행
        for j in range(n):      # 열
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print("*", end="")
            elif (i + j) % k == k - 1:      # 빗금 
                print("*", end="")
            else:
                print(" ", end="")
        print()
n, k = map(int, input().split())
ddd(n, k)