from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
MAX = 1000000
def dijkstra():
    q = deque([(0, 0)])
    visited = [[MAX] * n for _ in range(n)]
    visited[0][0] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                tmp = visited[y][x] + 1 + max(0, (graph[ny][nx] - graph[y][x]))
                if visited[ny][nx] > tmp:
                    visited[ny][nx] = tmp
                    q.append((ny,nx))
    return visited[n-1][n-1]

for T in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{T + 1}', dijkstra())

#############################################################################
# using PriorityQ
from heapq import heappush, heappop
delta = [(-1,0), (0, 1), (1, 0), (0, -1)]
def dijkstra():
    q = [(0, 0, 0)]
    while q:
        d, y, x = heappop(q)
        if y == n - 1 and x == n - 1: return d
        if visited[y][x]: continue
        visited[y][x] = True
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                nd = d + 1 + max(0, (graph[ny][nx] - graph[y][x]))
                heappush(q, (nd, ny, nx))

for T in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    print(f'#{T + 1}', dijkstra())
