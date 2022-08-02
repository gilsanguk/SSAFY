### 1. 평균 점수 구하기

```python
def get_dict_avg(dct):
    return sum(dct.values())/len(dct)

print(get_dict_avg({'python':80,'web':83,'algorithm':90,'django':89}))
```

### 2. 혈액형 분류하기

```python
def count_blood(bloods):
    dct={}
    for blood in bloods:
    # 1
        if blood in dct:
            dct[blood] += 1
        else:
            dct[blood] = 1
    return dct
    # 2
    blood_dict[blood] = blood_dict.get(blood,0) + 1

print(count_blood(['A','B','A','O','AB','AB','O','A','B','O','B','AB',]))
```

