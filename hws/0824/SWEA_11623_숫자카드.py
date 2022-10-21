from collections import deque

for T in range(int(input())):
    li = deque(range(1, int(input()) + 1))
    while len(li) > 2:
        li.popleft()
        li.append((li.popleft()))
    print(f'#{T + 1} {li[-1]}')