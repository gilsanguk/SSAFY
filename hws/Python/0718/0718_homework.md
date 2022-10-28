### 1. Python 예약어

- False, None, True, __peg_parser__, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda

### 2. 실수 비교

```python
num1 = 0.1*3
num2 = 0.3
import math
print(math.isclose(num1,num2))
```

### 3. 이스케이프 시퀀스

(1)\n, (2)\t, (3)\\

### 4. String Interpolation

```python
name='철수'
print(f'안녕, {name}야')
```

### 5. 형 변환

```python
str(1)
int('30')
int(5)
bool('50')
int('3.5') # Error
```

### 6. 네모 출력

```python
n = int(input())
m=int(input())
print(('*'*n+'\n')*m)
```

### 7. 이스케이프 시퀀스 응용

```python
print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```

### 8. 근의 공식

```python
(-b+((b**2)-(4*a*c))**(1/2))/2*a
(-b-((b**2)-(4*a*c))**(1/2))/2*a
```

