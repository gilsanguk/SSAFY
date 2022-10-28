def my_sort(lst, N):
    for i in range(N):
        for j in range(i, N - 1):
            if lst[i] > lst[j + 1]:
                lst[i], lst[j + 1] = lst[j + 1], lst[i]
    return lst
 
 
for T in range(10):
    n = int(input())
    li = list(map(int, input().split()))
    while n > 0:
        my_sort(li, len(li))
        li[-1] -= 1
        li[0] += 1
        n -= 1
    my_sort(li, len(li))
 
    print(f'#{T + 1} {li[-1] - li[0]}')