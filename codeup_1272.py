# Codeup_Python 기초3.단순 반복문_1272: 기부

# 수의 특성을 이용한 풀이이다. 
a=list(map(int, input("두 수를 입력하세요: ").split()))
b=0
for i in a:
    if i%2==0:
        b+=i*5
    else:
        b+=(i+1)/2
print(round(b))

# 위의 코드를 리스트 컴프리헨션으로 코드를 간결하게 만들어보았다. 
a = list(map(int, input("두 수를 입력하세요: ").split()))
b = sum([i*5 if i % 2 == 0 else (i+1)/2 for i in a])
print(round(b))
