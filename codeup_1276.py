# Codeup_Python 기초3.단순 반복문_1276: 팩토리얼 계산

n=int(input("자연수를 입력하세요: "))
for i in range(n-1,0,-1):
    n=n*i
print(n)


# 위랑 큰차이는 없다. 
# 이 코드는 팩토리얼계산할때 오름차순으로 하고, 1은 곱하나마나 결과에 차이가 없어 제외했으므로, 위의 코드보다 for문을 조금이라도 덜 돌린다. 
n=int(input("자연수를 입력하세요: "))
a=1
for i in range(2, n+1):
    a*=i
print(a)