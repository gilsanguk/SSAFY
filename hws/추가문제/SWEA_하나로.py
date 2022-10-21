def dijkstra(s):
    fee_list = [0] + [INF] * (n-1)
    visited = [False] * n
    res = 0
    for _ in range(n):
        s, fee = 0, INF
        for i in range(n):
            if not visited[i] and fee_list[i] < fee:
                s, fee = i, fee_list[i]
        visited[s] = True
        res += E * fee
        for i in range(len(graph_x)):
            fee = (graph_x[s] - graph_x[i]) ** 2 + (graph_y[s] - graph_y[i]) ** 2
            if fee_list[i] > fee:
                fee_list[i] = fee
    return res

for T in range(int(input())):
    n = int(input())
    graph_x = list(map(int, input().split()))
    graph_y = list(map(int, input().split()))
    E = float(input())
    INF = float('inf')
    print(f'#{T + 1}', round(dijkstra(0)))