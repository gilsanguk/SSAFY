def solve():
    n, m, k = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    for i in range(n):
        if (li[i] // m) * k < i+1:
            return 'Impossible'
    return 'Possible'


for T in range(int(input())):
    print(f'#{T+1} {solve()}')