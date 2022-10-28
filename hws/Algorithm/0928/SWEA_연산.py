from collections import deque
  
def bfs(n):
    q = deque([n])
    while q:
        n = q.popleft()
        if n == m: return visited[n]
        for a in [n+1, n-1, n*2, n-10]:
            if 0 <= a < MAX and not visited[a]:
                visited[a] = visited[n] + 1
                q.append(a)
  
for T in range(int(input())):
    n, m = map(int, input().split())
    MAX = 1000001
    visited = [0] * (MAX)
    print(f'#{T+1}', bfs(n))