<p style="font-size: 33px; font-weight: 700; margin-bottom: 3rem">OOP</p>



- 객체(Object)
- 객체지향프로그래밍(Object Oriented Programming)
- 클래스(Class)와 객체(Object)


# 객체(Object)

> Python에서 **모든 것은 객체(object)**입니다.
>
> 모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가집니다.


객체(Object)의 특징

- **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가? 
- **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
- **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?

# 객체 지향 프로그래밍(Object-Oriented Programming)

Object가 중심(oriented)이 되는 프로그래밍

**<wikipedia - 객체지향 프로그래밍>**
>
> 객체 지향 프로그래밍(영어: Object-Oriented Programming, OOP)은 컴퓨터 프로그래밍의 패러다임의 하나입니다. 
>
> 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것입니다.




## 절차 중심 vs. 객체 중심

> 프로그래밍 패러다임: 어떻게 프로그램을 작성할 것인가

## 객체 중심의 장점


**<wikipedia - 객체지향 프로그래밍>**
> 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됩니다. 
>
> 또한 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점을 갖고 있습니다.

- 코드의 **직관성**

- 활용의 **용이성**

- 변경의 **유연성**

## OOP 기초

### 기본 문법

```python
# 클래스 정의
class MyClass:
    pass

# 인스턴스 생성
my_instance = MyClass()

# 속성 접근
my_instance.my_attribute

# 메서드 호출
my_instance.my_method()
```

### 클래스(class)

- 클래스는 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류입니다.

### 인스턴스(Instance)
- 특정 클래스(class)의 실제 데이터 예시(instance)입니다. 
- 파이썬에서 모든 것은 객체이고, **모든 객체는 특정 클래스의 인스턴스**입니다.

```python
# Person 클래스
class Person:
    pass

# ssafykim은 Person 클래스의 인스턴스
ssafykim = Person()
```


```python
class Person:
    pass
```


```python
# Person 클래스의 인스턴스를 만들어봅시다.

ssafykim=Person()
```


```python
# ssafykim 변수에 담긴 인스턴스가 Person 클래스의 인스턴스인지 확인해봅시다.
# isinstance 함수를 활용합니다.

isinstance(ssafykim,Person)
```




    True



## 속성(attribute)과 메서드(method)

객체의 속성(상태, 데이터)과 조작법(함수)을 명확히 구분해 봅시다.

| type         | attributes       | methods                                |
| -------------| ---------------- | -------------------------------------- |
| `complex`    | `.real`, `.imag` |              _                          |
| `str`        |       _          | `.capitalize()`, `.join()`, `.split()` |
| `list`       |       _          | `.append()`, `.reverse()`, `.sort()`   |
| `dict`       |       _          | `.keys()`, `.values()`, `.items()`     |


### 속성(attribute)

- 속성(attribute)은 객체(object)의 상태/데이터를 뜻합니다.


**활용법**

```python
<객체>.<속성>
```

**예시**

```python
person.name
```

- `Person` 클래스의 객체들이 가지게 될 데이터를 활용해봅시다.

### 메서드(method)

- 특정 객체가 할 수 있는 행위(behavior)를 뜻 합니다.

**활용법**
```python
<객체>.<메서드>()
```

**예시**
```python
person.talk()
person.eat()
```

- `Person` 클래스에 공통적으로 적용 가능한 함수인 `메서드`를 활용해봅시다.

# 인스턴스(instance)

## 인스턴스(instance) 생성
* 정의된 클래스(`class`)에 속하는 객체를 해당 클래스의 인스턴스(instance)라고 합니다.

* `Person` 클래스의 인스턴스는 `Person()`을 호출함으로써 생성됩니다.

* `type()` 함수를 통해 생성된 객체의 클래스를 확인할 수 있습니다.


**활용법**


```python
# 인스턴스 = 클래스()
person1 = Person()
```

- `person1`은 사용자가 정의한(user-defined) `Person`이라는 데이터 타입(data type)의 인스턴스입니다.


```python
class Person:
    pass
```


```python
# Person 클래스의 인스턴스 p1과 p2를 생성해봅시다.
# 두 인스턴스의 type을 출력해보세요.

p1 = Person()
p2 = Person()
print(type(p1))
print(type(p2))
```

    <class '__main__.Person'>
    <class '__main__.Person'>
    

## 인스턴스 변수
* 인스턴스의 속성(attribute)
* 각 인스턴스들의 고유한 데이터
* 생성자 메서드에서 `self.변수명`로 정의(생성자 메서드는 뒤에 학습합니다.)
* 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당

---
**활용법**
    
```python
class Person:
    pass

p1 = Person()
p1.name = 'jack'
p1.age = 25
```


```python
# 위와 같은 Person 클래스를 똑같이 정의해봅시다.

class Person:
    pass
```


```python
# Person 클래스의 인스턴스를 생성하고, me 변수에 저장합니다.
# me의 인스턴스 변수 name을 본인 이름으로 설정합니다.

me = Person()
me.name = 'Sang-Uk'
```


```python
# me 인스턴스의 name 변수에 접근하여 값을 출력해봅시다.

me.name
```




    'Sang-Uk'




```python
# me 인스턴스의 name 변수의 값을 새로운 이름으로 할당하고 다시 출력해봅시다.

me.name = 'tmp'
print(me.name)
```

    tmp
    

## 인스턴스 메서드

> 메서드란?
> - 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미합니다.

* 인스턴스 메서드는 인스턴스가 사용할 메서드에 해당합니다.
* 클래스 내부에 정의되는 메서드는 기본적으로 인스턴스 메서드로 생성됩니다.
* **메서드 호출시, 첫번째 인자로 인스턴스 자기자신에 해당하는 `self`가 전달됩니다**

**활용법**

```python
class MyClass:
    def instance_method(self, arg1, arg2, ...):
        ...

my_instance = MyClass()
# 인스턴스 생성 후 메서드를 호출하면 자동으로 첫 번째 인자로 인스턴스(my_instance)가 들어갑니다.
my_instance.instance_method(.., ..)  
```


```python
# 위의 활용법을 참고하여 Person 클래스와 talk() 메서드를 정의했습니다.
```


```python
class Person:
    def talk(self):
        print('안녕!')
```


```python
# Person 클래스의 인스턴스 p1, p2를 생성하고 각각 talk 메서드를 실행해봅시다.

p1 = Person()
p2 = Person()
p1.talk()
p2.talk()
```

    안녕!
    안녕!
    

- 메서드도 함수이기 때문에 추가적인 인자를 받을 수 있습니다.
- `Person` 클래스를 재정의 하며 `talk` 메서드를 정의하고, `eat` 메서드를 추가로 정의해봅시다.
- `eat` 메서드는 `food` 라는 이름의 인자를 받아서 출력합니다.
- 추가적인 인자를 받기 위해서는 아래와 같은 모습으로 코드가 작성되어야 합니다.

```python
class MyClass:
    def method1(self):
        print('Hi')
    
    def method2(self, arg):
        print(arg)
```


```python
class Person:
    def talk(self):
        print('안녕')
    
    def eat(self, food):
        print(f'냠냠 {food}')
```


```python
# Person 클래스의 인스턴스 p1을 생성하고 eat() 메서드를 인자와 함께 호출해봅시다.

p1 = Person()
p1.eat('굿')
```

    냠냠 굿
    


```python
# 기본 인자, 가변 인자 리스트 등 함수의 인자와 동일하게 매개변수를 정의할 수 있습니다.
# Person 클래스를 재정의하며, eat() 메서드를 정의할 때 food 인자의 기본 값을 원하는 음식으로 설정해봅시다.

class Person:
    def eat(self, food = '굿'):
        print(f'냠냠 {food}')
```


```python
# Person 클래스의 인스턴스 p1을 생성하고, eat() 메서드를 인자 있이/없이 두번 호출해봅시다.

p1 = Person()
p1.eat()
p1.eat('삼겹살')
```

    냠냠 굿
    냠냠 삼겹살
    

##  `self` 

> 인스턴스 자신(self)

* Python에서 인스턴스 메서드는 **호출 시 첫번째 인자로 인스턴스 자신이 전달**되게 설계되었습니다. 


* 보통 매개변수명으로 `self`를 첫번째 인자로 정의 (다른 이름도 가능하지만 추천하지는 않습니다.)


```python
# 아래의 Person 클래스를 통해서 self가 무엇인지 확인해봅시다.
class Person:
    def test(self):
        print(self)
```


```python
# Person 클래스의 인스턴스 p1을 생성하고 test() 메서드를 호출하여 self를 확인해봅시다.

p1 = Person()
p1.test()
```

    <__main__.Person object at 0x000001266ADD63D0>
    


```python
# p1을 출력하여 비교해봅시다.

print(p1)
```

    <__main__.Person object at 0x000001266ADD63D0>
    

### 생성자(constructor) 메서드
- 인스턴스 객체가 생성될 때 자동으로 호출되는 함수입니다.
- 반드시 `__init__` 이라는 이름으로 정의합니다.

---
**활용법**

```python
class MyClass:
    def __init__(self):
        print('생성될 때 자동으로 호출되는 메서드입니다.')
```

- 생성자를 활용하면 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있습니다.



```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'I am {self.name}')
```


```python
# 자신의 이름을 인자로 넘기며 Person의 인스턴스 p1를 생성해봅시다.

p1=Person('Sang-Uk')
```


```python
# talk() 메서드를 호출해 봅시다.

p1.talk()
```

    I am Sang-Uk
    


```python
# talk 메서드를 클래스에서 메서드를 실행해봅시다. self는 정말 빈자리일까요?

Person.talk()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Input In [61], in <cell line: 3>()
          1 # talk 메서드를 클래스에서 메서드를 실행해봅시다. self는 정말 빈자리일까요?
    ----> 3 Person.talk()
    

    AttributeError: type object 'Person' has no attribute 'talk'


### 소멸자(destructor) 메서드
- 인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수입니다.
- 반드시 `__del__` 이라는 이름으로 정의합니다.

---

**활용법**

```python
# 소멸자 정의
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
    
# 소멸자 활용
del 인스턴스
```


```python
# 생성자와 소멸자를 만들어봅시다.
# 생성자 메서드는 __init__으로 정의하고,
# 소멸자 메서드는 __del__라는 이름으로 정의합니다.

class Person:
    def __init__(self,name):
        self.name = name
    
    def __del__(self):
        print(f'{self.name}은 사라졌습니다.')
```


```python
# Person 클래스의 인스턴스를 만들고 person1 변수에 할당합니다.

person1=Person('name')
```


```python
# del 키워드를 이용하여 소멸자를 활용해봅시다. 

del person1
```

    name은 사라졌습니다.
    

## 속성(Attribute) 정의

- 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터를 의미합니다.

- `self.<속성명> = <값>` 혹은 `<인스턴스>.<속성명> = <값>`으로 설정합니다

---
**활용법**

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 나는 {self.name}')
```


```python
# 인스턴스의 변수, 즉 개별 인스턴스들의 속성 데이터를 초기화와 동시에 정의해봅시다.
# 아래 Person 클래스는 name이라는 속성이 정의되어 있습니다.

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 나는 {self.name}')
```


```python
# 속성 정의는 꼭 생성자(__init__) 메서드에 작성해야 하지는 않지만, 일반적으로 생성자 메서드에 많이 작성합니다.
# 생성자 메서드를 통해 생성과 동시에 인스턴스 속성에 값을 할당할 수 있기 때문입니다.
# 새로운 Person의 인스턴스 p1을 이름과 함께 초기화 하고, 이름을 출력해봅시다.
```


```python
p1 = Person('asd')
print(p1.name)
```

    asd
    


```python
# 인스턴스 속성의 값을 변경할 수도 있습니다.
# 위에서 생성한 p1 인스턴스의 name을 다른 값으로 할당해보고, talk 메서드를 실행해봅시다.

p1.name = 'dfe'
p1.talk()
```

    안녕, 나는 dfe
    


```python
# 생성자 메서드도 함수이기 때문에, 인자의 개수가 맞지 않으면 에러가 발생합니다.
# name인자 없이 새로운 Person의 인스턴스 p1을 생성해봅시다.

p1 = Person()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [50], in <cell line: 4>()
          1 # 생성자 메서드도 함수이기 때문에, 인자의 개수가 맞지 않으면 에러가 발생합니다.
          2 # name인자 없이 새로운 Person의 인스턴스 p1을 생성해봅시다.
    ----> 4 p1 = Person()
    

    TypeError: __init__() missing 1 required positional argument: 'name'



```python
# 위에서 생성한 인스턴스 p1을 del 연산자를 사용해 소멸시켜봅시다.

del p1
```

## 매직(스페셜) 메서드
- 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`라고 불립니다.
- 매직(스페셜) 메서드 형태: `__someting__`
```python
 '__str__(self)',
 '__len__(self)',
 '__repr__(self)',
 '__lt__(self, other)',
 '__le__(self, other)',
 '__eq__(self, other)',
 '__ne__(self, other)',
 '__gt__(self, other)',
 '__ge__(self, other)',
```

### `__str__(self)` 

```python
class Person:
    def __str__(self):
        return '객체 출력(print)시 보여줄 내용'
```

- 특정 객체를 출력(`print()`) 할 때 보여줄 내용을 정의할 수 있습니다.


```python
# dir() 함수를 통해 문자열 인스턴스가 활용 가능한 메서드를 확인해봅시다.
# 아래 코드를 실행시켜 확인해보세요.

dir('')
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'removeprefix',
     'removesuffix',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']




```python
# Person 클래스를 생성했습니다.

class Person:
    def __init__(self, name):
        self.name = name
```


```python
# Person의 인스턴스 p1을 생성 후 출력해봅시다.

p1 = Person('ccc')
print(p1)
```

    <__main__.Person object at 0x000001266AD6ECD0>
    


```python
# __str__() 매직메서드를 아래와 같이 정의했습니다.

class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'나는 {self.name}'
```


```python
# 새로운 인스턴스 p2를 생성후 p2를 출력해봅시다.

p2 = Person('ccc')
print(p2)
```

    나는 ccc
    

## 실습

> 매직메서드를 활용하여 인스턴스간의 비교연산(`>`, `==`)이 가능하도록 매직메서드를 정의해봅시다.
1. `Person` 클래스를 정의합니다. 
2. 인스턴스 속성은 문자열 `name` 과 정수 `age`입니다. 두 속성 모두 생성자 함수에서 설정합니다.
3. 인스턴스간 `age`의 대/소비교가 가능해야합니다.
4.  `__gt__`메서드와 `__eq__`메서드를 활용합니다.


```python
# 아래 셀의 코드가 정상적으로 동작하도록 Person클래스를 정의해봅시다.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __gt__(self,other):
        return self.age > other.age
    
    def __eq__(self,other):
        return self.age == other.age
```


```python
p1 = Person('1', 1)
p2 = Person('2', 2)
p3 = Person('3', 1)

print(p1 > p2)
print(p1 == p3)
print(p1 == p2)
```

    False
    True
    False
    

# 클래스 (class)

> `class`: 객체들의 분류(class)를 정의할 때 쓰이는 키워드


## 클래스(Class) 생성

* 클래스 생성은 `class` 키워드와 정의하고자 하는 `<클래스의 이름>`으로 가능합니다.

* `<클래스의 이름>`은 `PascalCase`로 정의합니다.

* 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 데이터는 **속성(attribute)** 정의된 함수는 **메서드(method)**로 부릅니다.

---

**활용법**

```python
class <클래스이름>:
    <statement>
```

```python
class ClassName:
    statement
```


```python
# Person 이라는 이름의 class를 정의해봅시다. 
# 아래와 같이 """(docstring)을 통해 클래스에 대한 설명(doc)도 함께 정의해 봅시다.
```

```python
class ClassName:
    """
    이것은 ClassName 클래스입니다.
    """
```


```python
# Person 클래스를 docstring과 함께 정의해 봅시다.
class Person:
    """
    이것은 Person 클래스(class)입니다.
    """
```


```python
# 앞서 정의한 Person 클래스의 docstring을 출력해봅시다.
help(Person)
```

    Help on class Person in module __main__:
    
    class Person(builtins.object)
     |  이것은 Person 클래스(class)입니다.
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    

## 클래스 변수
* 클래스의 속성(attribute)
* 모든 인스턴스가 공유
* 클래스 선언 내부에서 정의
* `클래스.변수명`으로 접근 및 할당

---

**활용법**
```python
class Circle:
    pi = 3.14
    
print(Circle.pi)
```


```python
# 위의 예시 코드대로 Circle 클래스를 생성해봅시다.

class Circle:
    pi = 3.14
    
print(Circle.pi)
```

    3.14
    


```python
# Circle 클래스의 인스턴스 c1, c2를 생성해봅시다.

c1 = Circle()
c2 = Circle()
```


```python
print(c1.pi)
print(c1.pi)
```

    3.14
    3.14
    


```python
# 클래스 변수 pi에 접근해봅시다.

Circle.pi = 3
```


```python
# 인스턴스 c1, c2에서 pi 값을 출력해봅시다.

print(c1.pi)
print(c2.pi)
```

    3
    3
    


```python
# c1의 pi 값을 3.141592로 변경하여 봅시다.

c1.pi = 3.141592
```


```python
# c1, c2에서의 pi값을 각각 출력해봅시다.

print(c1.pi)
print(c2.pi)
```

    3.141592
    3
    


```python
# Circle의 pi를 출력해봅시다.

print(Circle.pi)
```

    3
    

## 클래스 메서드(class method)
* 클래스가 사용할 메서드에 해당합니다.
* `@classmethod` 데코레이터를 사용하여 정의합니다.
* **메서드 호출시, 첫 번째 인자로 클래스 `cls`가 전달됩니다**

---

**활용법**

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        ...

# 자동으로 첫 번째 인자로 클래스(MyClass)가 들어갑니다.
MyClass.class_method(.., ..)  
```

## 스태틱 메서드(static method)
* 클래스가 사용할 메서드에 해당합니다.
* 인스턴스와 클래스의 속성과 무관한 메서드입니다.
* `@staticmethod` 데코레이터를 사용하여 정의합니다.
* **호출시, 어떠한 인자도 전달되지 않습니다**
* 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용합니다.


---

**활용법**

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
        ...

MyClass.static_method(.., ..)
```


```python
# MyClass 클래스를 정의해 두었습니다.

class MyClass:
    
    def instance_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls
    
    @staticmethod
    def static_method(arg):
        return arg
```


```python
# MyClass 클래스의 인스턴스 mc를 생성해봅시다.

mc = MyClass()
```


```python
# 인스턴스 메서드를 호출하여 반환된 결과(self)와 인스턴스(mc)를 비교해봅시다.
# 1. id를 출력해 보고, 같은 id인지 확인
# 2. == 연산자를 확인해 비교

print(id(mc.instance_method()))
print(id(mc))
```

    1264513104144
    1264513104144
    


```python
# 클래스 메서드를 호출하여 반환된 결과(cls)와 인스턴스(mc)를 비교해봅시다.
# 1. id를 출력해 보고, 같은 id인지 확인
# 2. == 연산자를 확인해 비교

print(id(mc.class_method()))
print(id(mc))
```

    1264495559344
    1264513104144
    


```python
# 스태틱 메서드를 호출하고 반환된 결과(arg)를 확인해봅시다.
# 인스턴스 메서드, 클래스 메서드처럼 자동으로 전달되는 인자가 없습니다.

print(id(mc.static_method()))
print(id(mc))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [112], in <cell line: 4>()
          1 # 스태틱 메서드를 호출하고 반환된 결과(arg)를 확인해봅시다.
          2 # 인스턴스 메서드, 클래스 메서드처럼 자동으로 전달되는 인자가 없습니다.
    ----> 4 print(id(mc.static_method()))
          5 print(id(mc))
    

    TypeError: static_method() missing 1 required positional argument: 'arg'


## 인스턴스와 클래스 간의 이름 공간 (namespace)

* 클래스를 정의하면 클래스와 해당하는 이름 공간이 생성됩니다.
* 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간이 생성됩니다.
* 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색합니다.


```python
# 먼저 아래 코드에 대한 이름 공간을 확인해봅시다.

class Person:
    species = 'human'
    
    def __init__(self, name):
        self.name = name 
        
p1 = Person('Hong')
p2 = Person('Choi')
```


```python
# 아래 셀을 실행하여 이름 공간(namespace) 구성을 시각적으로 확인해보세요.
# 클래스를 위한 이름 공간 그리고 인스턴스별로 이름 공간이 따로 구성되는 점에 주목하세요.
```


```python
%%html
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=class%20Person%3A%0A%20%20%20%20species%20%3D%20'human'%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20name%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20name%20%0A%20%20%20%20%20%20%20%20%0Ap1%20%3D%20Person%28'Hong'%29%0Ap2%20%3D%20Person%28'Choi'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=9&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```


<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=class%20Person%3A%0A%20%20%20%20species%20%3D%20'human'%0A%20%20%20%20%0A%20%20%20%20def%20__init__%28self,%20name%29%3A%0A%20%20%20%20%20%20%20%20self.name%20%3D%20name%20%0A%20%20%20%20%20%20%20%20%0Ap1%20%3D%20Person%28'Hong'%29%0Ap2%20%3D%20Person%28'Choi'%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=9&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>




```python
# Person 클래스를 재정의하여 다른 예시로 살펴봅시다.
class Person:
    name = 'unknown'
    
    def talk(self):
        print(self.name)
        
p1 = Person()
p1.talk()

p2 = Person()
p2.talk()
p2.name = 'Kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)
```

    unknown
    unknown
    Kim
    unknown
    unknown
    Kim
    


```python
# p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수가 unknown으로 출력됩니다.


```


```python
# p2 인스턴스 변수 name을 다른 값으로 설정해봅시다.


```


```python
# Person 클래스의 값이 Kim으로 변경된 것이 아니므로
# p2 인스턴스의 이름 공간에 name이 Kim으로 저장됩니다.


```


```python
# 아래 셀을 실행하여 시각적으로 위의 설명을 시각적으로 살펴봅시다.
```


```python
%%html
<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=class%20Person%3A%0A%20%20%20%20name%20%3D%20'unknown'%0A%20%20%20%20%0A%20%20%20%20def%20talk%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28self.name%29%0A%20%20%20%20%20%20%20%20%0Ap2%20%3D%20Person%28%29%0Ap2.talk%28%29%0Ap2.name%20%3D%20'kim'%0Ap2.talk%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=8&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
```


<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=class%20Person%3A%0A%20%20%20%20name%20%3D%20'unknown'%0A%20%20%20%20%0A%20%20%20%20def%20talk%28self%29%3A%0A%20%20%20%20%20%20%20%20print%28self.name%29%0A%20%20%20%20%20%20%20%20%0Ap2%20%3D%20Person%28%29%0Ap2.talk%28%29%0Ap2.name%20%3D%20'kim'%0Ap2.talk%28%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=8&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>



# 비교 정리

### 인스턴스와 메서드
- 인스턴스는 3가지 메서드(인스턴스, 클래스, 정적 메서드) 모두에 접근할 수 있습니다.
    - 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않습니다. (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계합니다.



```python
# MyClass를 활용하여 살펴봅시다.

class MyClass:
    def instance_method(self):
        return 'instance_method', self
    
    @classmethod
    def class_method(cls):
        return 'class_method', cls
    
    @staticmethod
    def static_method():
        return 'static method'
```


```python
# MyClass의 인스턴스를 만들고 mc 변수에 저장합시다.

mc = MyClass()
```


```python
# 인스턴스에서 인스턴스 메서드를 호출하고 결과를 확인해봅시다.

mc.instance_method()
```




    ('instance_method', <__main__.MyClass at 0x1266ad84df0>)




```python
# 인스턴스에서 클래스 메서드를 호출하고 결과를 확인해봅시다.

mc.class_method()
```




    ('class_method', __main__.MyClass)




```python
# 인스턴스에서 스태틱 메서드를 호출하고 결과를 확인해봅시다.

mc.static_method()
```




    'static method'



### 클래스와 메서드
- 클래스는 3가지 메서드(인스턴스, 클래스, 정적 메서드) 모두에 접근할 수 있습니다.
    - 클래스에서 인스턴스 메서드는 호출하지 않습니다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계합니다. (클래스 메서드와 정적 메서드)
    - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의합니다.
    - 클래스와 클래스 속성에 접근할 필요가 없다면 **정적 메서드**로 정의합니다.
        - 정적 메서드는 `cls`, `self`와 같이 묵시적인 첫번째 인자를 받지 않기 때문입니다.


```python
# 클래스에서 인스턴스 메서드를 호출하면 오류가 발생합니다.
# 실행시켜 오류를 확인해봅시다.

MyClass.instance_method(mc)
```




    ('instance_method', <__main__.MyClass at 0x1266ad84df0>)




```python
# 클래스에서 인스턴스 메서드를 그냥 호출하면 'self'가 넘어가지 않기 때문에 오류가 발생합니다.
# 실행시켜 오류를 확인해봅시다.

instance_method()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [140], in <cell line: 4>()
          1 # 클래스에서 인스턴스 메서드를 그냥 호출하면 'self'가 넘어가지 않기 때문에 오류가 발생합니다.
          2 # 실행시켜 오류를 확인해봅시다.
    ----> 4 instance_method()
    

    NameError: name 'instance_method' is not defined



```python
# 클래스에서 클래스 메서드를 호출하고 결과를 확인해봅시다.

MyClass.class_method()
```




    ('class_method', __main__.MyClass)



# OOP의 핵심 개념

- 추상화 (Abstraction)
- 상속 (Inheritance)
- 다형성 (Polymorphism)
- 캡슐화 (Encapsulation)

## 추상화(Abstraction)란?

- 객체 지향 프로그래밍에서의 추상화는 세부적인 내용은 감추고 필수적인 부분만 표현하는 것을 뜻합니다.
- 현실 세계를 프로그램 설계에 반영하기 위해 사용됩니다.
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성하여 활용합니다.


```python
# 학생(Student)을 표현하기 위한 클래스를 생성합니다.

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
    def study(self):
        self.gpa += 0.1
```


```python
# 교수(Professor)를 표현하기 위한 클래스를 생성합니다.

class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
    def study(self):
        self.age += 1
```


```python
# 학생 클래스와 교수 클래스의 공통 속성과 행위(메서드)를 추출하여, 
# Person이라는 클래스를 통해 추상화를 해봅시다.

class Person:
    def __init(self, name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
```

## 상속(Inheritance)이란?


클래스에서 가장 큰 특징은 `상속`이 가능하다는 것입니다. 

부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드 재사용성이 높아집니다.

---

**활용법**


```python
class ChildClass(ParentClass):
    <code block>
```


```python
# Person 클래스를 정의해 보겠습니다.

class Person:
    population = 0
    
    def __init__(self, name='사람'):
        self.name = name
        Person.population += 1
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
```


```python
# Person 클래스의 인스턴스 p1을 생성해봅시다.
# name 속성은 자유롭게 설정합니다.

p1 = Person('john')
```


```python
# Person 클래스를 상속받아 Student 클래스를 만들어 보겠습니다.

class Student(Person):
    def __init__(self, student_id, name='학생'):
        self.name = name
        self.student_id = student_id  
        Person.population += 1
```


```python
# Student 클래스의 객체 s1을 만들어봅시다.

s1 = Student('john')
```


```python
# s1의 name과 student_id를 확인해봅시다.

print(s1.name)
print(s1.student_id)
```

    학생
    john
    


```python
# 자식 클래스의 인스턴스는 부모 클래스에 정의된 메서드를 호출 할 수 있습니다.
# talk 메서드를 호출해봅시다.

s1.talk()
```

    반갑습니다. 학생입니다.
    

이처럼 상속은 공통된 속성이나 메서드를 부모 클래스에 정의하고, 이를 상속받아 다양한 형태의 사람들을 만들 수 있습니다.

### `issubclass(class, classinfo)`

* class가 classinfo의 subclass인 경우 `True`를 반환합니다.

### `isinstance(object, classinfo)`

* object가 classinfo의 인스턴스거나 subclass인 경우 `True`를 반환합니다.


```python
# issubclass 함수를 통해 Student 클래스와 Person 클래스가 상속관계인지 확인해봅시다. (클래스 상속 검사)
# issubclass(자식클래스, 부모클래스)

issubclass(Student, Person)
```




    True




```python
# isinstance 함수를 통해
# s1이 Student 클래스의 인스턴스인지, s1이 Person 클래스의 인스턴스인지 모두 확인해봅시다.
# isinstance(인스턴스, 클래스)

print(isinstance(s1,Student))
print(isinstance(s1,Person))
```

    True
    True
    


```python
# 내장 자료형들도 아래와 같이 상속 관계가 있습니다.
# 아래 셀을 실행시켜 확인해봅시다.
```


```python
print(issubclass(bool, int)) # True
```

    True
    


```python
print(issubclass(float, int)) # False
```

    False
    

### `super()`

* 자식 클래스에 메서드를 추가로 구현할 수 있습니다.

* 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있습니다.

---

**활용법**


```python
class ChildClass(ParentClass):
    def method(self, arg):
        super().method(arg) 
```


```python
# Person 클래스와 Student 클래스를 함께 정의해 보겠습니다.

class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def greeting(self):
        print(f'안녕, {self.name}')
      
    
class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        self.student_id = student_id
        
p1 = Person('홍교수', 200, '0101231234', 'hong@gildong')
s1 = Student('학생', 20, '12312312', 'student@naver.com', '190000')
```


```python
# p1과 s1 모두 greeting 메서드를 호출해봅시다.


p1.greeting()
s1.greeting()
```

    안녕, 홍교수
    안녕, 학생
    

위의 코드는 상속을 했음에도 불구하고 초기화(`__init__`)에서 동일한 코드가 반복됩니다. 

초기화의 중복을 `super()` 함수를 통해 제거해봅시다.


```python
# Person과 Student를 처음부터 재정의해봅시다.

```

## 다형성(Polymorphism)이란?

- 여러 모양을 뜻하는 그리스어로, 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 뜻합니다.
- 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 각기 다른 방식으로 응답될 수 있습니다.

### 메서드 오버라이딩
> Method Overriding(메서드 오버라이딩): 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것

* 상속 받은 메서드를 `재정의`할 수도 있습니다. 
* 상속 받은 클래스에서 **같은 이름의 메서드**로 덮어씁니다.
* `__init__`, `__str__`의 메서드를 정의하는 것 역시, 메서드 오버라이딩입니다.


```python
# 아래 Person 클래스를 이용하여 메서드 오버라이딩을 해보겠습니다.

class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def talk(self):
        print(f'안녕, {self.name}')
```


```python
# 위의 Person 클래스를 상속 받아 군인답게 말하는 Soldier 클래스를 만들어봅시다.
# talk 메서드를 재정의(override)합니다.

class Soldier(Person):
    def talk(self):
        print(f'통신보안 대위 {self.name}입니다')
```


```python
# Person 클래스의 인스턴스 p를 만들어서 talk 메서드를 실행해보세요.


p = Person('유시진','30','010-4444-4444','special_force@gamil.com')
p.talk()
```

    안녕, 유시진
    


```python
# Soldier 클래스의 인스턴스 s를 만들어서 talk 메서드를 실행해보세요.

s = Soldier('유시진','30','010-4444-4444','special_force@gamil.com')
s.talk()
```

    통신보안 대위 유시진입니다
    

### [연습] Person & Animal (메서드 오버라이딩)

> 사실 사람은 포유류입니다. 
>
> Animal Class를 만들고, Person Class 가 상속받도록 구성해봅시다.
>
> (변수나, 메서드는 자유롭게 만들어보세요.)

```
예시) 
모든 동물은 이름이 있고, 사람은 이름과 이메일이 있습니다.
모든 동물은 talk 메서드가 있습니다. 
동물은 '으르렁'하고, 사람은 '안녕'합니다.
```



```python
# 아래에 코드를 작성해주세요.

class Animal:
    def __init__(self,name):
        self.name = name
        
    def talk(self):
        print('으르렁')
        
class Person(Animal):
    def __init__(self,name,email):
        super().__init__(name)
        self.email = email
        
    def talk(self):
        print('안녕')
        
a = Animal('곰')
p = Person('john','ddd@sss.ccc')
print(a.name)
print(p.name,p.email)
a.talk()
p.talk()
```

    곰
    john ddd@sss.ccc
    으르렁
    안녕
    

## 캡슐화(Encapsulation)란?

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단하는 것을 말합니다.
  - 예시: 주민등록번호
  
- 다른 언어와 달리 파이썬에서 캡슐화는 암묵적으로는 존재하지만, 언어적으로는 존재하지 않습니다.

---

**접근제어자의 종류**
- Public Access Modifier
- Protected Access Modifier
- Private Access Modifier

### Publie Member

- 언더바가 없이 시작하는 메서드나 속성들이 이에 해당합니다.
- 어디서나 호출 가능합니다.
- 하위 클래스에서 메서드 오버라이딩을 허용합니다.
- 일반적으로 작성되는 메서드와 속성의 대다수를 차지합니다.


```python
# 아래 간단한 Person 클래스가 정의되어 있습니다.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = 30
```


```python
# Person 클래스의 인스턴스인 p1은 이름(name)과 나이(age) 모두 접근 가능합니다.

p1 = Person('김싸피', 30)
print(p1.name)
print(p1.age)
```

    김싸피
    30
    

### Protected Member

- 언더바 1개로 시작하는 메서드나 속성들이 이에 해당합니다.
- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능합니다.
- 하위 클래스에서 메서드 오버라이딩을 허용합니다.


```python
# Person 클래스를 재정의해봅시다.
# 실제 나이(age)에 해당하는 값을 언더바 한 개를 붙여서 Protected Member로 지정하였습니다.

class Person:
    
    def __init__(self,age):
        self._age = age
    
    def get_age(self):
        return self._age
```


```python
# 인스턴스를 만들고 get_age 메서드를 활용하여 호출할 수 있습니다.

a = Person(26)
print(a.get_age())
```

    26
    


```python
# _age에 직접 접근하여도 확인이 가능합니다.
# 파이썬에서는 암묵적으로 활용됩니다.

print(a._age)
```

    26
    

### Private Member

- 언더바 2개로 시작하는 메서드나 속성들이 이에 해당합니다.
- 본 클래스 내부에서만 사용이 가능합니다.
- 하위 클래스 상속 및 호출이 불가능합니다.
- 외부 호출이 불가능합니다.


```python
# Person 클래스를 다시 재정의해봅시다.
# 실제 나이(age)에 해당하는 값을 언더바 두 개를 붙여서 Private Member로 지정하였습니다.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self): 
        return self.__age
```


```python
# 인스턴스를 만들고 get_age 메서드를 활용하여 호출할 수 있습니다.
# 실행시켜 확인해봅시다.

p1 = Person('김싸피', 30)
p1.get_age()
```




    30




```python
# __age에 직접 접근이 불가능합니다.

p1.__age
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Input In [200], in <cell line: 3>()
          1 # __age에 직접 접근이 불가능합니다.
    ----> 3 p1.__age
    

    AttributeError: 'Person' object has no attribute '__age'


### `getter` 메서드와 `setter` 메서드

변수에 접근할 수 있는 메서드를 별도로 생성할 수 있습니다.

- `getter` 메서드: 변수의 값을 읽는 메서드입니다.
  - `@property` 데코레이터를 사용합니다.
- `setter` 메서드: 변수의 값을 설정하는 성격의 메서드입니다.
  - `@변수.setter`를 사용합니다.


```python
class Person:
    
    def __init__(self, age):
        self._age = age 
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For SSAFY')
            return
        
        self._age = new_age
```


```python
# Person의 인스턴스를 만들어서 나이에 접근하면 정상적으로 출력됩니다.
# 실행시켜 확인해보세요.

p1 = Person(20)
print(p1.age)
```

    20
    


```python
# p1 인스턴스의 나이를 다른 값으로 바꿔도 정상적으로 반영됩니다.
# 실행시켜 확인해보세요.

p1.age = 33
print(p1.age)
```

    33
    


```python
# setter 함수에는 "나이가 19살 이하면 안된다는" 조건문이 하나 작성되어 있습니다.
# 따라서 나이를 19살 이하인 값으로 변경하게 되면 오류가 발생합니다.
# 실행시켜 확인해보세요.

p1.age = 19
print(p1.age)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [206], in <cell line: 5>()
          1 # setter 함수에는 "나이가 19살 이하면 안된다는" 조건문이 하나 작성되어 있습니다.
          2 # 따라서 나이를 19살 이하인 값으로 변경하게 되면 오류가 발생합니다.
          3 # 실행시켜 확인해보세요.
    ----> 5 p1.age = 19
          6 print(p1.age)
    

    Input In [201], in Person.age(self, new_age)
         10 @age.setter
         11 def age(self, new_age):
         12     if new_age <= 19:
    ---> 13         raise ValueError('Too Young For SSAFY')
         14         return
         16     self._age = new_age
    

    ValueError: Too Young For SSAFY


### 다중 상속
* 두개 이상의 클래스를 상속받는 경우, 다중 상속이 됩니다.
    * 상속 받은 모든 클래스의 요소를 활용 가능
    * 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정



```python
# Person 클래스를 정의합니다.
# Person 클래스는 생성자에서 인스턴스 변수로 name을 설정합니다.

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'
```


```python
# Mom 클래스를 정의합니다.
# Mom 클래스는 Person 클래스를 상속받으며, 클래스 변수로 gene을 갖습니다. 값은 'XX'입니다.
# Mom 클래스만의 인스턴스 메서드 swim을 자유롭게 정의해봅시다.

class Mom(Person):
    gene = 'XX'
    
    def swim(self):
        return '엄마가 수영'
```


```python
# Dad 클래스를 정의합니다.
# Dad 클래스는 Person 클래스를 상속받으며, 클래스 변수로 gene을 갖습니다. 값은 'XY'입니다.
# Dad 클래스만의 인스턴스 메서드 walk를 자유롭게 정의해봅시다.

class Dad(Person):
    gene = 'XY'
    
    def walk(self):
        return '아빠가 걷기'
```


```python
# FirstChild 클래스를 정의합니다. 
# 상속의 순서가 중요합니다.(Dad, Mom) 순서로 상속받아봅시다.
# 상속받은 swim 메서드를 재정의(override)해봅시다.
# FirstChild 클래스만의 인스턴스 메서드 cry를 자유롭게 정의해봅시다.

class FirstChild(Dad,Mom):
    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    




```


```python
# FirstChild 클래스의 인스턴스 baby1을 생성해봅시다.

baby1 = FirstChild('아가')
```


```python
# baby1의 cry 메서드를 실행해봅시다.

print(baby1.cry())
```

    첫째가 응애
    


```python
# baby1의 swim 메서드를 실행해봅시다.

print(baby1.swim())
```

    첫째가 수영
    


```python
# baby1의 walk 메서드를 실행해봅시다.

print(baby1.walk())
```

    아빠가 걷기
    


```python
# baby1의 gene 속성은 어떤 부모클래스의 속성값을 상속받는지 확인해봅시다.

print(baby1.gene)
```

    XY
    


```python
# 이번에는 SecondChild 클래스를 만들어 상속 순서를 바꿔봅시다.
# (Mom, Dad) 순서로 상속받아봅시다.
# 상속받은 walk 메서드를 재정의(override)해봅시다.
# SecondChild 클래스만의 인스턴스 메서드 cry를 자유롭게 정의해봅시다.

class SecondChild(Mom, Dad):
    def walk(self):
        return '둘째가 걷기'
    
    def cry(self):
        return '둘째가 응애'
```


```python
# SecondChild의 인스턴스 baby2를 생성합니다.

baby2 = SecondChild('아가')
```


```python
# baby2의 cry 메서드를 실행합니다.

print(baby2.cry())
```

    둘째가 응애
    


```python
# baby2의 walk 메서드를 실행합니다.

print(baby2.walk())
```

    둘째가 걷기
    


```python
# baby2의 swim 메서드를 실행합니다.

print(baby2.swim())
```

    엄마가 수영
    


```python
# baby2의 gene 속성은 어떤 부모클래스의 속성값을 상속받는지 확인해봅시다.

print(baby2.gene)
```

    XX
    

### 상속관계에서의 이름 공간과 MRO (Method Resolution Order)

- 기존의 `인스턴스 -> 클래스` 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장됩니다.
    * 인스턴스 -> 자식 클래스 -> 부모 클래스
    
- MRO는 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 속성 또는 메서드입니다.

---

**활용법**


```python
ClassName.__mro__

# 또는
ClassName.mro()
```


```python
# Mom, Dad 클래스를 정의해 보겠습니다.

class Mom:
    def walk(self):
        print('사뿐사뿐')
        
        
class Dad:
    def walk(self):
        print('저벅저벅')
```


```python
# Mom, Dad 클래스를 활용하여 Daughter, Son 클래스를 정의합니다.

class Daughter(Mom, Dad):
    pass


class Son(Dad, Mom):
    pass
```


```python
# Daugher, Son 클래스의 인스턴스를 생성합니다.
# 각각의 인스턴스에서 메서드를 호출하고 결과가 어떻게 나오는지 확인합니다.
# 아래 코드를 실행해시켜보세요.

d = Daughter()
s = Son()

d.walk()
s.walk()
```

    사뿐사뿐
    저벅저벅
    


```python
# Daughter 클래스의 mro 속성을 이용하여 확인해봅시다.

print(Daughter.__mro__)
```

    (<class '__main__.Daughter'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class 'object'>)
    


```python
# Son 클래스의 mro 속성을 이용하여 확인해봅시다.

print(Son.__mro__)
```

    (<class '__main__.Son'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class 'object'>)
    
