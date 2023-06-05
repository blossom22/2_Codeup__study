# Codeup_Python 기초3.if~else_1224: 분수 크기 비교

a,b,c,d = map(int, input("자연수를 입력하세요: ").split())
e=a/b
f=c/d
print('>') if e>f else print('<') if e<f else print('=')
