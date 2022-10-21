dct = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

def possible(s, leng):
    li = s[(-leng) * 56:]
    ret = [0]
    for i in range(0, leng*56, leng*7):
        temp = dct.get(li[i:i + 7*leng:leng])
        if temp == None: return
        ret.append(temp)
    return ret

def solve():
    for password in passwords:
        tmp = bin(int(password,16)).lstrip('0b').rstrip('0')
        print(password, tmp)
        leng = 1
        while tmp:
            while len(tmp) < 56*leng: tmp = '0' + tmp
            code = possible(tmp, leng)
            if code:
                tmp = tmp[:len(tmp) - leng * 56].rstrip('0')
                res.add(tuple(code))
                leng = 0
            leng += 1
    ans = 0
    for num in res:
        tmp = 0
        for i in range(1, 9):
            tmp += num[i] + num[i] * (i & 1) * 2
        if not tmp%10: ans += sum(num)
    return ans


for T in range(int(input())):
    n, m = map(int, input().split())
    passwords, res = set(), set()
    for _ in range(n):
        tmp = input().strip().strip('0')
        if tmp: passwords.add(tmp)
    print(f'#{T+1}', solve())