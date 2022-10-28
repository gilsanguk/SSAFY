def solve(li):
    op = ['(','{']
    cl = [')','}']
    stack = []
    for i in range(len(li)):
        if li[i] == op[0] or li[i] == op[1]:
            stack.append(li[i])
        elif li[i] == cl[0]:
            if stack and stack[-1] == op[0]:
                stack.pop()
            else:
                return 0
        elif li[i] == cl[1]:
            if stack and stack[-1] == op[1]:
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    return 1

for T in range(int(input())):
    li = list(input())
    print(f'#{T+1} {solve(li)}')