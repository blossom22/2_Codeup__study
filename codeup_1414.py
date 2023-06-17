# Codeup_Python 기초5-2.문자열_1414: C언어를 찾아라

a = input()
b = len(a)
d = a.count('c') + a.count('C')
e = ['cc', 'CC', 'cC', 'Cc']
f = sum(1 for i in range(b - 1) if a[i:i+2] in e)
print(d)
print(f)


# 아래는 d를 구할때, count를 쓰지 않고 구한 방식이다
a = input()
b = len(a)
d = sum(1 for i in a if i == 'c' or i == 'C')
e = {'cc', 'CC', 'cC', 'Cc'}
f = sum(1 for i in range(b - 1) if a[i:i+2] in e)

print(d)
print(f)