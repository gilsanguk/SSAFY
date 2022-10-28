def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) >> 1]
    low, equ, high = [], [], []
    for num in arr:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            equ.append(num)
    return quick_sort(low) + equ + quick_sort(high)

for T in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = quick_sort(arr)
    print(f'#{T+1}', arr[n>>1])