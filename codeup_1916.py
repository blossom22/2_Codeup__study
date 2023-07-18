# Codeup_Python 재귀함수_1916: (재귀 함수) 피보나치 수열 (Large)

import sys
sys.setrecursionlimit(10**6)
memo = {}   # 메모이제이션을 위한 딕셔너리를 생성

def f(n):
    if n in memo:
        return memo[n]  # n이 memo의 key로 존재하는지 확인해서, 이미 저장된 결과가 있다면, memo[n]반환하고 재귀호출X
    if n <= 1:
        memo[n] = n % 10009
        return memo[n]
    # 재귀 호출
    memo[n] = (f(n-1) + f(n-2)) % 10009
    return memo[n]

print(f(int(input())))