<p style="font-size: 33px; font-weight: 700; margin-bottom: 3rem">함수(function) I</p>

함수(function) I

- 함수의 정의
- 함수의 Output
- 함수의 Input

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181746-2a1d9400-a665-11e9-804e-e92940d4fc82.png", alt="func.png">
</center>

## 함수(Function)
- 특정 명령을 수행하는 함수 묶음을 말합니다.


```python
def multiply(x, y, z):
    return x * y * z


multiply(5, 6, 3)
```




    90



## 모듈 (Module)
- 함수 / 클래스의 모음 또는 하나의 프로그램을 구성하는 단위를 의미합니다.

## 패키지 (Package)
- 프로그램과 모듈의 묶음을 의미합니다.
    - 프로그램 : 실행하기 위한 것
    - 모듈 : 다른 프로그램에서 불러와 사용하기 위한 것
![module](https://user-images.githubusercontent.com/45934087/148158664-3798bd68-a9fa-4c21-be01-874bada7c11c.png)


## 라이브러리 (Library)
- 패키지의 모음을 의미합니다.
![Library](https://user-images.githubusercontent.com/45934087/148158810-466f417d-f950-4ac0-abcb-321e0577d043.png)

# 들어가기전에 
다음의 코드를 봅시다. 무엇을 하는 코드일까요?


```python
values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
total = 0
cnt = 0

for value in values:
    total += value
    cnt += 1
mean = total / cnt

total_var = 0
for value in values:
    total_var += (value - mean) ** 2
sum_var = total_var / cnt

target = sum_var
count = 0 
while True : 
    count += 1 
    root = 0.5 * (target + (sum_var / target))  
    if (abs(root - target) < 0.0000000000000001): 
        break 
    target = root

std_dev = target
print(std_dev)
```

    14.499760534421096
    

이해하기 쉬운가요? 그리고 만약 다른 곳에서 동일한 작업을 다시해야할 경우 어떻게 해야 할까요?


```python
import math
values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
cnt = len(values)
mean = sum(values) / cnt
sum_var = sum(pow(value - mean, 2) for value in values) / cnt
std_dev = math.sqrt(sum_var)
print(std_dev)
```

    14.499760534421096
    

한줄로도 가능할까요?


```python
import statistics
values = [100, 75, 85, 90, 65, 95, 90, 60, 85, 50, 90, 80]
statistics.pstdev(values)
```




    14.499760534421096



# 함수(function)

> 특정한 기능(function)을 하는 코드의 묶음

## 함수를 쓰는 이유

- 가독성
- 재사용성
- 유지보수

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181741-2984fd80-a665-11e9-93b8-578c56689d0e.png", alt="programming principle">
</center>

## 함수의 선언과 호출

* 함수의 선언은 `def` 키워드를 활용합니다.


* `들여쓰기(4spaces)`로 함수의 body(코드 블록)를 작성합니다.
    * Docstring은 함수 body 앞에 선택적으로 작성 가능합니다.


* 함수는 `매개변수(parameter)`를 넘겨줄 수도 있습니다.


* 함수는 동작후에 `return`을 통해 결과값을 반환합니다.
    * 반드시 하나의 값을 반환합니다 (`return` 값이 없으면, `None`을 반환)


* 함수는 호출은 `함수명()`으로 합니다. 
    * 예) `func()` / `func(val1, val2)`

---

#### 활용법

```python
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value
```

### [연습] 세제곱 함수 
> 입력 받은 수를 세제곱하여 반환(return)하는 함수 `cube()`을 작성해보세요.

---

**[입력 예시]**

```py
cube(2)
```

**[출력 예시]**

8

위 문제를 참고하여 아래에 cube라는 이름의 함수를 작성하고 실행해봅시다.

함수의 기본 선언을 연습하는 예제입니다
- 거듭 제곱 연산자 : `**` (별표 2개)
- ex) 10의 2승 => `10 ** 2`

```python
def 함수이름(매개변수):
     거듭 제곱 연산자를 활용하여 입력 받은 매개변수를 세제곱하여 변수에 할당하는 코드 작성합니다.
     위에서 할당한 변수를 반환합니다.
```


```python
#
def cube(num):
    return num**3
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(cube(2))
print(cube(100))
```

    8
    1000000
    

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e.png", alt="function descrpition">
</center>


```python
# 우리가 활용하는 print문도 파이썬에 지정된 함수입니다. 
# 아래에서 'hi'는 argument이고 출력을 하게 됩니다.
print('hi')
```

    hi
    

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181739-2984fd80-a665-11e9-991b-f2f058397a69.png", alt="built_in">
</center>

[파이썬 문서](https://docs.python.org/ko/3/library/functions.html)


```python
# 아래 작성된 함수를 실행하여 내장함수 목록을 직접 확인해봅시다.
dir(__builtins__)
```




    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BlockingIOError',
     'BrokenPipeError',
     'BufferError',
     'BytesWarning',
     'ChildProcessError',
     'ConnectionAbortedError',
     'ConnectionError',
     'ConnectionRefusedError',
     'ConnectionResetError',
     'DeprecationWarning',
     'EOFError',
     'Ellipsis',
     'EnvironmentError',
     'Exception',
     'False',
     'FileExistsError',
     'FileNotFoundError',
     'FloatingPointError',
     'FutureWarning',
     'GeneratorExit',
     'IOError',
     'ImportError',
     'ImportWarning',
     'IndentationError',
     'IndexError',
     'InterruptedError',
     'IsADirectoryError',
     'KeyError',
     'KeyboardInterrupt',
     'LookupError',
     'MemoryError',
     'ModuleNotFoundError',
     'NameError',
     'None',
     'NotADirectoryError',
     'NotImplemented',
     'NotImplementedError',
     'OSError',
     'OverflowError',
     'PendingDeprecationWarning',
     'PermissionError',
     'ProcessLookupError',
     'RecursionError',
     'ReferenceError',
     'ResourceWarning',
     'RuntimeError',
     'RuntimeWarning',
     'StopAsyncIteration',
     'StopIteration',
     'SyntaxError',
     'SyntaxWarning',
     'SystemError',
     'SystemExit',
     'TabError',
     'TimeoutError',
     'True',
     'TypeError',
     'UnboundLocalError',
     'UnicodeDecodeError',
     'UnicodeEncodeError',
     'UnicodeError',
     'UnicodeTranslateError',
     'UnicodeWarning',
     'UserWarning',
     'ValueError',
     'Warning',
     'WindowsError',
     'ZeroDivisionError',
     '__IPYTHON__',
     '__build_class__',
     '__debug__',
     '__doc__',
     '__import__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'abs',
     'all',
     'any',
     'ascii',
     'bin',
     'bool',
     'breakpoint',
     'bytearray',
     'bytes',
     'callable',
     'chr',
     'classmethod',
     'compile',
     'complex',
     'copyright',
     'credits',
     'delattr',
     'dict',
     'dir',
     'display',
     'divmod',
     'enumerate',
     'eval',
     'exec',
     'execfile',
     'filter',
     'float',
     'format',
     'frozenset',
     'get_ipython',
     'getattr',
     'globals',
     'hasattr',
     'hash',
     'help',
     'hex',
     'id',
     'input',
     'int',
     'isinstance',
     'issubclass',
     'iter',
     'len',
     'license',
     'list',
     'locals',
     'map',
     'max',
     'memoryview',
     'min',
     'next',
     'object',
     'oct',
     'open',
     'ord',
     'pow',
     'print',
     'property',
     'range',
     'repr',
     'reversed',
     'round',
     'runfile',
     'set',
     'setattr',
     'slice',
     'sorted',
     'staticmethod',
     'str',
     'sum',
     'super',
     'tuple',
     'type',
     'vars',
     'zip']




```python
# 제공된 링크로 이동해서 편하게 써왔던 random.sample() 함수의 내부도 직접 확인해봅시다.
```

https://github.com/python/cpython/blob/master/Lib/random.py#L385

### [연습] 함수 만들기

> 아래의 코드와 동일한 `my_max` 함수를 만들어주세요.
>
> 정수를 두개 받아서, 큰 값을 반환합니다. 

```python
my_max(1, 5)
```
---
```
출력 예시)
5
```



```python
# 먼저 내장함수 max()를 확인해봅시다.
# 내장함수 max에 숫자 1과 5를 전달인자로 작성하고 실행합니다.
max(1, 5)
```




    5



내장함수와 비슷하게 동작하는 my_max 함수를 직접 작성해봅시다. 

(2개의 변수가 입력된다는 점에 주의합니다.)

```python
def 함수이름(숫자a, 숫자b):
    if문을 활용하여 입력 받은 두 숫자 중 큰 수를 리턴합니다.
```


```python
#
def my_max(a, b):
    if a>b:
        return a
    else:
        return b
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
my_max(1, 5)
```




    5



### 함수의 선언과 호출 살펴보기


```python
# 아래의 코드의 결과는 무엇일까요? 실행하기 전에 예측해봅시다.

num1 = 0
num2 = 1

def func1(a, b):
    return a + b
    
def func2(a, b):
    return a - b
    
def func3(a, b):
    return func1(a, 5) + func2(5, b)
    
result = func3(num1, num2)
print(result)
```

    9
    

* [Python tutor](http://pythontutor.com/visualize.html#code=num1%20%3D%200%0Anum2%20%3D%201%0A%0Adef%20func1%28a,%20b%29%3A%0A%20%20%20%20return%20a%20%2B%20b%0A%20%20%20%20%0Adef%20func2%28a,%20b%29%3A%0A%20%20%20%20return%20a%20-%20b%0A%20%20%20%20%0Adef%20func3%28a,%20b%29%3A%0A%20%20%20%20return%20func1%28a,%205%29%20%2B%20func2%285,%20b%29%0A%20%20%20%20%0Aresult%20%3D%20func3%28num1,%20num2%29%0Aprint%28result%29&cumulative=false&curInstr=10&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)를 통해 실행 순서를 직접 확인하세요.

* 함수는 호출되면 계산을 수행하고, 값을 반환하며 종료됩니다.

# 함수의 Output

## 함수의 `return`

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류(~~의 객체~~)라도 상관없습니다. 
 
단, **오직 한 개의 객체**만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

### [실습] 사각형의 넓이를 구하는 함수
> 너비와 높이를 입력 받아 사각형의 넓이와 둘레를 반환(return)하는 함수 `rectangle()`을 작성해보세요.

---

**[입력 예시]**

```py
rectangle(30, 20)
```

**[출력 예시]**

(600, 100)

rectangle 이라는 이름의 함수를 작성하고 호출해봅시다.

(작성하려는 함수가 어떤 목적을 갖고 있는지 고민하면서 작성합니다.)

- 이번 함수는 **넓이와 둘레** 2가지 값을 한번에 반환하는 함수입니다.
- 넓이 : 너비 * 높이
- 둘레 : 2 * (너비 + 높이)

```python
def 함수이름(너비, 높이):
    넓이와 둘레를 구하고 저장하는 코드를 작성합니다.
    저장된 넓이, 둘레를 함께 반환합니다.
```


```python
#
def rectangle(width, height):
    return (width*height, 2*(width+height))
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(rectangle(30, 20))
print(rectangle(50, 70))
```

    (600, 100)
    (3500, 240)
    

### [연습] 함수를 정의하고 값을 반환해봅시다.
 
> 리스트 두개를 받아 각각 더한 결과를 비교하여 값이 큰 리스트를 반환하는 함수를 만들어주세요.

```python
my_list_max([10, 3], [5, 9])
```
---
```
예시 출력)
[5, 9]
```


my_list_max 라는 이름의 함수를 작성하고 호출해봅시다.

(입력되는 값이 **리스트**임에 주의합니다.)

1. 입력되는 리스트a의 요소들의 합을 구하고,
1. 입력되는 리스트b의 요소들의 합을 구하고,
1. 계산한 두 값을 비교합니다.

```python
def 함수이름(리스트a, 리스트b):
    if문을 활용하여 각 리스트 요소의 합을 비교하고 값이 큰 리스트를 반환하는 코드 작성
```


```python
#
def my_list_max(a, b):
    if sum(a)>sum(b):
        return a
    else:
        return b
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(my_list_max([10, 3], [5, 9]))
```

    [5, 9]
    

# 함수의 입력(Input)

## 매개변수(parameter) & 전달인자(argument)

### 매개변수(parameter)

```python
def func(x):
      return x + 2
```

* `x` 는 매개변수(parameter)입니다.
* 입력을 받아 함수 내부에서 활용할 `변수`입니다.
* **함수를 정의하는 부분에서 확인할 수 있습니다.**


### 전달인자(argument)

```python
func(2)
```

* `2` 는 전달인자(argument)입니다.
* 실제로 전달되는 `값`입니다.
* **함수를 호출하는 부분에서 볼 수 있습니다.**
    
> 주로 혼용해서 사용하지만 엄밀하게 따지면 둘은 다르게 구분되어 사용됩니다. 개념적 구분보다 함수가 작동하는 원리를 이해하는게 더 중요합니다.

## 함수의 인자

함수는 입력값(input)으로 `인자(argument)`를 넘겨줄 수 있습니다.

### 위치 인자 (Positional Arguments)

기본적으로 인자는 위치에 따라 함수 내에 전달됩니다. 

### [연습] 원기둥의 부피

> 원기둥의 반지름(r)과 높이(h)를 받아서 부피를 return하는 함수 `cylinder()`를 작성하세요.
>
> *원기둥 부피 = 3.14 * 반지름 * 반지름 * 높이*

`cylinder` 라는 이름의 함수를 작성하고 호출해봅시다.

(함수 선언의 반복 연습입니다.)
 
- 원기둥 부피 : 원의 넓이 * 높이 
- 3.14 * (반지름의 제곱) * 높이
- 3.14 * 반지름 * 반지름 * 높이

```python
def 함수이름(반지름, 높이):
    원기둥 부피를 계산하여 반환합니다.
```


```python
#
def cylinder(r, h):
    return (r**2*3.14*h)
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(cylinder(5, 2))
print(cylinder(2, 5)) # 순서를 바꾸면 다른 값이 나옵니다.
```

    157.0
    62.800000000000004
    

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181743-2a1d9400-a665-11e9-8df2-e4856caf16e4.png", alt="function example 02">
</center>

### 기본 인자 값 (Default Argument Values)

**함수를 정의할 때,** 매개변수에 기본값을 지정하여 함수 호출 시 정의된 매개변수보다 적은 인자로 함수를 호출할 수 있습니다. 

---

**활용법**
```python
def func(p1=v1):
    return p1
```

### [연습] 기본 인자 값 활용

> 이름을 받아서 다음과 같이 인사하는 함수 `greeting()`을 작성하세요. 이름이 길동이면, "길동, 안녕?" 이름이 없으면 "익명, 안녕?" 으로 출력하세요.

greeting 이라는 이름의 함수를 작성하고 호출해봅시다.

(매개변수의 기본인자에 대한 연습입니다.)

**입력된 값이 없을 때** 라는 상황과 **그 상황에서 사용할 값**이라는 점에 주의합니다.

- 입력된 값이 길동 => '길동, 안녕?'
- 값이 없는 경우 => '익명, 안녕?'

```python
def 함수이름(이름='입력이 없으면 사용할 값'):
    매개변수를 활용하여 문장(문자열)을 완성하여 리턴합니다.
```


```python
#
def greeting(name='익명'):
    return name
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(greeting())
print(greeting('철수'))
```

    익명
    철수
    

* 기본 인자 값이 설정되어 있더라도 기존의 함수와 동일하게 호출 가능합니다.


<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181744-2a1d9400-a665-11e9-9095-6924ca11122e.png">
</center>

* 호출시 인자가 없으면 기본 인자 값이 활용됩니다.


<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181745-2a1d9400-a665-11e9-95ef-e50e463e1583.png", alt="function example 03">
</center>

**\*주의\* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없습니다.**


```python
# 다음 코드를 바로 실행해서 오류를 확인해봅시다.
def greeting(name='peter', age):
    return f'{name}은 {age}살입니다.'
```


      Input In [38]
        def greeting(name='peter', age):
                                      ^
    SyntaxError: non-default argument follows default argument
    


오류가 발생하지 않도록 다음 셀에 직접 수정하고 실행해봅시다.

(오류가 발생한 원인을 친절히 안내해준다는 것을 다시 한번 확인 할 수 있습니다.)

- Error 문장을 다시 읽어보면, `non-default argument follows default argument`
- 즉, 기본 인자는 기본 인자가 아닌 친구들 다음에 위치해야한다고 알려주고 있습니다. 수정해봅시다.

```python
def 함수이름(기본인자가 아닌 친구들, 기본인자):
    매개변수를 활용하여 문장(문자열)을 완성해서 반환합니다.
```


```python
#
def greeting(age, name='peter'):
    return f'{name}은 {age}살입니다.'
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(greeting(1))
print(greeting(2, 'ssafy'))
```

    peter은 1살입니다.
    ssafy은 2살입니다.
    

### 키워드 인자 (Keyword Arguments)

**함수를 호출할 때** 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달할 수 있습니다.


```python
# 다음 코드를 실행해서 greeting 함수를 선언합니다.
def greeting(age, name):
    return f'{name}은 {age}살입니다.'
```


```python
# 아래와 같이 키워드 인자를 사용해서 함수를 호출할 수 있습니다.
```


```python
greeting(name='철수', age=24)
```




    '철수은 24살입니다.'




```python
# 위치 인자와 함께 사용할 수 있습니다.
```


```python
greeting(24, name='철수')
```




    '철수은 24살입니다.'



* **단 아래와 같이 `키워드 인자`를 활용한 다음에 `위치 인자`를 활용할 수는 없습니다.**


```python
# 다음 코드를 실행해서 오류를 직접 확인해봅시다.
greeting(age=24, '철수')
```


      Input In [45]
        greeting(age=24, '철수')
                             ^
    SyntaxError: positional argument follows keyword argument
    


## 정해지지 않은 여러 개의 인자 처리


우리가 주로 활용하는 `print()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어있습니다.
> <center>
    <img src="https://user-images.githubusercontent.com/18046097/61181751-2b4ec100-a665-11e9-9a7c-a19a8c445cfa.png", alt="print">
</center>


```python
# 지금까지 열심히 사용했던 print에는 여러 값을 넣을 수 있습니다.
```


```python
print('첫번째 문장')
print('두번째 문장', end='_')
print('세번째 문장', '네번째 문장')
print('다섯번째 문장', '마지막 문장', sep='/', end='끝!')
```

    첫번째 문장
    두번째 문장_세번째 문장 네번째 문장
    다섯번째 문장/마지막 문장끝!

### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 **함수를 정의할 때** 가변 인자 리스트`*args`를 활용합니다. 

가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다. 

---

**활용법**

```python
def func(a, b, *args):
```
> `*args` : 임의의 개수의 위치인자를 받음을 의미
> 
> 보통, 이 가변 인자 리스트는 매개변수 목록의 마지막에 옵니다.


```python
# 앞서 살펴봤던 print문에 대한 공식문서를 다시 한번 살펴봅니다.
# 바로, *obejcts를 통해 임의의 숫자의 인자를 모두 처리(가변 인자 리스트)하고 있다는 것을 알 수 있습니다.
```


```python
print('hi', '안녕', 'Guten Tag', 'gonnichiwa', sep=',')
```


```python
# 또한, args는 함수 내부에서 tuple 자료형으로 사용됩니다.
```


```python
def my_func(*args):
    return args
    
print(my_func(1, 2))
print(type(my_func(1, 2)))
```

    (1, 2)
    <class 'tuple'>
    

### [연습] 가변 인자 리스트를 사용해봅시다.

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 함수 `my_max()`를 작성하세요.
>
> max 내장 함수 사용은 금지합니다.

```python
my_max(10, 20, 30, 50)
```
---
```
예시출력)
50
```


```python
# 정해지지 않은 여러 개의 인자를 내장 함수 max에서는 어떻게 처리하는지 확인해봅시다.
```


```python
max(1, 2, 3, 4)
```




    4



이제 my_max 이름의 함수를 직접 선언해봅시다.

용어 이름은 가변 인자 리스트이지만, 기본적으로 튜플 자료형임에 주의합니다.
- `*` (별표 1개)를 매개변수에 작성해야합니다.
- 말 그대로 정해지지 않았기 때문에, 이번 예제에서는 반복문을 통해 간편하게 개별 값에 접근합니다.

```python
def 함수이름(가변 인자 리스트):
    가변 인자 리스트 중 처음 값을 기준이 되는 값으로 할당합니다.
    반복문을 통해 입력 받은 값들을 검사합니다.
    조건문으로 기준이 되는 값과 다른 요소들을 비교해서, 더 큰 값을 기준값으로 변경합니다.
    찾아낸 최대값을 반환합니다.
```     


```python
def my_max(*args):
    result = args[0]
    for i in range(len(args)):
        if result < args[i]:
            result=args[i]
    return result
```


```python
# 다음 코드를 실행해 올바른 결과가 나오는지 확인하세요.
my_max(-1, -2, -3, -4)
```




    -1



### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

정해지지 않은 키워드 인자들은 **함수를 정의할 때** 가변 키워드 인자 `**kwargs`를 활용합니다. 

가변 키워드 인자는 **`dict`** 형태로 처리가 되며, 매개변수에 `**`로 표현합니다. 

---

**활용법**

```python
def func(**kwargs):
```
> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미합니다

우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있습니다.
> <center>
    <img src="https://user-images.githubusercontent.com/18046097/61181740-2984fd80-a665-11e9-94cf-7f5ab41873b1.png", alt="dictionary">
</center>


```python
# 딕셔너리 생성 함수 예시입니다.
# 가변 키워드 인자 활용을 확인해보기 위한 예시입니다.
```


```python
hi = dict(한국어='안녕', 영어='hi')
print(hi)
```

    {'한국어': '안녕', '영어': 'hi'}
    


```python
# 식별자는 숫자만으로는 이루어질 수가 없다는 것에 주의합니다.
# 키워드인자로 넘기면 함수 안에서 식별자(변수이름)로 쓰이기 때문입니다.
```


```python
dict(1=1, 2=2)  # SyntaxError
```


      Input In [59]
        dict(1=1, 2=2)  # SyntaxError
             ^
    SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
    



```python
# Key가 숫자인 딕셔너리를 만들고 싶다면, 아래와 같이 사용해야합니다.
print(dict([(1, 1), (2, 2)]))
print(dict(((1,1), (2,2))))
```

    {1: 1, 2: 2}
    {1: 1, 2: 2}
    


```python
# 아래 셀의 코드를 실행시켜 kwargs가 딕셔너리로 처리되는 것을 확인해봅시다.
```


```python
def my_dict(**kwargs):
    return kwargs

print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
```

    {'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
    

### [실습] URL 생성기

> `my_url()` 함수를 만들어 완성된 URL을 반환하는 함수를 작성하세요.
>
>

```python
my_url(sidoname='서울', key='asdf')
```

---

```
예시 출력)
https://api.go.kr?sidoname=서울&key=asdf&
```

입력받은 가변 키워드 인자를 활용하여 'https://api.go.kr?'를 BASE_URL로 사용하는 URL을 생성해봅시다.

my_url 이라는 이름의 함수를 직접 작성해봅시다.

가변 키워드 인자(kwargs)를 사용하는 실습입니다.
- `**` (별표 2개)를 변수명 앞에 붙여서 작성하는 문법 사항에 주의합니다.
- 또한, 가변 키워드 인자는 기본적으로 딕셔너리 자료형이라는 점에 주의합니다.
- 이번에도 정해지지 않은 수의 인자가 입력되기 때문에 반복문을 활용합니다.

```python
def 함수이름(가변 키워드 인자):
    기본이 되는 url인 'https://api.go.kr?'를 미리 url 변수에 할당합니다.
    딕셔너리를 반복문으로 조회하기 위해 .items() 메서드를 활용합니다.
    해당 메서드로 얻어 낼수 있는 key값과, value값을 활용하여 url을 완성합니다.
    완성된 url을 반환합니다.
```


```python
def my_url(**kwargs):
    url = 'https://api.go.kr?'
    for i, j in kwargs.items():
        url += f'{i}={j}&'
    return url
```


```python
# 다음 코드를 실행하여 결과를 확인해봅시다.
print(my_url(sidoname='서울', key='asdf'))
```

    https://api.go.kr?sidoname=서울&key=asdf&
    

<p style="font-size: 33px; font-weight: 700; margin-bottom: 3rem">함수(function) II</p>

- 함수와 스코프
- 재귀 함수
- 함수 응용

# 함수와 스코프(scope)

함수는 코드 내부에 스코프(scope)를 생성합니다. 함수로 생성된 공간은 `지역 스코프(local scope)`라고 불리며, 그 외의 공간인 `전역 스코프(global scope)`와 구분됩니다.

* **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
* **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간


* **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
* **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수



```python
# 전역 스코프와 지역 스코프를 알아봅시다.
# 먼저, 지역스코프에서 전역스코프의 변수는 참조할 수 있습니다.
```


```python
# 전역 스코프(global scope)
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    print(a)
    print(b)

func(a)
```

    10
    10
    


```python
# 전역 스코프에서는 지역 스코프의 변수를 참조할 수 없습니다.
# func 함수 바깥에서 함수 안의 지역 변수 c를 출력하고 오류를 확인해봅시다.
```


```python
# 전역 스코프(global scope)
a = 10 # 전역 변수(global)

def func(b):
    # 지역 스코프(local scope)
    c = 20 # 지역 변수(local variable)
    print(a)
    print(b)

func(a)

# 변수 c는 접근 불가합니다.
print(c)
```

    10
    10
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [79], in <cell line: 13>()
         10 func(a)
         12 # 변수 c는 접근 불가합니다.
    ---> 13 print(c)
    

    NameError: name 'c' is not defined



```python
# 전역 스코프와 지역 스코프에 같은 이름의 변수를 만들면 어떻게 되는지 확인해봅시다.
```


```python
a = 10 # 전역 변수(global)

def func(b):
    a = 30 # 지역 변수(local variable)
    print(a)
    
func(a)
print(a)
```

    30
    10
    

### 변수의 수명주기(lifecycle)

변수의 이름은 각자의 `수명주기(lifecycle)`가 있습니다.

* **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지


* **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날 때 까지 유지


* **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)

## 이름 검색(resolution) 규칙

파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있습니다.

아래와 같은 순서로 이름을 찾아나가며, `LEGB Rule` 이라고 부릅니다.

* `L`ocal scope: 함수


* `E`nclosed scope: 특정 함수의 상위 함수 


* `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈


* `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성


```python
# 이것을 통해 첫시간에 내장함수의 식별자를 사용할 수 없었던 예제에서 오류가 생기는 이유를 확인할 수 있습니다.
# Built-in scope와 Global scope를 알아봅시다.
```


```python
print = 'ssafy'
print(3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [81], in <cell line: 2>()
          1 print = 'ssafy'
    ----> 2 print(3)
    

    TypeError: 'str' object is not callable



```python
# print라는 이름(식별자)이 'ssafy'라는 문자열 정보를 저장한 하나의 변수가 되었습니다.
# 내장 함수인 print 함수를 다시 사용할 수 있도록 print라는 이름의 변수를 삭제합니다.
```


```python
del print
```

## 

1. `print()` 코드가 실행되면


2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,


3. `print`라는 식별자를 Global scope에서 찾아서 `print = ssafy`를 가져오고, 


4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.


5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.


```python
# Global scope(G)와 Local scope(L)를 다시 한번 복습합니다.
```


```python
a = 1 # 전역 변수 a
def local_scope(a):
    return a # 지역 변수 a

local_scope(3)
```




    3




```python
# 앞선 내용(G & L)을 확장하여 LEGB Rule을 자세히 알아봅시다.
# 각 변수가 어느 스코프에 해당하는 변수인지 확인해보고 왜 그렇게 되는지 고민해보세요.
```


```python
a = 10
b = 20
def enclosed():
    a = 30
    def local():
        c = 40
        print(a, b, c)
    local()
    a = 50
enclosed()
```

    30 20 40
    


```python
# 전역 변수를 바꿀 수 있을까요?
```


```python
# 기본적으로 지역 스코프에서 전역 스코프의 변수를 바꿀 수는 없습니다.
# 아래 셀의 코드에서 함수 내부의 global_num은 지역 변수로 생성됩니다.
```


```python
global_num = 3
def local_scope():
    global_num = 5

local_scope()
print(global_num)
```

    3
    


```python
# 전역에 있는 변수의 값을 변경하고 싶다면,
# 아래와 같이 global 키워드를 사용하여 지역 스코프에서 전역 변수의 값을 바꿀 수 있습니다.
```


```python
global_num = 3
def local_scope():
    global global_num
    global_num = 5

local_scope()
print(global_num)
```

    5
    

* 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라집니다.
* 해당 스코프에 변수가 없는 경우 LEGB rule에 의해 이름을 검색합니다.
    * 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없습니다.
    * 값을 할당하는 경우 해당 스코프의 이름공간에 새롭게 생성되기 때문입니다.
    * **단, 함수 내에서 필요한 상위 스코프 변수는 인자로 넘겨서 활용합니다.** (클로저 제외)
* 상위 스코프에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능합니다.
    * 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생합니다.

# 재귀 함수(recursive function)

재귀 함수는 함수 내부에서 자기 자신을 호출 하는 함수를 뜻합니다.

알고리즘을 설계 및 구현에서 유용하게 활용됩니다.

## 팩토리얼 계산
> 팩토리얼은 1부터 n 까지 양의 정수를 차례대로 곱한 값이며 `!` 기호로 표기합니다. 예를 들어 3!은 3 * 2 * 1이며 결과는 6 입니다.
>
> `팩토리얼(factorial)`을 계산하는 함수 `fact(n)`를 작성하세요. 
>
> n은 1보다 큰 정수라고 가정하고, 팩토리얼을 계산한 값을 반환합니다.

$$
\displaystyle n! = \prod_{ k = 1 }^{ n }{ k }
$$

$$
\displaystyle n! = 1*2*3*...*(n-1)*n
$$

---
```
예시 출력)
120
```

### 재귀를 이용한 팩토리얼 계산

```
1! = 1
2! = 1 * 2 = 1! * 2 
3! = 1 * 2 * 3 = 2! * 3
```

재귀 함수를 이용하여 다음 셀에 팩토리얼 함수를 직접 구현해봅시다.

(점화식에 대한 고민을 통해 코드 구현을 연습합니다.)

Case(1) = `1! = 1`

Case(2) = `2! = 1 * 2` = Case(1) * 2

Case(3) = `3! = 1 * 2 * 3` = Case(2) * 3

...

Case(N) = N! = 1 * 2 * 3 * ... * N = Case(N-1) * N => N-1 단계까지의 결과 * N

이렇게 반복적인 구조 (이전 단계까지의 결과 * 현재 단계의 숫자)를 찾아내고, 이를 코드로 표현합니다.

```python
def 팩토리얼재귀(현재 단계의 숫자):
    만약, 현재 단계가 1 단계라면?
        더이상 재귀호출을 진행하지않고, 1을 반환합니다.
    그렇지 않은 경우에는 (현재 단계의 숫자 * 이전 단계의 재귀 함수의 실행 결과)를 반환합니다.
```


```python
#
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
factorial(5)
```




    120



### 반복문을 이용한 팩토리얼 계산

반복문으로 구현해봅시다.

- 목표하는 n값 만큼 반복하여 곱을 누적합니다.
 
 
```python
def 팩토리얼반복(현재 단계의 숫자):
    시작하는 숫자는 1
    while문을 활용하여, n번만큼 결과에 곱을 누적합니다.
    최종 결과를 리턴합니다.
```


```python
#
def fact(n):
    a = 1
    result = 1
    while a<=n:
        result = result*a
        a+=1
    return result
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
fact(5)
```




    120



## 반복문과 재귀함수
```python
factorial(3)
3 * factorail(2)
3 * 2 * factorial(1)
3 * 2 * 1
3 * 2
6
```

* 두 코드 모두 원리는 같습니다.


1. 반복문 코드
    - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소합니다. 
    - 마지막에 n이 1이면 더 이상 반복문을 돌지 않습니다.
  
  
2. 재귀 함수 코드
    - 재귀 함수를 호출하며, n은 1씩 감소합니다. 
    - 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않습니다.


* 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제를 풀게 됩니다.

* 재귀함수를 작성시에는 반드시, `base case`가 존재 하여야 합니다. 

* `base case`는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳을 의미합니다. 

* 재귀를 이용한 팩토리얼 계산에서의 base case는 **n이 1이 되면 함수를 호출하지 않고 정수를 반환하는 것**입니다.

* 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용됩니다.
* 코드가 더 직관적이고 이해하기 쉬운 경우가 있습니다. 
* 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있습니다.
* 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생깁니다.
* 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료됩니다. (최대 재귀 깊이)

### 최대 재귀 깊이


```python
def ssafy():
    print('Hello, ssafy!')
    ssafy()
 
ssafy()
```
---

`ssafy()`를 호출하면 아래와 같이 문자열이 계속 출력되다가 RecursionError가 발생합니다.

파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있기 때문입니다.

주피터 노트북은 커널이 종료되어 확인하기 어렵습니다.

---

```bash
Hello, world!
Hello, world!
...
Hello, world!
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)

...

      1 def hello():
      2     print('Hello, world!')
----> 3     hello()
      4 
      5 hello()

RecursionError: maximum recursion depth exceeded while calling a Python object
```

## [실습] 피보나치 수열

첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열입니다. 

(0), 1, 1, 2, 3, 5, 8

> 피보나치 수열은 다음과 같은 점화식이 있습니다. 
>
> 피보나치 값을 리턴하는 두가지 방식의 코드를 모두 작성해주세요.
>

$$
\displaystyle F_0 = 0
$$


$$
\displaystyle F_1 = 1
$$

$$
F_n=F_{n-1}+F_{n-2}\qquad(n\in\{2,3,4,\dots\})
$$

1) `fib(n)` : 재귀함수

2) `fib_loop(n)` : 반복문 활용한 함수

---
```
예시 입력)
fib(10)

예시 호출)
55
```

재귀 함수를 활용하여, fib 라는 이름의 피보나치 수열 함수를 작성하세요.

(점화식에 대한 고민을 통해 코드 구현을 연습합니다.)

Case(0) = 0

Case(1) = 1

Case(2) = Case(1) + Case(0) = 1

Case(3) = Case(2) + Case(1)

...

Case(N) = Case(N-1) + Case(N-2)

(현재 단계 = 바로 전 단계 + 바로 전전 단계)의 식을 코드로 표현합니다!

```python
def 피보나치재귀(현재단계):
    만약, 현재단계가 2단계보다 작으면
        그냥 현재 단계를 반환합니다.
    그렇지 않다면,
        전단계의 재귀함수 + 전전단계의 재귀함수 의 결과를 반환합니다.
```


```python
# 
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
```


```python
fib(10)
```




    55



반복문(for문)을 활용하여, fib_loop라는 이름의 피보나치 수열 함수를 작성하세요.

반복문으로 구현해봅시다.
- 모든 Case의 결과를 리스트에 누적하는 방식으로 계산합니다.

```python
def 피보나치반복(현재단계):
    만약, 입력된 단계가 2보다 작다면
        입력된 단계를 그대로 리턴!

    결과를 저장할 기본 리스트([0, 1])를 준비 (각각 Case(0)와 Case(1)의 결과)
    반복문을 시작(2부터 시작, N까지)
        마지막 2개의 요소들의 합을 리스트에 추가

    리스트의 마지막 값을 반환
``` 


```python
#
def fib_loop(n):
    lst = [0,1]
    for i in range(2,n+1):
        lst.append(lst[i-1]+lst[i-2])
    print(lst[-1])
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
fib_loop(10)
```

    55
    

이번에는 리스트를 사용 하지 않고 반복문(for문)을 활용하여 fib_loop2()을 작성하세요.

- 반드시 리스트로 모든 값을 저장할 필요가 있을까요?
- 실제로 매 반복문 마다 필요한 값은 (마지막 2개의 요소)였습니다.
- 그렇기 때문에 변수 2개에 값을 변경 & 덮어쓰기 하면서 로직을 구성할 수 있습니다!

```python
def 피보나치반복(현재단계):
    만약, 입력된 단계가 2보다 작다면
        입력된 단계를 그대로 리턴!

    결과를 저장할 변수를 2개 준비 (각각 Case(0)단계와 Case(1)단계의 결과를 의미)
    반복문을 시작(0부터 N-2까지)
        전 단계의 값과 전전 단계의 값의 합을 전 단계에 덮어쓰기하면서, 동시에 원래가지고 있던 전 단계 값을 전전 단계에 저장

    마지막 결과 값을 반환!
```


```python
#
def fib_loop_2(n):
    case_1 = 0
    case_2 = 1
    tem = 0
    for i in range(n-1):
        tem = case_1
        case_1 = case_2
        case_2 = tem+case_2
    return case_2
        
```


```python
#
fib_loop_2(10)
```




    55




```python
# 반복문(while 문)을 이용한 코드 fib_while()을 작성하세요.
# 알고리즘을 구현하는 코드는 여러가지 방식이 있을 수 있습니다.
```

## 반복문과 재귀 함수의 차이

* 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용합니다.
* 재귀 호출은 `변수 사용` 을 줄여줄 수 있습니다.


```python
# 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래걸립니다.
# fib() 함수에 10 이상의 값을 넣어보고 실행한 뒤 연산 시간을 확인해봅시다.
```


```python
import time

t0 = time.time()
fib(50)
t1 = time.time()

total = t1 - t0
print(total)
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Input In [8], in <cell line: 4>()
          1 import time
          3 t0 = time.time()
    ----> 4 fib(50)
          5 t1 = time.time()
          7 total = t1 - t0
    

    Input In [1], in fib(n)
          4     return n
          5 else:
    ----> 6     return fib(n-1) + fib(n-2)
    

    Input In [1], in fib(n)
          4     return n
          5 else:
    ----> 6     return fib(n-1) + fib(n-2)
    

        [... skipping similar frames: fib at line 6 (33 times)]
    

    Input In [1], in fib(n)
          4     return n
          5 else:
    ----> 6     return fib(n-1) + fib(n-2)
    

    KeyboardInterrupt: 



```python
# 반복문은 재귀로 구현된 함수보다 연산 속도가 빠른 편입니다.
# fib_loop() 함수에 10 이상의 값을 넣어보고 실행한 뒤 연산 시간을 확인해봅시다.
# 그리고 100배 더 큰 1000 이상의 값도 넣어보고 실행한 뒤 연산 시간을 확인해봅시다.
```


```python
import time

t0 = time.time()
fib_loop(1000)
t1 = time.time()

total = t1 - t0
print(total)
```

    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    0.0
    

## 함수 응용

## `map(function, iterable)`

* 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다. 


* return은 `map_object` 형태이다.


```python
numbers = [1, 2, 3]

# 위의 변수 numbers를 문자열 '123'으로 만드세요. (join 메서드 활용)
```


```python
# List comprehension 활용
```


```python
new_numbers = [ str(i) for i in numbers]
''.join(new_numbers)
```




    '123'




```python
print(new_numbers)
```

    ['1', '2', '3']
    


```python
# map() 활용
```


```python
new_numbers = list(map(str,numbers))
new_numbers=str(''.join(new_numbers))
```


```python
print(new_numbers)
```

    123
    

`map()` 함수는 입력값을 처리할 때 자주 활용합니다.


```python
numbers = ['1', '2', '3']

# 위의 변수 numbers를 정수로 구성된 리스트 [1, 2, 3]으로 만드세요.
```


```python
# List comprehension 활용
```


```python
new_numbers = [ int(i) for i in numbers]
```


```python
print(new_numbers)
```

    [1, 2, 3]
    


```python
# map() 활용
```


```python
new_numbers =list(map(int,numbers))
```


```python
print(new_numbers)
```

    [1, 2, 3]
    

첫번째 인자 function은 사용자 정의 함수도 가능합니다.


```python
# 세제곱의 결과를 나타내는 함수가 있습니다.
def cube(n):
    return n ** 3
```


```python
# 세제곱 함수를 각각의 요소에 적용한 결과값을 구해봅시다.
numbers = [1, 2, 3]
```


```python
new_numbers = list(map(cube, numbers))
```


```python
print(new_numbers)
```

    [1, 8, 27]
    

### [연습] 코딩 테스트의 기본

> 두 정수를 입력 받아 더한 값을 출력하세요.

**[입력 예시]**

3 5

---

**[출력 예시]**

8


```python
# 아래에 코드를 작성하세요.
a, b = map(int,input().split())
print(a+b)
```

    3 5
    8
    

## `filter(function, iterable)`

* iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환합니다.


* `filter object` 를 반환합니다.


```python
# 특정 list에서 홀수만을 걸러내는 코드를 작성해봅시다.
```


```python
# 홀수를 판별하는 함수가 있습니다.
def odd(n):
    return n % 2
```


```python
# 홀수인 요소만 뽑아 new_numbers에 저장합니다.
numbers = [1, 2, 3]
```


```python
new_numbers = list(filter(odd, numbers))
```


```python
print(new_numbers)
```

    [1, 3]
    


```python
# 다음의 list comprehension과 동일합니다.
```


```python
new_numbers = [i for i in numbers if i%2]
print(new_numbers)
```

    [1, 3]
    

## `zip(*iterables)` 

* 복수의 iterable 객체를 모아(`zip()`)줍니다.


* 결과는 튜플의 모음으로 구성된 `zip object` 를 반환합니다.


```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
```


```python
# zip() 활용하여 짝을 맞추어 본다.
```


```python
pair = list(zip(girls, boys))
```


```python
print(pair)
```

    [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
    

## lambda 함수

* 표현식을 계산한 결과 값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불립니다.

* return 문을 가질 수 없고, 간단한 조건문 외의 구성이 어렵습니다.

* 함수를 정의해서 사용하는 것보다 간결하게 사용 가능합니다.

```python

def triangle_area(b, h):
    return 0.5 * b * h

lambda b, h: 0.5 * b * h
```


```python
# 아래와 같이 간단한 함수를 정의해서 사용하는 것이 아니라 간결하게 사용 가능합니다.
list(map(lambda n: n%2, [1, 2, 3]))
```




    [1, 0, 1]


