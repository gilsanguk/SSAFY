dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for T in range(int(input())):
    n, m = map(int, input().split())
    li = [(list(map(int, input().split()))) for _ in range(n)]
    res = set()
    cnt = 0
    for _ in range(m):
        y, x, b = map(int, input().split())
        res.add((y,x))
        for i in range(4):
            for j in range(1, b + 1):
                ny, nx = y + j * dy[i], x + j * dx[i]
                if 0 <= ny < n and 0 <= nx <n:
                    res.add((ny,nx))
    for y, x in res:
        cnt += li[y][x]
    print(f'#{T+1} {cnt}')