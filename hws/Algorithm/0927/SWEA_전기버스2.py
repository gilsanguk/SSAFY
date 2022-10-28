for T in range(int(input())):
    arr = list(map(int,input().split()))
    n = arr[0]
    dp = [0] * (n+1)
    for i in range(n - 1, 0, -1):
        if i + arr[i] >= n + 1:
            dp[i] = 1
        else:
            dp[i] = min(dp[i + 1:i+arr[i]+1]) + 1
    print(f'#{T+1}', 0 if arr[1] + 1 >= n else dp[1] - 1)