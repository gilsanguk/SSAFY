from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(s, g):
    q = deque()
    q.append(s)
    visited[s] = 1
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            s = q.popleft()
            for i in li[s]:
                if i == g:
                    return cnt
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
    return 0


for T in range(int(input())):
    n, m = map(int, input().split())
    li = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for _ in range(m):
        s, e = map(int, input().split())
        li[s].append(e)
        li[e].append(s)
    s, g = map(int,input().split())
    print(f'#{T + 1} {bfs(s, g)}')