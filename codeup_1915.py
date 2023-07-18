# Codeup_Python 재귀함수_1915: (재귀 함수) 피보나치 수열
import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)
print(f(int(input())))