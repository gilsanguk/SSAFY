def my_sum(li):
    result = 0
    for i in li:
        result += i
    return result


for T in range(int(input())):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << n):
        part_li = []
        for j in range(n):
            if i & (1 << j):
                part_li.append(li[j])
        if my_sum(part_li) == k:
            cnt += 1

    print(f'#{T + 1} {cnt}')
