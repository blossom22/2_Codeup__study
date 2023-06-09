# Codeup_Python 기초3.단순 반복문_1280: 홀수는 더하고 짝수는 빼고 2

a, b=map(int, input("두 자연수를 입력하세요: ").split())
c=0
d=[]
for i in range(a,b+1):
    if i % 2 == 1:
        c += i
        d.append("+"+str(i))
    else:
        c -= i
        d.append("-"+str(i))
d.append("="+str(c))
print(''.join(d))

