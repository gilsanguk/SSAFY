def solve(curr, visited):
    if curr == n:
        return 0
    if dp[visited]:
        return dp[visited]

    for factory in range(n):
        if visited & (1 << factory): continue
        dp[visited] = min(
            dp[visited], solve(curr+1, visited | (1 << factory)) + arr[curr][factory]
        )
    return dp[visited]

for T in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dp = [2000] * (1 << n)
    solve(0, 0)
    print(f'#{T+1}', dp[0])