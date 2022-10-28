for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
 
    max_v = 0
    min_v = n - 1
    for i in range(1, n):
        if li[i] >= li[max_v]:
            max_v = i
 
    for j in range(n - 2, -1, -1):
        if li[j] <= li[min_v]:
            min_v = j
    result = max_v - min_v
 
    if result < 0:
        result = -result
 
    print(f'#{T + 1} {result}')