def backtrack(curr, total, add, sub, mul, div):
    global MAX, MIN
    if curr == n:
        MAX = max(total, MAX)
        MIN = min(total, MIN)
        return
    if add: backtrack(curr + 1, total + nums[curr], add-1, sub, mul, div)
    if sub: backtrack(curr + 1, total - nums[curr], add, sub-1, mul, div)
    if mul: backtrack(curr + 1, total * nums[curr], add, sub, mul-1, div)
    if div: backtrack(curr + 1, int(total / nums[curr]), add, sub, mul, div-1)

for T in range(int(input())):
    n = int(input())
    add, sub, mul, div = map(int,input().split())
    nums = list(map(int, input().split()))
    MAX, MIN = -100000001, 100000000
    backtrack(1, nums[0], add, sub, mul, div)
    print(f'#{T+1}', MAX-MIN)