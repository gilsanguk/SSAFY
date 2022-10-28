from collections import deque

for _ in range(10):
    n = int(input())
    li = deque(map(int, input().split()))
    minv, idx = min(li), li.index(min(li))
    tmp = minv - minv % 15 - 15
    for i in range(8):
        li[i] = li[i] - tmp
    while li[-1]:
        for i in range(1, 6):
            tmp = li.popleft() - i
            if tmp <= 0:
                li.append(0)
                break
            li.append(tmp)
    print(f'#{n}', end=' ')
    print(*li)
