def bubble_sort(lst, n):
    for i in range(n):
        for j in range(i, n - 1):
            if lst[i] > lst[j + 1]:
                lst[i], lst[j + 1] = lst[j + 1], lst[i]
    return lst


for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li = bubble_sort(li, n)

    print(f'#{T + 1} {li[-1] - li[0]}')
