from collections import defaultdict

def solve():
    o, t = defaultdict(int), defaultdict(int)
    tmp = [o, t]
    for i in range(len(li)):
        dct = tmp[i & 1]
        dct[li[i]] += 1
        win = (i & 1) + 1
        if dct[li[i]] == 3: return win
        if dct[li[i]-2] and dct[li[i] - 1]: return win
        if dct[li[i]-1] and dct[li[i] + 1]: return win
        if dct[li[i]+1] and dct[li[i] + 2]: return win
    return 0


for T in range(int(input())):
    li = list(map(int, input().split()))
    print(f'#{T+1}', solve())