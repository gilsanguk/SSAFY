for T in range(10):
    n = int(input())
    w = input()
    stack = [int(w[0])]
    i = 0
    while i != n-1:
        if w[i+1] == '*':
            stack[-1] = stack[-1] * int(w[i+2])
        else:
            stack.append(int(w[i+2]))
        i += 2
    print(f'#{T+1} {sum(stack)}')