# Codeup_Python 기초3.단순 반복문_1266: n개의 수의 합

n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
print(sum(a))

# 그냥 위처럼 sum함수 써서 해결할 수 있지만, 출제자의 의도에 맞게 반복문을 써서 해결해보았다. 
n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
b=0
for i in range(n):
    b+=a[i]
print(b)