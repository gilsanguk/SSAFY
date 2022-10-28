for T in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    dp = {}
    for i in range(n):
        num = li[i]
        now = {}
        now[num] = 1
        for k, v in dp.items():
            if num+k in now: now[num+k] += v
            else: now[num + k] = v
        for k, v in now.items():
            if k in dp: dp[k] += v
            else: dp[k] = v
    print(f'#{T+1}', dp[m] if m in dp else 0)