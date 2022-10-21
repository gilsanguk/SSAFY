def dijkstra():
    w_list = [0] + [11] * v
    visited = [0] * (v + 1)
    res = 0
    for _ in range(v+1):
        s, w = 0, 11
        for i in range(v+1):
            if not visited[i] and w_list[i] < w:
                s, w = i, w_list[i]
        visited[s] = 1
        res += w
        for e, w in graph[s]:
            if w_list[e] > w:
                w_list[e] = w
    return res

for T in range(int(input())):
    v, e = map(int,input().split())
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        s, e, w = map(int,input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))
    print(f'#{T+1}', dijkstra())