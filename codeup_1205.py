# Codeup_Python 기초3.if~else_1205: 최댓값

a, b=map(float, input("실수를 입력하세요: ").split())
c=[]
for i in range(2):
    c.extend([a+b, a-b, a*b, a/b, a**b])        # append는 리스트에 원소를 하나씩 밖에 못넣으므로, extend를 사용해준다. 
    a,b = b,a
print(format(max(c), ".6f"))