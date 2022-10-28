def DFS(graph,route):
    visited = set()
    stack = [route]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            if n not in graph:
                continue
            stack += graph[n] - visited
    return visited

def solve():
    _, e = map(int, input().split())
    graph = {}
    for _ in range(e):
        s, e = map(int, input().split())
        if s in graph:
            graph[s].add(e)
        else:
            graph[s] = {e}
    s, e = map(int, input().split())
    if e in DFS(graph,s):
        return 1
    return 0

for T in range(int(input())):
    print(f'#{T+1} {solve()}')