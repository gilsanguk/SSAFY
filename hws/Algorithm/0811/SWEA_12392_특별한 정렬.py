for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    lst = []
    while len(li) > 1:
        max_idx = 0
        min_idx = 0
        for i in range(len(li)):
            if li[i] > li[max_idx]:
                max_idx = i
            if li[i] < li[min_idx]:
                min_idx = i
        if max_idx > min_idx:
            a, b = li.pop(max_idx), li.pop(min_idx)
        else:
            b, a = li.pop(min_idx), li.pop(max_idx)
        lst += [a,b]
    if li:
        lst.append(li.pop())
    print(f'#{T + 1}', end=' ')
    for i in range(10):
        print(lst[i],end=' ')
    print()
