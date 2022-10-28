# 모듈(Module)

- 모듈(module)은 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)
- 파이썬의 경우, 특정 기능을 파이썬 파일(.py) 단위로 작성한 것을 말합니다.


## 모듈 생성
- jupyter notebook 파일 트리 화면에서 New > Text File을 선택해 새로운 파일을 만들어 주세요.
- 파일의 이름을 `check.py`로 저장해 주세요.


```python
# check.py 파일에 짝수, 홀수를 판별하는 함수를 작성해봅시다.
# 1. n을 매개변수로 받아 홀수인지를 판단하는 odd 함수를 작성해 주세요.
# 2. return은 n이 홀수라면 True를, 아니라면 False를 return 합니다.

```


```python
# 3. n을 매개변수로 받아 짝수인지를 판단하는 even 함수를 작성해 주세요.
# 4. return은 n이 짝수라면 True를, 아니라면 False를 return 합니다.


```

## 모듈 활용

### `import`
- 모듈을 활용하기 위해서는 반드시 `import`문을 통해 내장 모듈을 이름공간(namespace)으로 가져와야 합니다.
- `import`문이 사용된 코드의 위치에 따라 namespace가 결정됩니다.
- 코드 최상단에 `import`문을 작성할 경우, Global namespace에 import됩니다.(함수 챕터에서 학습한 전역스코프와 지역스코프 참조)


```python
# import를 이용하여 작성한 check.py를 가져옵니다.
import check
```


```python
# 우리가 만든 check 모듈의 odd, even 함수를 dir 함수를 통해 확인해봅시다.
# dir 내장 함수는 하나의 객체를 매개변수로 넣어주면, 
# 해당 객체가 어떤 변수와 메서드(method)를 가지고 있는지 나열해 줍니다.
dir(check)
```




    ['__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'even',
     'odd']




```python
# odd와 even 함수를 사용해봅시다.
print(check.odd(31))
print(check.even(21))
```

    True
    False
    

# 패키지(Package)

- 패키지(package)는 하나의 디렉토리에 모듈(module)이 옹기종기 모여있는 형태를 말합니다. 
- 우리는 이 패키지를 점(`.`)으로 구분해서 패키지.모듈 이름(`package.module`)형태로 모듈을 구조화 할 수 있습니다.

## 패키지 생성

- jupyter notebook 파일 트리 화면에서 New > Folder를 선택합니다.
- 그리고 다음과 같은 폴더 구조를 생성해 주세요.

```python
my_package/
    __init__.py
    math/
        __init__.py
        tools.py  
```
> 모듈 이름 `my_package.math`는 `my_package`라는 이름의 패키지에 있는 `math`라는 이름의 하위 패키지를 가리킵니다.

- **`__init__.py`**가 뭐지?
> `__init__.py`는 '이 파일이 있는 디렉터리를 하나의 파이썬 패키지로 인식해!'라고 파이썬에게 알려주는 역할을 하는 파일입니다. 사실 python 3.3 버전 이후부터는 이 파일이 없어도 패키지로 인식하지만, 우리가 작성하는 프로그램이 항상 python 3.3 버전 이상에서 실행된다는 보장을 할 수 없으므로 하위 버전 호환을 위해 `__init__.py`를 생성하는 것이 권장됩니다.

`math` 패키지 만들기
- 아래의 파일 구조로 `math` 패키지를 만들어 주세요.
- 모든 `__init__.py` 파일은 빈 파일로 만듭니다.
```py
my_package/
    __init__.py
    math/
        __init__.py
        tools.py 
```


```python
# 다음 코드를 math/tools.py에 작성해 주세요.

pi = 3.14159265358979323846
e = 2.71828182845904523536

def my_max(a, b):
    if a > b:
        return a
    else:
        return b
```

`statistics` 패키지 만들기
- 아래의 파일 구조로 `statistics` 패키지를 만들어 주세요.
```py
my_package/
    __init__.py
    math/
        __init__.py
        tools.py  
    statistics/
        __init__.py
        tools.py
```


```python
# 다음 코드를 statistics/tools.py에 작성해 주세요.

def standard_deviation(values):
    mean = sum(values) / len(values)
    sum_var = sum(pow(value - mean, 2) for value in values) / len(values)
    std_dev = math.sqrt(sum_var)
    return std_dev

```

## 패키지 활용
- 모듈과 동일하게 `from`과 `import` 키워드를 활용해 가져와서 사용합니다.

### `from` *패키지* `import` *모듈*

`import`는 `from`과 함께 활용할 수 있습니다.


```python
# math 패키지의 tools 모듈을 namespace에 추가해봅시다.

from my_package.math import tools
```

### `from` *패키지.모듈* `import` *데이터*

특정한 함수 혹은 어트리뷰트만 활용하고 싶을 때는 아래와 같이 작성합니다.


```python
# math 패키지의 tools 모듈 내부에 있는 자연 상수 e를 print를 이용해 출력해보세요.
from my_package.math.tools import e
print(e)
```

    2.718281828459045
    

### `from` *모듈* `import` `*`

`*`는 해당하는 모듈 내의 모든 변수, 함수, 클래스를 가져옵니다.


```python
# math 패키지 내부의 tools 모듈에 있는 모든 변수와 함수를 가져와봅시다.
# pi 변수와 my_max 함수를 사용해 보세요.
from my_package.math.tools import*
print(pi)
print(y_max(5,3))
```

    3.141592653589793
    




    5



### `from` *모듈* `import` *데이터*  `as` *별명*

모든 데이터에는 `as`를 이용해서 새로운 이름(alias)을 붙일 수 있습니다.


```python
# statistics 패키지 tools 모듈에 있는 standard_deviation 함수를 
# 'sd'라는 짧은 이름으로 줄여서 가져와봅시다.
# standard_deviation 함수를 사용해서 [1, 2, 3, 4, 5]의 표준 편차를 구해봅시다.

from my_package.statistics.tools import standard_deviation as sd
print(sd([1,2,3,4,5]))
```

    1.4142135623730951
    

# 정리

## 용어 정리
- 모듈 vs 패키지
- 라이브러리 (library)?
> 라이브러리는 패키지가 옹기종기 모여있는 형태입니다! <br>다만 종종 패키지와 라이브러리를 같은 의미로 쓰기도 합니다.

|용어|정의|
|--------|-------------------|
|  모듈   | 특정 기능을 `.py` **파일 단위**로 작성한 것. |
|  패키지  | 특정 기능과 관련된 여러 **모듈들의 집합**. 패키지 안에는 또다른 서브 패키지를 포함 할수도 있음.  |
| 파이썬 표준 라이브러리 | 파이썬에 **기본적으로 설치된 모듈과 내장 함수**를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 불림. |
| 패키지 관리자(**`pip`**) | `PyPI` 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지. |

## 모듈과 패키지 사용하기
### 모듈
```py
import module
from module import var, function, Class
from module import *
```

### 패키지
```py
from package import module
from package.module import var, function, Class

```
