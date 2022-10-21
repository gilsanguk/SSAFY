def dfs(s):
    visited[s] = 1
    for node in graph[s]:
        if visited[node]: continue
        dfs(node)

for T in range(int(input())):
    n, m = map(int,input().split())
    tmp = list(map(int,input().split()))
    visited = [0] * (n+1)
    graph = [[] for _ in range(n + 1)]
    res = 0
    for i in range(0, m*2, 2):
        graph[tmp[i]].append(tmp[i+1])
        graph[tmp[i+1]].append(tmp[i])
    for i in range(1,n+1):
        if visited[i]: continue
        dfs(i)
        res += 1
    print(f'#{T+1}', res)