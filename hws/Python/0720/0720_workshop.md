### 1. 세로로 출력하기

```python
num = int(input())
for i in range(1,num+1):
    print(i)
```

### 2. 가로로 출력하기

```python
num = int(input())
for i in range(1,num+1):
    print(i, end=' ')
```

### 3. 거꾸로 세로로 출력하기

```python
num = int(input())
for i in range(num,-1,-1):
    print(i)
```

### 4. 거꾸로 출력해 보아요

```python
num = int(input())
for i in range(num,-1,-1):
    print(i, end=' ')
```

### 5. N줄 덧셈

```python
result = 0
num = int(input())
for i in range(num+1):
    result += i
print(result)
```

### 6. 삼각형 출력하기

```python
N = int(input())
count = 0
for i in range(N):
    count+=1
    for j in range(N-count):
        print(end=' ')
    for j in range(count):
        print('*', end='')
    print()
```

### 7. 중간값 찾기

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
     ]
numbers.sort()
mid_num = numbers[int(len(numbers)/2)]
print (mid_num)
```

