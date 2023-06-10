# Codeup_Python 기초3.if~else_1675: 시저의 암호 1

a=input("암호문을 입력하세요: ")
b=[]
for i in range(len(a)):
    if a[i]!=' ' and ord(a[i]) >= 100:
        b.append(chr(ord(a[i])-3))
    elif a[i]!=' ' and ord(a[i]) < 100:
        b.append(chr(ord(a[i])+23))
    else: 
        b.append(' ')
print(''.join(b))
