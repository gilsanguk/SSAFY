# 반복
for T in range(int(input())):
    day, mon, tri, year = map(int,input().split())
    month = [0] + list(map(int,input().split()))
    memo = [0] * 13
    for i in range(1, 13):
        if i < 3:
            memo[i] = memo[i - 1] + min(month[i] * day, mon)
        else:
            memo[i] = min(memo[i - 1] + min(month[i] * day, mon), memo[i-3] + tri)
    print(f'#{T+1}', min(memo[-1], year))

###################################################################
# 재귀
def dp(curr):
    if curr == 13: return 0
    if curr > 10:
        memo[curr] = min(month[curr] * day, mon) + dp(curr+1)
    else:
        memo[curr] = min(min(month[curr] * day, mon) + dp(curr+1), dp(curr+3) + tri)
    return memo[curr]
for T in range(int(input())):
    day, mon, tri, year = map(int,input().split())
    month = [0] + list(map(int,input().split()))
    memo = [0] * 13
    print(f'#{T+1}', min(dp(0), year))