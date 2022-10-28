for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    result = 0
    new_li = [0]*n
    for i in range(0, n):
        for j in range(i+1, n):
            if li[i] > li[j]:
                new_li[i] += 1
 
    for i in new_li:
        if result < i:
            result = i
 
    print(f'#{T+1} {result}')