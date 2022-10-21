def backtrack():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    s, e = 0, 0
    for i in range(n):
        for j in range(n):
            if li[i][j] == 2:
                y, x = i, j
                s += 1
            elif li[i][j] == 3:
                e += 1
    if s != 1 or e != 1:
        return 'error'
    stack = [(y, x)]
    visited = [[0] * n for _ in range(n)]
    while stack:
        y, x = stack.pop()
        visited[y][x] = 1
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if li[ny][nx] == 3:
                    return 1
                elif li[ny][nx] == 0 and not visited[ny][nx]:
                    stack.append((ny, nx))
    return 0

for T in range(int(input())):
    n = int(input())
    li = [(list(map(int, input()))) for _ in range(n)]
    print(f'#{T+1} {backtrack()}')