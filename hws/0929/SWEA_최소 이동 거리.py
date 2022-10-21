from heapq import heappush, heappop
def dijkstra():
    q = [(0, 0)]
    visited = [0] * (n + 1)
    while q:
        d, s = heappop(q)
        visited[s] = 1
        for e, w in graph[s]:
            if e == n: return d + w
            if visited[e]: continue
            heappush(q, (d + w, e))


for T in range(int(input())):
    n, e = map(int,input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(e):
        s, e, w = map(int,input().split())
        graph[s].append((e,w))
    print(f'#{T+1}', dijkstra())

####################################################
# O(n^2) dp  의미있나..?
for T in range(int(input())):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dp = [987654321] * (n+1)
    dp[0] = 0
    for i in range(k):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
 
    for s in range(n+1):
        for e, w in graph[s]:
            dp[e] = min(dp[e], dp[s] + w)
    print(f'#{T+1}', dp[n])