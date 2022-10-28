def solve():
    c_li = list(zip(*li))
    cnt = 0
    for x in range(100):
        stack = []
        for y in range(100):
            if len(stack) == 0:
                if c_li[x][y] == 1:
                    stack.append(c_li[x][y])
            else:
                if c_li[x][y] != 0 and c_li[x][y] != stack[-1]:
                    stack.append(c_li[x][y])
        cnt += len(stack) // 2
    return cnt

for T in range(10):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{T+1} {solve()}')