dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solve(y, x):
    global res

    visited[y][x] = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if li[ny][nx] == 3:
            res = 1
            return
        if li[ny][nx] == 0 and not visited[ny][nx]:
            solve(ny, nx)

for _ in range(10):
    n = int(input())
    li = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    res = 0
    for y in range(16):
        for x in range(16):
            if li[y][x] == 2:
                solve(y, x)
    print(f'#{n} {res}')