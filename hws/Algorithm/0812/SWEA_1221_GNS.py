num=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for T in range(int(input())):
    cnt = [0]*10
    a, b = map(str, input().split())
    li = list(map(str, input().split()))
    for i in range(int(b)):
        for j in range(10):
            if li[i] == num[j]:
                cnt[j] += 1
    for i in range(10):
        print(f'#{T + 1}')
        while cnt[i] > 0:
            print(num[i],end=' ')
            cnt[i]-=1
    print()