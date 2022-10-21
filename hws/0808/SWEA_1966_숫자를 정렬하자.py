for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
 
    for i in range(n):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
 
    print(f'#{T + 1} {" ".join(map(str, li))}')