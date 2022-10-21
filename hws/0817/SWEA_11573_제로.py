for T in range(int(input())):
    stack = []
    result = 0
    k = int(input())
    li = list(map(int, input().split()))
    for tmp in li:
        if tmp:
            stack.append(tmp)
        else:
            if len(stack):
                stack.pop()
    for i in range(len(stack)):
        result += stack[i]
    print(f'#{T+1} {result}')