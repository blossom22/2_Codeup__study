# Codeup_Python 기초3.if~else_1286: 최댓값, 최솟값

a=[]
for i in range(5):
    i=int(input("정수를 입력하세요: "))
    a.append(i)
print(max(a))
print(min(a))


# 리스트 컴프리헨션을 사용하여 해결한 풀이이다. 
a = [int(input("정수를 입력하세요: ")) for i in range(5)]
print(max(a))
print(min(a))


# 초기값으로 엄청 크거나 작은 수를 설정해두고 비교하면서, max와 min값을 뽑아내는 방식이다. 
a = float('-inf')   # 음의 무한대를 나타내는 부동소수점 값이다. 이 값을 최대값으로 설정해두면 다른 어떤 수랑 비교해도 이 수보다는 클 것이다. 
b = float('inf')    # 양의 무한대를 나타내는 부동소수점 값으로, 사용원리는 위와 같다. 
for i in range(5):
    i = int(input("정수를 입력하세요: "))
    a = max(a, i)
    b = min(b, i)
print(a)
print(b)

# sort함수로 정렬을 한 후, 최소값과 최대값을 뽑아내는 방식이다. 
a=[int(input())for i in'i'*5]
a.sort()
print(a[-1])
print(a[0])
