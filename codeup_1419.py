# Codeup_Python 기초5-2.문자열_1419: love 2

a = input()
b = len(a)
c = sum(1 for i in range(b - 3) if a[i:i+4] == 'love')
print(c)