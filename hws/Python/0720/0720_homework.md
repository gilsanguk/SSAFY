### 1. Built-in 함수

- Print(), dict(), list(), float(), int(), bool(), len() .... 

### 2. 홀수만 담기

```python
list(range(1,51,2))
```

### 3. 반복문으로 네모 출력

```python
m = int(input())
n = int(input())
k = n
while m!=0:
    while n!=0:
        print('*', end='')
        n -= 1
    n = k
    print()
    m -= 1
```

### 4. 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp>=37.5 else print('입실 가능')
```

### 5. 정중앙 문자

```python
def get_middle_char(a):
    if len(a)%2 == 1:
        print(str(a[len(a)//2]))
    else:
        print(str(a[len(a)//2-1])+str(a[len(a)//2]))
```

