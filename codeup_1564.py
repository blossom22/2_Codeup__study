# Codeup_Python 기초100제_1564: 함수로 최대공약수 리턴하기

import sys
def f(a,b):
    if b==0:
        return a
    return f(b,a%b)

a,b = map(int, sys.stdin.readline().split())
print(f(a,b))

'''
a,b 각각의 약수를 구해서 공통되는 약수중 가장 큰 값을 찾는 것은 비효율적이다.
for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i == 0:
        return i
따라서 유클리드 호제법을 이용했다.
"a를 b로 나눈 나머지와 b"의 최대공약수는 "a와 b의 최대공약수"와 같다는 사실을 이용
'''