def solve():
    dp[0][0] = li[0][0]
    for y in range(n):
        for x in range(n):
            if dp[y][x] == -1:
                if y == 0:
                    dp[y][x] = dp[y][x-1] + li[y][x]
                elif x == 0:
                    dp[y][x] = dp[y-1][x] + li[y][x]
                else:
                    dp[y][x] = min(dp[y-1][x] + li[y][x], dp[y][x-1] + li[y][x])
    return dp[n-1][n-1]

for T in range(int(input())):
    n = int(input())
    li = [list(map(int,input().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(n)]
    print(f'#{T+1}', solve())