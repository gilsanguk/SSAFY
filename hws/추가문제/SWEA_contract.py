from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    visited = [False] * (101)
    visited[s] = True
    while q:
        cur = list(q)[:]
        for _ in range(len(q)):
            s = q.popleft()
            for i in li[s]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
    return cur

for T in range(10):
    n, s = map(int, input().split())
    li = [set() for _ in range(101)]
    tmp = list(map(int, input().split()))
    for i in range(0, len(tmp), 2):
        li[tmp[i]].add(tmp[i + 1])
    print(f'#{T+1}', max(bfs(s)))