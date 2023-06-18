# Codeup_Python 기초5-2.문자열_6130: 일차 방정식 ax±b=0의 해 구하기

a = input()
b = a.index('x')
if a[b+1]=='+':
    print('{:.2f}'.format((-int(''.join(a[b+2:])))/int(''.join(a[:b]))))
else:
    print('{:.2f}'.format((int(''.join(a[b+2:])))/int(''.join(a[:b]))))