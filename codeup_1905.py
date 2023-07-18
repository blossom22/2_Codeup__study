# Codeup_Python 재귀함수_1905: (재귀 함수) 1부터 n까지 합 구하기

import sys
sys.setrecursionlimit(10**6)
# 재귀함수문제를 풀 경우, 위 코드 두줄을 꼭 써주자.
# 파이썬의 재귀 깊이제한은 1000으로 굉장히 짧다. 그래서 재귀조금 많이 돌리려고 하면, RecursionError 뜬다.
# 이 코드를 쓰면 재귀의 최대 깊이가 10**6으로 바뀌게 된다
def f(n,a):
    if n>0:
        a+=n
        f(n-1,a)
    else:
        print(a)
n = int(input())
f(n,a=0)