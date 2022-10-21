for T in range(int(input())):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort()
    t.sort()
    res = 0
    while t:
        now = t.pop()
        while w:
            tmp = w.pop()
            if tmp <= now:
                res += tmp
                break
    print(f'#{T + 1}', res)