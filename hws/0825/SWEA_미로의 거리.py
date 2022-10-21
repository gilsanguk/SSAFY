from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if li[ny][nx] == 3:
                        return cnt - 1
                    if li[ny][nx] == 0 and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q.append((ny, nx))
    return 0

for T in range(int(input())):
    n = int(input())
    li = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if li[y][x] == 2:
                print(f'#{T + 1} {bfs(y, x)}')