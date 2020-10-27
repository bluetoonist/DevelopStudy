# Python for Speed
```
Refer Link : https://pybit.es/faster-python.html
```

## 1. Know the basic data structuresy 
```
- 파이썬에서 사용중인 자료구조에서 이미 잘 정의된 기본적인 것들을 사용하는 것들이
성능을 올리는 것에 중요한 도움이 될 수 있음
- 아래의 링크에서는 시간 복잡도를 줄이기 위해 참조할 수 있는 링크
Time Complexity  : https://wiki.python.org/moin/TimeComplexity
```

## 2. Reduce memory footprint
```
[BAD CASE]
msg = 'line1\n'
msg += 'line2\n'
msg += 'line3\n'

[Consideration]
msg = ['line1', 'line2', 'line3']
'\n'.join(msg)
```
```
위와 같은 코드는 각 라인마다 새 문자열이 생성되기 때문에 비효율적, 따라서 리스트를 이용하고 join 함수를 통해 생성 하는 패턴을 고려
```

```
# slow
msg = 'hello ' + my_var + ' world'

# faster
msg = 'hello %s world' % my_var

# or better:
msg = 'hello {} world'.format(my_var)
```
```
비슷한 예제로 '+' 연산자를 사용하여 문자열을 결합하는 경우도 해당, f-strings 를 사용하여 문자열 처리를 하는 것이 성능 향상에 도움이 됨
```
```
[BAD CASE]       if variable == true:
[Consideration]  if variable:
```
```
Pythonic Code는 가독성이 높을 뿐만 아니라 더 빠름
```

## 3. Use builtin functions and libraries
```
[BAD CASE]
newlist = []
for word in oldlist:
    newlist.append(word.upper())

[Consideration]
newlist = map(str.upper, oldlist)  # wiki cites map as a for loop moved into C code
```
```
sum, max, any, map 등과 같은 Built-in 함수는 C로 구현 됨, 매우 효율적
```

```
Pythonic의 효율적인 데이터 구조 (deque, defaultdict, Counter 등)를 제공하는 collections 모듈
```

## 4. Move calculations outside the loop
```
[BAD CASE]
for i in big_it:
    m = re.search(r'\d{2}-\d{2}-\d{4}', i)
    if m:

[Consideration]
date_regex = re.compile(r'\d{2}-\d{2}-\d{4}')

for i in big_it:
    m = date_regex.search(i)
    if m:
```
```
정규 표현식을 이용할 경우 캐시(Cached) 된 데이터를 사용하여 loop를 이용할 것 
```