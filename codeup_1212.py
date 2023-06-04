# Codeup_Python 기초3.if~else_1212: 삼각형의 성립 조건

a=list(map(int, input('직선의 길이를 입력하세요: ').split()))
a.sort()
print('yes') if a[2]<(a[0]+a[1]) else print('no')

# sort를 쓰지 않고 푸는 방법으로 '버블정렬'이 있다.
# 버블정렬이란 두 개의 자료를 서로 비교하고 값이 더 작은 것을 앞으로 보내는 것을 끝날 때 까지 반복하는 것이다.
a=list(map(int, input('직선의 길이를 입력하세요: ').split()))
for j in range(len(a)):
    k = len(a)-j
    for i in range(1,k):
        if a[i-1] >= a[i]:
            a[i],a[i-1]=a[i-1],a[i]     # 임시변수 하나 만들어서 해도되고, XOR연산자 이용해도 된다. 
print('yes') if a[2]<(a[0]+a[1]) else print('no')

