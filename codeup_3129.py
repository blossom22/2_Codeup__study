# Codeup_스택_3129: 올바른 괄호 2

w = list(input())
stack = []
for i in w:
    if i=='(':
        stack.append(i)
    elif i==')' and stack:
        if stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)
    elif i==')' and not stack:
        stack.append(i)
print('bad') if stack else print('good')