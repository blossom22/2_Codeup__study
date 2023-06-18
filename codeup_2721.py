# Codeup_Python 기초5-2.문자열_2721: 순환 문자열

a = input()
b = input()
c = input()
if a[-1] == b[0] and b[-1] == c[0] and c[-1] == a[0]:
    print('good')
else:
    print('bad')