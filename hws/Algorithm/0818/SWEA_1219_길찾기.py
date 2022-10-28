def DFS(graph,route):
    visited = []
    stack = [route]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n not in graph:
                continue
            stack += graph[n] - set(visited)
    return visited

def solve(e):
    li = list(map(int, input().split()))
    graph = {}
    for i in range(1,e*2,2):
        s, e = li[i-1], li[i]
        if s in graph:
            graph[s].add(e)
        else:
            graph[s] = {e}
    if 99 in DFS(graph,0):
        return 1
    return 0

for i in range(10):
    T, e = map(int, input().split())
    print(f'#{T} {solve(e)}')