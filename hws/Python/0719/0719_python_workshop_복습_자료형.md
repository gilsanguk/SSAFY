<p style="font-size: 33px; font-weight: 700; margin-bottom: 3rem">Python 기초 I</p>

# 개요

본 강의 자료는 [Python 공식 Tutorial](https://docs.python.org/3/tutorial/index.html)에 근거하여 만들어졌으며, Python 3.9 이상 버전에 해당하는 내용을 담고 있습니다.

또한, 파이썬에서 제공하는 스타일 가이드인 [`PEP-8`](https://www.python.org/dev/peps/pep-0008/) 내용을 반영하였습니다. 

파이썬을 활용하는 다양한 IT기업들은 대내외적으로 본인들의 스타일 가이드를 제공하고 있습니다. 

* [구글 스타일 가이드](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [Tensorflow 스타일 가이드](https://www.tensorflow.org/community/contribute/code_style?hl=ko)



# 기초 문법(Syntax)
## 들여쓰기(Indentation)

코드 블록을 구분할 때, 중괄호 ({,}) 대신 <들여쓰기 (identation)>를 사용합니다.

들여쓰기를 할 때는 4칸(space키 4번) 혹은 1탭 (Tab키 1번)을 입력합니다.
- 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용합니다.
- 원칙적으로는 공백 (빈칸, space) 사용을 권장합니다. * PEP8 권장사항


```python
# 일반적인 코드 작성 스타일
```


```python
print('hello')
print('world')

a = 'apple'

if True:
    print(True)
else:
    print(False)

b = 'banana'
```

## 변수(Variable)

### 변수 
컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름을 의미합니다.
- 객체(object) : 숫자, 문자, 클래스 등 **값을 가지고 있는 모든 것**을 말합니다.
    - 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있습니다.
- 동일 변수에 다른 객체를 언제든 할당할 수 있습니다.
    - 즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수' 라고 부릅니다.

<center><img src="https://user-images.githubusercontent.com/18046097/61179855-0c8d0200-a646-11e9-9e9e-2c6df0504296.png", alt="variable"/></center>


<center><img src="https://user-images.githubusercontent.com/18046097/61179857-13b41000-a646-11e9-9a88-8487df4eaf52.png", alt="box"/></center>

### 할당 연산자(Assignment Operator): `=`

* 변수는 `=`을 통해 할당(assignment) 됩니다. 

* 해당 데이터 타입을 확인하기 위해서는 `type()`을 활용합니다.

* 해당 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용합니다.


```python
# 변수 x에 임의의 문자열을 할당해봅시다.
```


```python
# type(x)를 실행하여 변수 x에 할당된 값의 데이터 타입을 확인해 봅시다.
```


```python
x = 'ssafy'
print(type(x))
```

    <class 'str'>
    


```python
# id(x)를 실행하여 변수 x의 고유 메모리 주소를 확인해봅시다.
```


```python
print(id(x))
```

    1409808829104
    

### 변수 연산


```python
# i, j, s 변수에 각각 5, 3, '파이썬'을 할당해봅시다.
```


```python
i = 5
j = 3
s = '파이썬'
```


```python
# 변수 i와 j를 더해봅시다.
```


```python
print(i + j)
```

    8
    


```python
# 변수 i에 i - j를 할당해봅시다.
```


```python
i = (i - j)
```


```python
# 변수 j에 -2를 할당하고 i * j를 실행해봅시다.
```


```python
j = -2
print(i * j)
```

    -4
    


```python
# i * j / 3 을 실행하여 결과를 확인해봅시다.
```


```python
print(i * j / 3)
```

    -1.3333333333333333
    


```python
# 문자열 '안녕'과 변수 s를 더해봅시다.
```


```python
print('안녕'+s)
```

    안녕파이썬
    


```python
# 변수 s에 s * 3을 할당하고 결과를 확인해봅시다.
```


```python
s = s * 3
print(s)
```

    파이썬파이썬파이썬
    


```python
# 변수 s에 문자열 'Python'을 할당하고
# s + ' is fun'을 실행하여 결과를 확인해봅시다.
```


```python
s = 'Python'
print(s + ' is fun')
```

    Python is fun
    

### 변수 할당
* 같은 값을 동시에 할당할 수 있습니다.


```python
# 같은 값을 x와 y에 동시에 할당해봅시다.
# 그리고 print를 이용하여 x, y 값을 확인해봅시다.
```


```python
x = y = 1
print(x, y)
```

    1 1
    

* 다른 값을 동시에 할당 가능합니다.


```python
# 두 개의 변수 x, y에 값 1, 2를 동시에 할당해봅시다.
# 그리고 print를 이용하여 x, y 값을 확인해봅시다.
```


```python
x, y = 1, 2
print(x, y)
```

    1 2
    


```python
# 두 개의 변수 x, y에 값 1을 할당해봅시다.
# 두 개의 변수에 하나의 값을 할당했을 때의 오류를 확인해봅시다.
```


```python
x, y = 1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [18], in <cell line: 1>()
    ----> 1 x, y = 1
    

    TypeError: cannot unpack non-iterable int object



```python
# 두 개의 변수 x, y에 값 1, 2, 3을 동시에 할당해봅시다.
# 두 개의 변수에 세 개의 값을 할당했을 때의 오류를 확인해봅시다.
```


```python
x, y = 1, 2, 3
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [19], in <cell line: 1>()
    ----> 1 x, y = 1, 2, 3
    

    ValueError: too many values to unpack (expected 2)


### 실습 문제
- x = 10, y = 20 일 때, 각각 값을 바꿔서 저장하는 코드를 작성하세요.


```python
x, y = 10, 20
```


```python
# 변수 x와 y의 값을 바꿔봅시다.
# 그리고 결과를 print를 이용해 확인해봅시다.
```


```python
# 방법1 : 임시 변수 활용
```


```python
tem = x
x = y
y = tem
print(x,y)
```

    20 10
    


```python
# 방법 2 : Pythonic
```


```python
x, y = y, x
print(x,y)
```

    20 10
    

### 식별자(Identifiers)

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)입니다. 

* 식별자의 이름은 영문 알파벳(대문자와 소문자), 언더스코어(_), 숫자로 구성됩니다.
* 첫 글자에 숫자가 올 수 없습니다.
* 길이에 제한이 없습니다.
* 대/소문자(case)를 구별합니다.
* 아래의 키워드는 사용할 수 없습니다. [파이썬 문서](https://docs.python.org/ko/3/reference/lexical_analysis.html#keywords)

```
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```


```python
# 키워드들을 직접 확인해봅시다.
# import 구문을 사용하여 keyword를 불러옵니다.
# print를 이용하여 파이썬이 가지고 있는 키워드 / 예약어를 출력해봅시다.
# import 구문에 대한 자세한 내용은 모듈 챕터에서 학습하겠습니다.
```


```python
import keyword
print(keyword.kwlist)
```

    ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    

*  내장함수나 모듈 등의 이름으로도 만들면 안됩니다.
- 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않게됩니다.


```python
# 내장함수의 이름을 사용하면 어떤일이 일어나는지 확인해봅시다.
```


```python
# print는 값을 출력해주는 내장함수(Built-in function)입니다.
# print(5)를 실행하여 결과를 확인해봅시다.
print(5)
```

    5
    


```python
# 변수 print에 문자열 'hi'를 할당합니다. 
# 그리고 print() 를 사용하였을때 발생하는 오류를 확인해봅시다.
# print는 'hi'라는 값을 가지는 변수로 할당되었기 때문에 이전의 출력 기능을 수행하지 못합니다.
```


```python
print = 'hi'
print(5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [29], in <cell line: 2>()
          1 print = 'hi'
    ----> 2 print(5)
    

    TypeError: 'str' object is not callable



```python
# 뒤에서 진행될 코드에 영향이 갈 수 있기 때문에 방금 생성한 print 변수를 삭제합니다.
# 아래와 같이 del 연산자를 활용합니다.
# del print
# 사용자가 지정한 변수 print는 삭제되고, 기존의 화면출력 기능을 가지는 print가 동작합니다.
# 자세한 내용은 namespace 파트에서 확인해봅시다.
```


```python
del print
```

## 사용자 입력(input)

### input([prompt])
* 사용자로부터 값을 즉시 입력 받을 수 있는 파이썬 내장함수입니다.
* 대괄호([]) 안에 문자열을 입력하면 해당 문자열을 출력할 수 있습니다.
    - 단, 대괄호는 생략합니다.
    ```python
    # ex)
    input('값을 입력해 주세요. : ')
    ```


```python
# input()을 사용해 봅시다.
# data 변수에 input()의 반환값을 할당합니다.
# print 함수를 이용하여 data 변수에 담긴 값을 출력해 봅시다.
```


```python
data = input()
print(data)
```

    1234
    1234
    


```python
# 문자열 '이름을 입력 해 주세요. : '를 출력하는 input 함수를 변수 name에 할당합니다.
# print 함수를 이용하여 name 변수에 담긴 값을 출력해 봅시다.
```


```python
name = input('이름을 입력 해 주세요. : ')
print(name)
```

    이름을 입력 해 주세요. : 길상욱
    길상욱
    

* 반환값은 항상 문자열의 형태로 반환됩니다.

```python
>>> num = input('숫자를 입력 해 주세요. : ')
숫자를 입력 해 주세요. : 100
    
>>> print(num)
'100'

>>> print(type(num))
<class 'str'>
```


```python
# input()으로 입력 받은 값의 type을 출력해 봅시다.
```


```python
x = input()
print(type(x))
```

    1
    <class 'str'>
    

## 주석(Comment)

* 한 줄 주석은 `#`으로 표현합니다. 

* 여러 줄의 주석은 
    1. 한 줄 씩 `#`을 사용해서 표현하거나,
    2. `"""` 또는 `'''`(여러줄 문자열, multiline string)으로 표현할 수 있습니다.
    (multiline은 주로 함수/클래스를 설명(docstring)하기 위해 활용됩니다.)


```python
# 주석을 연습해봅시다. 
```


```python
# print('hello') # 이 줄은 실행되지 않습니다.
print('world')
```

    world
    


```python
# 여러줄 주석을 multiline string을 활용하여 연습해봅시다.
```


```python
"""
이것은
여러줄에 걸친
주석을 만드는 코드입니다.
"""
print('world')
```

    world
    

# 자료형(Data Type)

## 자료형 분류
- **불린형**(Boolean Type)
- **수치형**(Numeric Type)
    - int (정수, integer)
    - float (부동소수점, 실수, floating point number)
- **문자열**(String Type)
- **None**
    - 값이 없음을 표현하기 위한 타입


<img width="634" alt="자료형" src="https://user-images.githubusercontent.com/45934087/148158891-fe28256b-1df4-4b83-ab51-54d06c107d20.png">


## 불린형 (Boolean Type)

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.

비교/논리 연산을 수행 등에서 활용됩니다.

다음은 `False`로 변환됩니다.
```
0, 0.0, (), [], {}, '', None
```


```python
# print와 type을 이용하여 True와 False의 타입을 출력해 봅시다.
```


```python
print(type(True))
print(type(False))
```

    <class 'bool'>
    <class 'bool'>
    

- bool() 함수
    - 특정 데이터가 True인지 False인지 검증합니다.


```python
# 0, '', 1, [], -1, [1, 2, 3] 을 bool 함수를 이용하여 타입을 확인해 봅시다.
```


```python
print(bool(0))
```

    False
    


```python
print(bool(''))
```

    False
    


```python
print(bool(1))
```

    True
    


```python
print(bool([]))
```

    False
    


```python
print(bool(-1))
```

    True
    


```python
print(bool([1, 2, 3]))
```

    True
    

## 수치형(Numeric Type)
[파이썬 문서](https://docs.python.org/ko/3/library/stdtypes.html#numeric-types-int-float-complex)

###  `int` (정수, ingteger)

모든 정수는 `int`로 표현됩니다.

Python3에서는 `long` 타입은 없고 모두 `int` 타입으로 표기 됩니다.

* 보통 프로그래밍 언어 및 Python2에서의 long은 OS 기준 32/64비트입니다.
* Python3에서는 모두 int로 통합되었습니다.

8진수 : `0o` / 2진수 : `0b` / 16진수: `0x` 로도 표현 가능합니다. 


```python
# 변수 a에 정수 3을 할당하고 해당 변수의 type을 알아봅시다.
```


```python
a=int(3)
print(a)
```

    3
    


```python
# 변수 a에 2의 64제곱을 할당합니다.
# print와 type을 이용하여 a의 값과 타입을 확인해봅시다.
```


```python
a=(2**64)
print(type(a))
```

    <class 'int'>
    

**파이썬에서 표현할 수 있는 가장 큰 수**
* 파이썬에서 가장 큰 숫자를 활용하기 위해 sys 모듈을 불러옵니다.
* 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형(integer)에서 오버플로우가 없습니다.
* 임의 정밀도 산술(arbitrary-precision arithmetic)을 사용하기 때문입니다. 

> **오버플로우(overflow)**
- 데이터 타입 별로 사용할 수 있는 메모리의 크기가 제한되어 있습니다.
- 표현할 수 있는 수의 범위를 넘어가는 연산을 하게 되면, 기대했던 값이 출력되지 않는 현상, 즉 메모리를 넘어선 상황을 의미합니다.

> **임의 정밀도 산술(arbitrary-precision arithmetic)**
- 사용할 수 있는 메모리양이 정해져 있는 기존의 방식과 달리, 현재 남아있는 만큼의 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있는 형태를 의미합니다.
- 특정 값을 나타내는데 4바이트가 부족하다면 5바이트, 더 부족하면 6바이트까지 사용할 수 있게 유동적으로 운용합니다.



```python
# 파이썬이 얼만큼 큰 숫자까지 저장할 수 있는지 확인해봅시다.
```


```python
import sys
max_int = sys.maxsize
# sys.maxsize 의 값은 2**63 - 1 => 64비트에서 부호비트를 뺀 63개의 최대치
print(max_int)
super_max = sys.maxsize * sys.maxsize
print(super_max)
```

    9223372036854775807
    85070591730234615847396907784232501249
    


```python
# n진수를 만들어봅시다.
# 2진수는 변수 binary_number에 0b10을 할당합니다.
# 8진수는 변수 octal_number에 0o10을 할당합니다.
# 10진수는 변수 decimal_number에 10을 할당합니다.
# 16진수는 변수 hexadecimal_number에 0x10을 할당합니다.
# 각 변수를 print를 이용해서 여러줄로 출력해봅시다.
```


```python
binary_number = 0b10
octal_number = 0o10
decimal_number = 10
hexadecimal_number = 0x10
print(f"""2진수 : {binary_number}
8진수 : {octal_number}
10진수 : {decimal_number}
16진수 : {hexadecimal_number}
""")
```

    2진수 : 2
    8진수 : 8
    10진수 : 10
    16진수 : 16
    
    

### `float` (부동소수점, 실수, floating point number)

실수는 `float`로 표현됩니다. 

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않습니다. (floating point rounding error)

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값이 같은지 비교하는 과정에서 문제가 발생할 수 있습니다.


```python
# 변수 a에 실수 3.5를 할당하고 해당 변수의 type을 알아봅시다.
```


```python
a = float(3.5)
print(type(a))
```

    <class 'float'>
    

#### 컴퓨터식 지수 표현 방식
* e를 사용할 수도 있습니다. (e와 E 모두 사용 가능)


```python
# 컴퓨터식 지수 표현 방식을 사용해봅시다.
# 변수 b에 지수 314e-2를 할당하고 해당 변수의 type을 알아봅시다.
# print를 이용해 변수 b의 값도 알아봅시다.
```


```python
b = 314e-2
print(type(b))
print(b)
```

    <class 'float'>
    3.14
    

#### 실수의 연산
* 실수의 경우 실제로 값을 처리하기 위해서는 조심할 필요가 있습니다.


```python
# 실수의 덧셈을 해봅시다.
# 실수 두 개를 더해봅시다. (3.5 + 3.2)
```


```python
print(3.5+3.2)
```

    6.7
    


```python
# 실수의 뺄셈을 해봅시다. (3.5 - 3.12)
```


```python
print(3.5+3.12)
```

    6.62
    


```python
# 우리가 원하는대로 반올림을 해봅시다.
# round() 는 0~4는 내림, 5는 동일하게 작동하지 않고 반올림 방식에 따라 다릅니다.
# 짝수에서 5는 내림 / 홀수에서 5는 올림
# round(값, 소수점자릿수)
# 3.5 - 3.12 의 값을 반올림하는데 소수점 2자리까지 나타나게 해봅시다.
```


```python
print(round(3.5-3.12,2))
```

    0.38
    


```python
# 3.5 - 3.12의 결과와 0.38의 값이 같은지 == 을 사용해서 확인해봅시다.
```


```python
print(bool(3.5-3.12==0.38))
```

    False
    


```python
# print를 이용해서 3.5 - 3.12의 값을 확인해 봅시다.
```


```python
print(3.5-3.12)
```

    0.3799999999999999
    

* 따라서 다음과 같은 방법으로 처리 할 수 있습니다. (이외에 다양한 방법이 있음)


```python
# 1. 기본적인 처리방법을 알아봅시다.
# 변수 a, b에 각각의 실수 값을 저장합니다.
# 그리고 abs()를 이용하여 a와 b의 차이를 구합니다.
# a와 b의 차이가 1e-10 값 이하이면 a 와 b 는 같다고 볼 수 있습니다.
```


```python
a = 3.5 - 3.12
b = 0.38

abs(a - b) <= 1e-10
```




    True




```python
# 2. sys 모듈을 통해 처리하는 방법을 알아봅시다.
# `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
# abs() 를 이용하여 a, b의 차이를 구합니다.
# a와 b의 차이가 sys.float_info.epsilon의 값 이하이면 a, b 는 같다고 볼 수 있습니다.
```


```python
import sys
abs(a - b) <= sys.float_info.epsilon
```




    True




```python
# 3. python 3.5부터 활용 가능한 math 모듈을 통해 처리하는 법을 알아봅시다.
```


```python
# math.isclose() 를 이용해서 a와 b의 값이 같은지 확인할수 있습니다.
import math
math.isclose(a, b)
```




    True



## 문자열 (String Type)

### 문자열
- 모든 문자는 `str` 로 표현됩니다.

### 기본 활용법

* 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능합니다.

* 단, 문자열을 묶을 때 동일한 문장부호를 활용해야하며, `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 하고 있습니다. 
(Pick a rule and Stick to it)


```python
# 문자열 hello 를 출력해 봅시다.
# 문자열 hello의 타입을 출력해 봅시다.
```


```python
print('hello')
print(type('hello'))
```

    hello
    <class 'str'>
    


```python
# 문자열 철수 '안녕' 을 출력해 봅시다.
# 문자열 철수 "안녕" 을 출력해 봅시다.
```


```python
print("철수 '안녕'")
print('철수 "안녕"')
```

    철수 '안녕'
    철수 "안녕"
    


```python
# 변수에 문자열을 할당하고 출력해봅시다.
# 변수 greeting 에 hi를 name 에 'ssafy'를 할당합시다. 
# 그리고 각각의 변수를 print로 찍어보고 type도 확인해봅시다.
```


```python
greeting = 'hi'
name = "'ssafy'"
print(greeting, name)
print(type(greeting),type(name))
```

    hi 'ssafy'
    <class 'str'> <class 'str'>
    


```python
# 변수 age 에 사용자로 부터 입력을 받을 수 있는 input()의 결과를 저장합시다.
# age 에 입력받은 값이 저장되었는지 그리고 그 type이 무엇인지 확인해봅시다.
# 숫자를 할당했을때와 문자를 할당했을때의 type이 같은지 다른지도 확인해봅시다.
```


```python
age = input()
print(age,type(age))
```

    str
    str <class 'str'>
    

- Immutable

문자열을 변경할 수 없음


```python
a = 'my string?'
a[-1] = '!'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [72], in <cell line: 2>()
          1 a = 'my string?'
    ----> 2 a[-1] = '!'
    

    TypeError: 'str' object does not support item assignment


- Iterable

문자열을 순회 가능함


```python
a = '123'
for char in a:
    print(char)
```

    1
    2
    3
    

### 중첩 따옴표 (Nested Quotes)
따옴표 안에 따옴표를 표현할 경우 아래와 같이 사용할 수 있습니다.

- 작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`


```python
print('문자열 안에 "작은 따옴표"를 사용하려면 큰 따옴표로 묶는다.')
```

    문자열 안에 "작은 따옴표"를 사용하려면 큰 따옴표로 묶는다.
    

- 큰따옴표: `"'작은' 따옴표를 담을 수 있습니다"`


```python
print("문자열 안에 '작은 따옴표'를 사용하려면 큰 따옴표로 묶는다.")
```

    문자열 안에 '작은 따옴표'를 사용하려면 큰 따옴표로 묶는다.
    

### 삼중 따옴표 (Triple Quotes)
작은 따옴표나 큰 따옴표를 삼중으로 사용합니다.

- 문자열 안에 따옴표를 넣을 때 사용합니다.

- 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능합니다.

* `PEP-8`에 따르면 이 경우에는 반드시 `"""`를 사용하도록 규정합니다.


```python
# 아래 작성된 내용을 삼중 따옴표와 하나의 print 문을 사용하여 출력해 봅시다.
```

문자열 안에 '작은 따옴표'나

"큰 따옴표"를 사용할 수 있고

여러 줄을 사용할 때도 편리하다.


```python
print("""
개행문자 없이
여러 줄을 그대로 출력 가능합니다.
""")
```

    
    개행문자 없이
    여러 줄을 그대로 출력 가능합니다.
    
    

### 이스케이프 시퀀스 (Escape sequence)

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 역슬래시 `\`를 활용하여 이를 구분합니다. 

|<center>예약문자</center>|내용(의미)|
|:--------:|:--------:|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\\\ |`\`|
|\\'|단일인용부호(`'`)|
|\\"|이중인용부호(`"`)|


```python
# 다음 문자열을 작은 따옴표와 escape sequence만을 사용하여 출력해 봅시다.
# 철수야 '안녕'
```


```python
print('철수야 \'안녕\'')
```

    철수야 '안녕'
    


```python
# 다음 문자열을 하나의 print 함수에서 출력해 봅시다.
# escape sequence를 이용합니다.
```

이 다음은 엔터.
그리고 탭    탭


```python
print('이 다음은 엔터. \n그리고 탭\t탭')
```

    이 다음은 엔터. 
    그리고 탭	탭
    

### String interpolation 

* `%-formatting` 

    * `%d` : 정수
    
    * `%f` : 실수
    
    * `%s` : 문자열

* [`str.format()` ](https://pyformat.info/)

* [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원


```python
# name 변수에 이름, score 변수에 학점을 할당해봅시다.
```


```python
name = '철수'
score = 95
```


```python
# %-formatting을 활용해봅시다.
# print를 이용하여 name 을 출력해봅시다..
# print를 이용하여 score를 정수 형태로 출력해봅시다.
# print를 이용하여 score를 실수 형태로 출력해봅시다.
```


```python
print('%s' %name)
print('%d' %score)
print('%f' %score)
```

    철수
    95
    95.000000
    


```python
# str.format()을 활용해봅시다.
# name 을 출력해봅시다.
```


```python
print('{}'.format(name))
```

    철수
    


```python
# f-string을 활용해봅시다.
# name 을 출력해봅시다.
```


```python
print(f'{name}')
```

    철수
    


```python
# 여러줄 문자열에서도 사용 가능합니다.
# f-string을 이용하여 name을 여러줄 문자열로 출력해봅시다.
```


```python
print(f"""
Hello,
{name}
""")
```

    
    Hello,
    철수
    
    

* f-strings에서는 형식을 지정할 수 있습니다.


```python
# 다양한 형식을 활용하기 위해 datetime 모듈로 오늘을 표현해봅시다.
# today 에 현재 시간 날짜를 할당해봅시다.
# print를 이용하여 today를 출력해봅시다.
```


```python
import datetime
today = datetime.datetime.now()
print(today)
```

    2022-07-19 10:22:09.290511
    


```python
# interpolation에서 출력형식을 지정할 수 있습니다.
# today에 저장된 시간을 YYYY년, mm월, dd일, a요일 로 구분해서 출력해봅시다.
# 각각 %y, %m, %A를 사용합니다.
```


```python
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
```

    오늘은 22년 07월 19일 Tuesday
    

* f-strings에서는 연산과 출력형식 지정도 가능합니다.


```python
# string interpolation을 통해 출력형식 지정 뿐만 아니라, 연산도 가능합니다.
# pi = 3.141592를 할당하고 
# 원주율은 3.14. 반지를이 2일 때 원의 넓이는 12.566368이라고 출력해봅시다.
```


```python
pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {2*2*pi}')
```

    원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
    

## None Type

파이썬에서는 값이 없음을 표현하기 위해 `None` 타입이 존재합니다.


```python
# None의 타입을 알아봅시다.
```


```python
print(type(None))
```

    <class 'NoneType'>
    


```python
# 변수에 저장해서 확인해봅시다.
# 변수 a에 None을 할당하고 출력해봅시다.
```


```python
a=None
print(a)
```

    None
    

# 컨테이너(Container)

여러 개의 값을 저장할 수 있는 것(객체)을 의미하며, `서로 다른 자료형`을 저장 할 수 있습니다.

### 컨테이너 분류
- 시퀀스(Sequence)형 : 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형 : 순서가 없는(unordered) 데이터

<img width="712" alt="container" src="https://user-images.githubusercontent.com/45934087/148164052-3b12d3a2-a95e-4d4d-ae25-86ca1ba9657b.png">

## 시퀀스(sequence)형 컨테이너

`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타냅니다. 

* **주의! 순서대로 나열된 것이 `정렬되었다(sorted)`라는 뜻은 아닙니다.**

### 특징
1. 순서가 있습니다.

2. **특정 위치의 데이터를 가리킬 수 있습니다.**

### 종류
파이썬에서 기본적인 시퀀스 타입은 다음과 같습니다.

* 리스트(list)

* 튜플(tuple)

* 레인지(range)

* *문자형(string)*

* *바이너리(binary)* : 다루지 않습니다.



### 리스트 (List)

<center><img src="https://user-images.githubusercontent.com/18046097/61180421-fe90ae80-a650-11e9-8211-d06f87756d05.png", alt="list figure"/></center>

**생성과 접근**
```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 및 `list()` 를 통해 만들 수 있습니다.


```python
# 빈 list를 만들어봅시다.
# 변수명 my_list인 list를 대괄호로 만들어봅시다.
# 변수명 another_list인 list를 list()로 만들어 봅시다.
# 두 변수의 타입을 출력해 봅시다.
```


```python
my_list=[]
another_list = list()
print(type(my_list),type(another_list))
```

    <class 'list'> <class 'list'>
    


```python
# 원소를 포함한 list를 만들어 봅시다.
# 변수명이 location인 list에 ssafy 지역 5곳을 원소로 포함해 만들어 봅시다.
# 변수 location을 출력해 봅시다.
# location의 타입을 출력해 봅시다.
```


```python
location = ['서울', '대전', '광주', '구미', '부울경']
print(location, type(location))
```

    ['서울', '대전', '광주', '구미', '부울경'] <class 'list'>
    


```python
# location의 첫번째 값을 인덱스로 접근해 봅시다.
```


```python
print(location[0])
```

    서울
    


순서가 있는 시퀀스로 인덱스를 통해 접근 가능합니다.
- 값에 대한 접근은 `list[i]` 방식으로 접근합니다.

![image](https://user-images.githubusercontent.com/45934087/148164331-f0ff4193-6b05-4d99-bbde-dd1eef13b0b1.png)



```python
# 변수 boxes에 문자열 'A', 'B', 리스트 ['apple', 'banana', 'cherry']를 할당합니다.
```


```python
boxes=['A', 'B', ['apple', 'banana', 'cherry']]
```


```python
# boxes의 길이를 len 함수를 이용하여 출력해 봅시다.
```


```python
print(len(boxes))
```

    3
    


```python
# boxes의 3번째 요소를 인덱스로 접근하여 출력해 봅시다.
```


```python
print(boxes[2])
```

    ['apple', 'banana', 'cherry']
    


```python
# boxes의 3번째 요소들 중, 마지막 요소를 negative index로 접근하여 출력해 봅시다.
```


```python
print(boxes[2][-1])
```

    cherry
    


```python

```


```python
# boxes의 마지막 요소들 중, 두번째 요소의 첫번째 문자열을 출력해 봅시다.
```


```python
print(boxes[2][1][0])
```

    b
    


```python

```

### 튜플 (Tuple)

**생성과 접근**
```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

- tuple은 수정 불가능(불변, immutable)합니다.

- 직접 사용하기 보다는 파이썬 내부에서 다양한 용도로 활용되고 있습니다.


```python
# tuple을 만들어봅시다.
# 변수명이 my_tuple인 tuple을 만들어 봅시다. 단, 무작위 정수 2개를 포함하여 만듭니다.
# my_tuple의 타입을 출력해 봅시다.
```


```python
my_tuple = (1, 2)
print(type(my_tuple))
```

    <class 'tuple'>
    


```python
# 아래와 같은 방식으로도 만들 수 있습니다.
```


```python
another_tuple = 1, 2
print(another_tuple)
print(type(another_tuple))
```

    (1, 2)
    <class 'tuple'>
    

**튜플 생성 주의 사항**
- 단일 항목의 경우


```python
# 하나의 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표를 붙여야 합니다.
# 아래 코드를 실행하여 변수 a의 타입을 확인해 봅시다.
a = 1,
print(a)
print(type(a))
```

    (1,)
    <class 'tuple'>
    


```python
# 변수명이 single_tuple인 하나의 요소(값)로 구성된 tuple을 만들어 봅시다. (길이가 1)
# 하나의 요소(값)로 구성된 tuple은 값 뒤에 쉼표를 붙여서 만듭니다.
# single_tuple의 타입을 출력해 봅시다.
# single_tuple의 길이를 출력해 봅시다.
```


```python
single_tuple = ('hello',)
print(type(single_tuple))
print(len(single_tuple))
```

    <class 'tuple'>
    1
    


```python
# 길이가 1인 tuple을 만들 때 쉼표가 없는 경우 어떻게 되는지 확인 해봅시다.
```


```python
tuple_or_not = ('hello')
print(type(tuple_or_not))
```

    <class 'str'>
    

- 복수 항목의 경우


```python
# 마지막 항목에 붙은 쉼표는 생략 할 수 있습니다.
# 아래 코드를 실행하여 변수 b와 c의 타입을 확인해 봅시다.
```


```python
b = 1, 2, 3
print(b)
print(type(b))
```

    (1, 2, 3)
    <class 'tuple'>
    


```python
c = 4, 5, 6,
print(c)
print(type(c))
```

    (4, 5, 6)
    <class 'tuple'>
    

**튜플 대입**
- 우변의 값을 좌변의 변수에 한번에 할당하는 과정을 의미합니다.
- 튜플은 일반적으로 파이썬 내부에서 활용됩니다.
    - 추후 함수 파트에서 복수의 값을 반환하는 경우에도 확인할 수 있습니다.


```python
# 파이썬 내부에서는 다음과 같이 활용됩니다. (변수 및 자료형 예제에서 사용된 코드입니다.)
```


```python
x, y = 1, 2
print(x)
print(y)
```

    1
    2
    


```python
# 실제로는 tuple로 처리됩니다.
```


```python
x, y = (1, 2)
print(x)
print(y)
```

    1
    2
    


```python
# 변수의 값을 swap하는 코드 역시 tuple을 활용하고 있습니다. 
```


```python
x, y = y, x
print(x)
print(y)
```

    2
    1
    


```python
# 변수명이 empty인 빈 tuple을 만들어 봅시다.
# 빈 tuple은 빈 괄호 쌍으로 만들어집니다.
# empty의 타입을 출력해 봅시다.
# empty의 길이를 출력해 봅시다.
```


```python
empty = ()
print(type(empty))
print(len(empty))
```

    <class 'tuple'>
    0
    

### 레인지 (range())

`range` 는 정수의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)` 


> 0부터 n-1까지 값을 가짐


범위 지정 : `range(n, m)` 

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다


```python
# range를 만들어봅시다.
# 0부터 2까지 값을 가지는 range를 만들고 타입을 출력해 봅시다.
```


```python
print(type(range(3)))
```

    <class 'range'>
    


```python
# 0부터 9까지 값을 가지는 range를 만들고 list로 형 변환을 해 봅시다.
# 작성한 range를 list()로 감싸 형 변환 할 수 있습니다.
```


```python
list(range(10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
# 4부터 8까지의 숫자를 담은 range를 만들고 list로 형 변환을 해 봅시다.
```


```python
list(range(4,9))
```




    [4, 5, 6, 7, 8]




```python
# range(start, end, [step, ])을 활용합니다.
# 0부터 -9까지 담긴 range를 만들고 list로 형 변환을 해 봅시다.
# 출력 결과는 다음과 같습니다.
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```


```python
list(range(0,-10,-1))
```




    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]



### 딕셔너리 (dictionary)

`dictionary`는 `key`와 `value`가 쌍으로 이뤄져있습니다.


<center><img src="https://user-images.githubusercontent.com/18046097/61180427-1405d880-a651-11e9-94e1-1cc5c2a2ff34.png"></center> 

**생성과 접근**

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

* `{}`를 통해 만들며, `dict()`로 만들 수 있습니다.
* 순서를 보장하지 않습니다.
* `key`는 **변경 불가능(immutable)한 데이터**만 가능합니다. (immutable : string, integer, float, boolean, tuple, range)
* `value`는 `list`, `dictionary`를 포함한 모든 것이 가능합니다.


```python
# 비어있는 dictionary를 두가지 방법으로 만들어봅시다.
# {}와 dict()로 만들 수 있습니다.
# 두 변수의 타입을 출력해 봅시다.
```


```python
a = {}
b = dict()
print(type(a),type(b))
```

    <class 'dict'> <class 'dict'>
    


```python
# dictionary에 중복된 key는 존재할 수 없습니다.
```


```python
dict_a = {1: 1, 2: 2, 3: 3, 1: 4}
print(dict_a)
```

    {1: 4, 2: 2, 3: 3}
    


```python
# 지역번호가 담긴 전화번호부를 만들어봅시다.
# 변수 phone_book에 key를 지역명, value를 지역번호로 가지는 원소를 작성합니다.
# 예) 서울 - 02
```


```python
phone_book = {'서울':'02', '인천':'032', '경기':'031', '강원':'033'}
```


```python
# 위에서 작성한 phone_book이 가지고 있는 key 목록을 확인 해 봅시다.
# dictionary의 .keys() 메소드를 활용하여 key를 확인 해볼 수 있습니다.
```


```python
print(phone_book['서울'])
```

    02
    


```python
# 위에서 작성한 phone_book이 가지고 있는 value 목록을 확인 해 봅시다.
# 딕셔너리의 .values() 메소드를 활용하여 value를 확인 해볼 수 있습니다.
```


```python
print(phone_book.values())
```

    dict_values(['02', '032', '031', '033'])
    


```python
# 위에서 작성한 phone_book이 가지고 있는 key와 value 목록을 확인 해 봅시다.
# 딕셔너리의 .items() 메소드를 활용하여 key, value를 확인 해볼 수 있습니다.
```


```python
print(phone_book.items())
```

    dict_items([('서울', '02'), ('인천', '032'), ('경기', '031'), ('강원', '033')])
    
