# Codeup_Python 기초5-1.1차원배열_1410: 올바른 괄호 1 (괄호 개수 세기)

a=input()
b=0
c=0
for i in range(len(a)):
    if a[i]=='(':
        b+=1
    else:
        c+=1
print(b,c)

# 아니면, 어차피 '(' 아니면 ')'니까 이렇게 풀수도있다. 
a = input()
b = a.count('(')
c = len(a) - b
print(b, c)
