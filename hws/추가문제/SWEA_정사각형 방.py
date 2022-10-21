dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for T in range(int(input())):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    tmp = [0] * ((n ** 2) + 1)
    idx, res = 1, 1
    for y in range(n):
        for x in range(n):
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and li[ny][nx] == li[y][x] + 1:
                    tmp[li[y][x]] = 1
    for i in range((n**2), -1, -1):
        tmp[i-1] = (tmp[i] + tmp[i-1]) * tmp[i-1]
    for i in range((n ** 2) + 1):
        if res < tmp[i] + 1:
            res, idx = tmp[i] + 1, i
    print(f'#{T+1}', idx, res)