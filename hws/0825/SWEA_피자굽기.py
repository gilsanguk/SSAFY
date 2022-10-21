from collections import deque

def solve():
    q = deque()
    while len(q) != n:
        q.append(li.popleft())
    while len(q) != 1:
        idx, tmp = q.popleft()
        if tmp//2:
            q.append((idx, tmp//2))
        elif tmp//2 == 0 and li:
            q.append(li.popleft())
    return q[0][0] + 1

for T in range(int(input())):
    n, m = map(int, input().split())
    li = deque(map(int, input().split()))
    li = deque(enumerate(li))
    print(f'#{T + 1} {solve()}')