for T in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    res = 987654321
    dp = set()
    for i in range(n):
        num = li[i]
        now = {num}
        for j in dp:
            tmp = num+j
            if tmp >= res: continue
            if tmp >= k:
                res = min(res, tmp)
            now.add(tmp)
        for j in now:
            dp.add(j)
    print(f'#{T+1}', res-k)

############################################################
def track(depth, tmp):
    global res, max_v
    if depth == n:
        if tmp >= b: res = min(tmp, res)
        return
    if tmp > res or (n-depth) * max_v + tmp < b: return
    for i in range(2):
        if i & 1: track(depth+1, tmp + li[depth])
        else: track(depth+1, tmp)

for T in range(int(input())):
    n, b = map(int,input().split())
    li = list(map(int,input().split()))
    max_v = max(li)
    res = 987654321
    track(0,0)
    print(f'#{T+1}', res-b)