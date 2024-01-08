# Codeup_이분탐색_2633: Lower Bound
# 해결책은 두가지이다. 

# 1. bisect 라이브러리를 사용하는 방법이다. 
from bisect import bisect_left
import sys
n,k = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
ans = bisect_left(nl, k)+1
print(n+1) if ans==n else print(ans)

# 2. 이분탐색 개념을 활용
import sys
n,k = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
def solution(nl, k):
    left = 0
    right = n
    while left<right:
        mid = (left+right)//2
        if nl[mid]<k:
            left = mid + 1
        else:
            right = mid
    return n+1 if right==n else right+1
print(solution(nl, k))