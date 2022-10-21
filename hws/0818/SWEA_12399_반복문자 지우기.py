def pang(w):
    stack = []
    while w:
        if stack and stack[-1] == w[-1]:
            stack.pop()
            w.pop()
        else:
            stack.append(w.pop())
    return len(stack)

for T in range(int(input())):
    w = list(input())
    print(f'#{T+1} {pang(w)}')