for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
 
    result = 0
    for i in range(n - 1):
        if li[i] + li[i + 1] > result:
            result = li[i] + li[i + 1]
 
    print(f'#{T + 1} {result}')