# Codeup_Python 기초100제_1565: 함수로 최소공배수 리턴하기


import sys
def g(a,b):
    if b==0:
        return a
    return g(b,a%b)

def f(a,b):
    result = (a*b)//g(a,b)      # a랑 b를 곱한후, 최대공약수로 나누면 된다. 그게 곧 최소공배수
    return result
a,b = map(int, sys.stdin.readline().split())
print(f(a,b))

'''
그냥 소인수분해로 하면 이렇게 풀 수 있지만, 비효율적이다
for i in range(max(a,b),(a*b)+1):
    if i%a==0 and i%b==0:
        print(i)
        break
'''