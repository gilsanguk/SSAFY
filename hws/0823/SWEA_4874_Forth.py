def operate(a, b, c):
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        return a//b

def solve():
    operator = ['+', '-', '*', '/']
    try:
        stack = [int(li[0]), int(li[1])]
        for i in range(2, len(li) - 1):
            if li[i] in operator:
                b, a, c = stack.pop(), stack.pop(), li[i]
                stack.append(operate(a, b, c))
            else:
                stack.append(int(li[i]))
        if len(stack) == 1:
            return stack[0]
        else:
            return 'error'
    except:
        return 'error'

for T in range(int(input())):
    li = list(input().split())
    print(f'#{T+1} {solve()}')