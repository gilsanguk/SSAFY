def merge_sort(s, e):
    if e - s < 2: return
    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m, e)
    merge(s, m, e)

def merge(s, m, e):
    global cnt
    tmp = []
    i, j = s, m
    if arr[m-1] > arr[e - 1]: cnt += 1
    while i < m and j < e:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i < m:
        tmp.append(arr[i])
        i += 1
    while j < e:
        tmp.append(arr[j])
        j += 1
    arr[s:e] = tmp

for T in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, n)
    print(f'#{T+1}', arr[n//2], cnt)