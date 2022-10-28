def init(k):
    global i
    if k > n: return
    init(k << 1)
    tree[k] = i
    i += 1
    init((k << 1) | 1)


for T in range(int(input())):
    n = int(input())
    tree = [0] * (n + 1)
    i = 1
    init(1)
    print(f'#{T+1}', tree[1], tree[n >> 1])