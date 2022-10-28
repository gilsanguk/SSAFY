for T in range(int(input())):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 2)
    for i in range(m):
        a, b = map(int, input().split())
        tree[a] = b
        while a > 1:
            a >>= 1
            tree[a] = tree[a << 1] + tree[(a << 1) | 1]
    print(f'#{T+1}', tree[l])