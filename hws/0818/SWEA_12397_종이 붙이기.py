dp = [0]*31
def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if dp[n]:
        return dp[n]
    dp[n] = paper(n-1) + 2*paper(n-2)
    return dp[n]
for T in range(int(input())):
    n = int(input())
    print(f'#{T+1} {paper(n//10)}')