# Codeup_Python 기초5-2.문자열_1408: 암호 처리

a = input()
b = len(a)
for i in range(b - 1):
    print(chr(ord(a[i]) + 2), end='')
print(chr(ord(a[b - 1]) + 2))       # 마지막 문자에서 줄바꿈 해야므로. 굳이 if문 걸지말고 처음부터 이렇게 하면 불필요한 연산 줄일수있다. 

for i in range(b):
    print(chr((ord(a[i]) * 7) % 80 + 48), end='')