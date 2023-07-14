# Codeup_Python 기초100제_1542: 함수로 prime 또는 composite 출력하기

import sys
def f(n):
    a = True
    for i in range(2, int(n**0.5) + 1):     # n의 제곱근까지만 봐도 된다. 어차피 소수가 아니라면 약수들이 중복될테니까.
        if n % i == 0:
            a = False
            break
    print('prime' if a else 'composite')
n = int(sys.stdin.readline())
f(n)