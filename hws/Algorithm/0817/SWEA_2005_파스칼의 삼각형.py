def pascal(n):
    if n < 2:
        return 0
    pascal(n-1)
    for i in range(1,n):
        res[n][i] = res[n-1][i-1] + res[n-1][i]

for T in range(int(input())):
    n = int(input())
    res=[[1]*(i+1) for i in range(n)]
    print(f'#{T+1}')
    pascal(n-1)
    for i in range(len(res)):
        print(*res[i])