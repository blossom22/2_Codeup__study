# Codeup_Python 기초3.단순 반복문_1281: 홀수는 더하고 짝수는 빼고 3

a, b=map(int, input("두 자연수를 입력하세요: ").split())
c=0
d=[]
if a%2==1:
    d.append(str(a))
else:
    d.append(str(-a))
for i in range(a+1,b+1):
    if i % 2 == 1:
        c += i
        d.append("+"+str(i))
    else:
        c -= i
        d.append("-"+str(i))
d.append("="+str(int(d[0])+c))
print(''.join(d))


# 위의 코드를 줄여보았다. 
a, b = map(int, input("두 자연수를 입력하세요: ").split())
c = 0
d = []
d.append(str(a) if a % 2 == 1 else str(-a))
for i in range(a + 1, b + 1):
    c += i if i % 2 == 1 else -i
    d.append(("+" if i % 2 == 1 else "-") + str(i))
d.append("="+str(int(d[0])+c))
print(''.join(d))