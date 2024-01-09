# Codeup_스택_3021: 큰 수 덧셈

import sys
a = list(map(int, list(sys.stdin.readline().strip())))
b = list(map(int, list(sys.stdin.readline().strip())))
# 더 큰 수를 a로, 더 작은 수를 b로 한다.  
if len(a)<len(b):
    a,b = b,a
result = []
tmp = 0     # 자릿수 올림시 사용하는 변수
hap = 0     # 임시로 쓰는 부분의 합 

# 먼저 작은 수(b)가 있는 자릿수부터 처리한다.
for i in range(len(b)):
    hap = a.pop() + b.pop() + tmp
    if hap>=10:
        tmp = 1
        result.append(hap-10)
    else:
        result.append(hap)
        tmp = 0

# 이제 큰 수(a)만 존재하는 자릿수를 처리한다.(앞서 a,b가 공통으로 있는 부위는 pop하면서 다 처리됨)
for i in range(len(a)):
    hap = a.pop() + tmp
    if hap>=10:
        tmp = 1
        result.append(hap-10)
    else:
        tmp = 0
        result.append(hap)
if tmp==1:
    result.append(1)
result.reverse()
print(*result, sep='')