# Codeup_Python 기초100제_1555: 함수로 n까지의 합 리턴하기

def f(n):
    a = 0
    for i in range(1,n+1):
        a+=i
    print(a)
n = int(input())
f(n)

# 등차수열 합공식으로 푸는 방법도 있다. 
def f(n):
    a = (n*(n + 1))//2      # 여기서 2로 나누는데, '//' 쓴이유: 어차피 n(n+1)은 짝수인데, 단순히 '/'로 나누면 뒤에 소수점이 붙는다. 이를 방지하기 위해 '//'쓴 것
    return a
n = int(input())
print(f(n))