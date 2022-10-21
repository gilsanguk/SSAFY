from collections import deque

for T in range(int(input())):
    n, m = map(int, input().split())
    li = deque(map(int, input().split()))
    for i in range(m%n):
        li.append(li.popleft())
    print(f'#{T+1} {li[0]}')