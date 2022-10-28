def my_sum(li):
    result = 0
    for i in li:
        result += i
    return result

for T in range(int(input())):
    n, k = map(int, input().split())
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    tmp = []
    subset = []
    cnt = 0
    for i in range(1<<len(li)):
        for j in range(len(li)):
            if i & (1<<j):
                tmp.append(li[j])
        subset.append(tmp)
        tmp = []
    for i in subset:
        if len(i) == n:
            if my_sum(i) == k:
                cnt+=1

    print(f'#{T + 1} {cnt}')