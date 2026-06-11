# Python3 Dict 详细用法

## 1. 什么是字典 (Dictionary)

字典是 Python 中的**键值对(key-value)**映射集合,用花括号 `{}` 表示。

### 特点对比

| 特性 | 列表 List | 元组 Tuple | 集合 Set | 字典 Dict |
|------|----------|-----------|---------|----------|
| 符号 | `[]` | `()` | `{}` | `{}` |
| 可变性 | ✅ 可变 | ❌ 不可变 | ✅ 可变 | ✅ 可变 |
| 有序性 | ✅ 有序 | ✅ 有序 | ❌ 无序 | ✅ 有序(3.7+) |
| 重复元素 | ✅ 允许 | ✅ 允许 | ❌ 不允许 | ❌ 键不重复 |
| 访问方式 | 索引 | 索引 | 遍历 | 键 |
| 用途 | 序列数据 | 固定数据 | 去重/集合运算 | 键值映射 |

```python
# 列表 - 通过索引访问
my_list = ['apple', 'banana', 'cherry']
print(my_list[0])  # 'apple'

# 字典 - 通过键访问
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(my_dict['name'])  # 'Alice'
```

---

## 2. 创建字典

### 2.1 使用花括号

```python
# 基本创建
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 空字典
empty = {}
print(type(empty))  # <class 'dict'>

# 不同类型的值
mixed = {
    'name': 'Bob',
    'age': 30,
    'scores': [85, 90, 95],
    'address': {'city': 'Shanghai', 'street': 'Nanjing Rd'}
}

# 键可以是不同类型(但必须可哈希)
d = {
    'string_key': 1,
    42: 'number_key',
    (1, 2): 'tuple_key'
}
```

### 2.2 使用 dict() 函数

```python
# 从键值对列表创建
d = dict([('name', 'Alice'), ('age', 25)])
print(d)  # {'name': 'Alice', 'age': 25}

# 使用关键字参数
d = dict(name='Alice', age=25, city='Beijing')
print(d)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 从两个列表创建
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Beijing']
d = dict(zip(keys, values))
print(d)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 空字典
empty = dict()
print(empty)  # {}
```

### 2.3 使用 dict.fromkeys()

```python
# 创建具有相同值的字典
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}

# 默认值为 None
d = dict.fromkeys(keys)
print(d)  # {'a': None, 'b': None, 'c': None}

# 注意:可变对象作为默认值的陷阱
d = dict.fromkeys(['a', 'b'], [])
d['a'].append(1)
print(d)  # {'a': [1], 'b': [1]} ← 共享同一个列表!
```

### 2.4 字典推导式

```python
# 基本推导式
d = {x: x**2 for x in range(5)}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 带条件
d = {x: x**2 for x in range(10) if x % 2 == 0}
print(d)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 从列表创建
words = ['apple', 'banana', 'cherry']
d = {word: len(word) for word in words}
print(d)  # {'apple': 5, 'banana': 6, 'cherry': 6}

# 键值转换
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## 3. 访问字典元素

### 3.1 使用方括号 []

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 访问存在的键
print(person['name'])  # 'Alice'
print(person['age'])   # 25

# 访问不存在的键会报错
try:
    print(person['phone'])
except KeyError as e:
    print(f"键不存在: {e}")  # 键不存在: 'phone'
```

### 3.2 使用 get() 方法(推荐)

```python
person = {'name': 'Alice', 'age': 25}

# 访问存在的键
print(person.get('name'))  # 'Alice'

# 访问不存在的键返回 None
print(person.get('phone'))  # None

# 指定默认值
print(person.get('phone', 'N/A'))  # 'N/A'
print(person.get('age', 0))  # 25 (键存在,返回实际值)
```

### 3.3 检查键是否存在

```python
person = {'name': 'Alice', 'age': 25}

# in 运算符
print('name' in person)   # True
print('phone' in person)  # False

# not in 运算符
print('phone' not in person)  # True

# 先检查再访问
if 'phone' in person:
    print(person['phone'])
else:
    print('电话号码不存在')
```

---

## 4. 修改字典

### 4.1 添加/修改元素

```python
person = {'name': 'Alice', 'age': 25}

# 添加新键值对
person['city'] = 'Beijing'
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 修改已存在的键
person['age'] = 26
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'Beijing'}

# 批量添加/修改
person['phone'] = '123-4567'
person['email'] = 'alice@example.com'
print(person)
```

### 4.2 update() - 批量更新

```python
person = {'name': 'Alice', 'age': 25}

# 使用字典更新
person.update({'city': 'Beijing', 'age': 26})
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'Beijing'}

# 使用关键字参数
person.update(phone='123-4567', email='alice@example.com')
print(person)

# 使用键值对列表
person.update([('country', 'China'), ('job', 'Engineer')])
print(person)
```

### 4.3 setdefault() - 设置默认值

```python
person = {'name': 'Alice', 'age': 25}

# 键不存在时设置默认值并返回
city = person.setdefault('city', 'Beijing')
print(city)    # 'Beijing'
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 键存在时返回现有值,不修改
age = person.setdefault('age', 30)
print(age)     # 25 (不是30)
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 常用于累加计数
word_count = {}
words = ['apple', 'banana', 'apple', 'cherry', 'banana']
for word in words:
    word_count[word] = word_count.setdefault(word, 0) + 1
print(word_count)  # {'apple': 2, 'banana': 2, 'cherry': 1}
```

---

## 5. 删除字典元素

### 5.1 del 语句

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 删除指定键
del person['age']
print(person)  # {'name': 'Alice', 'city': 'Beijing'}

# 删除不存在的键会报错
try:
    del person['phone']
except KeyError:
    print('键不存在')

# 删除整个字典
# del person
# print(person)  # NameError
```

### 5.2 pop() - 删除并返回值

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 删除并返回值
age = person.pop('age')
print(age)     # 25
print(person)  # {'name': 'Alice', 'city': 'Beijing'}

# 键不存在时返回默认值
phone = person.pop('phone', 'N/A')
print(phone)  # 'N/A'

# 键不存在且无默认值会报错
try:
    person.pop('email')
except KeyError:
    print('键不存在')
```

### 5.3 popitem() - 删除并返回最后一个键值对

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 删除并返回最后一个键值对(Python 3.7+按插入顺序)
item = person.popitem()
print(item)    # ('city', 'Beijing')
print(person)  # {'name': 'Alice', 'age': 25}

# 空字典会报错
try:
    empty = {}
    empty.popitem()
except KeyError:
    print('字典为空')
```

### 5.4 clear() - 清空字典

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

person.clear()
print(person)  # {}
print(len(person))  # 0
```

---

## 6. 字典的视图对象

### 6.1 keys() - 获取所有键

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 获取键视图
keys = person.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])
print(type(keys))  # <class 'dict_keys'>

# 转换为列表
keys_list = list(keys)
print(keys_list)  # ['name', 'age', 'city']

# 遍历
for key in person.keys():
    print(key, end=' ')  # name age city
print()

# 简写(直接遍历字典)
for key in person:
    print(key, end=' ')  # name age city
```

### 6.2 values() - 获取所有值

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 获取值视图
values = person.values()
print(values)  # dict_values(['Alice', 25, 'Beijing'])

# 转换为列表
values_list = list(values)
print(values_list)  # ['Alice', 25, 'Beijing']

# 遍历
for value in person.values():
    print(value, end=' ')  # Alice 25 Beijing
print()

# 检查值是否存在
print('Alice' in person.values())  # True
```

### 6.3 items() - 获取所有键值对

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 获取键值对视图
items = person.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Beijing')])

# 转换为列表
items_list = list(items)
print(items_list)  # [('name', 'Alice'), ('age', 25), ('city', 'Beijing')]

# 遍历(最常用)
for key, value in person.items():
    print(f"{key}: {value}")

# 输出:
# name: Alice
# age: 25
# city: Beijing
```

### 6.4 视图对象的动态性

```python
person = {'name': 'Alice', 'age': 25}

# 获取视图
keys = person.keys()
print(keys)  # dict_keys(['name', 'age'])

# 修改字典
person['city'] = 'Beijing'

# 视图自动更新
print(keys)  # dict_keys(['name', 'age', 'city'])
```

---

## 7. 字典的遍历

### 7.1 遍历键

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 方法1: 直接遍历
for key in person:
    print(key)

# 方法2: 使用 keys()
for key in person.keys():
    print(key)

# 方法3: 遍历键并访问值
for key in person:
    print(f"{key}: {person[key]}")
```

### 7.2 遍历值

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

for value in person.values():
    print(value)
```

### 7.3 遍历键值对(推荐)

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

for key, value in person.items():
    print(f"{key}: {value}")
```

### 7.4 带索引遍历

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

for i, (key, value) in enumerate(person.items()):
    print(f"{i}: {key} = {value}")

# 输出:
# 0: name = Alice
# 1: age = 25
# 2: city = Beijing
```

---

## 8. 字典的排序

### 8.1 按键排序

```python
d = {'c': 3, 'a': 1, 'b': 2}

# 按键排序(返回列表)
sorted_keys = sorted(d.keys())
print(sorted_keys)  # ['a', 'b', 'c']

# 创建排序后的字典
sorted_dict = {k: d[k] for k in sorted(d.keys())}
print(sorted_dict)  # {'a': 1, 'b': 2, 'c': 3}

# 或使用 dict()
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)  # {'a': 1, 'b': 2, 'c': 3}
```

### 8.2 按值排序

```python
d = {'apple': 3, 'banana': 1, 'cherry': 2}

# 按值排序
sorted_items = sorted(d.items(), key=lambda x: x[1])
print(sorted_items)  # [('banana', 1), ('cherry', 2), ('apple', 3)]

# 创建排序后的字典
sorted_dict = dict(sorted_items)
print(sorted_dict)  # {'banana': 1, 'cherry': 2, 'apple': 3}

# 降序
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)  # {'apple': 3, 'cherry': 2, 'banana': 1}
```

### 8.3 复杂排序

```python
students = {
    'Alice': {'age': 25, 'score': 85},
    'Bob': {'age': 23, 'score': 92},
    'Charlie': {'age': 24, 'score': 78}
}

# 按分数排序
sorted_students = dict(sorted(
    students.items(),
    key=lambda x: x[1]['score'],
    reverse=True
))

for name, info in sorted_students.items():
    print(f"{name}: {info['score']}")

# 输出:
# Bob: 92
# Alice: 85
# Charlie: 78
```

---

## 9. 字典的合并

### 9.1 update() 方法

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 键冲突时,后者覆盖前者
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}
```

### 9.2 ** 解包运算符(Python 3.5+)

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# 合并为新字典
d3 = {**d1, **d2}
print(d3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 键冲突时,后者覆盖前者
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {**d1, **d2}
print(d3)  # {'a': 1, 'b': 3, 'c': 4}
```

### 9.3 | 运算符(Python 3.9+)

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# 合并为新字典
d3 = d1 | d2
print(d3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 原地合并
d1 |= d2
print(d1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

## 10. 字典的拷贝

### 10.1 浅拷贝

```python
original = {'name': 'Alice', 'age': 25, 'scores': [85, 90]}

# 方法1: copy()
copy1 = original.copy()

# 方法2: dict()
copy2 = dict(original)

# 方法3: 字典推导式
copy3 = {k: v for k, v in original.items()}

# 修改拷贝不影响原字典
copy1['name'] = 'Bob'
print(original['name'])  # 'Alice'

# 但嵌套对象是共享的(浅拷贝)
copy1['scores'].append(95)
print(original['scores'])  # [85, 90, 95] ← 被修改了!
```

### 10.2 深拷贝

```python
import copy

original = {'name': 'Alice', 'age': 25, 'scores': [85, 90]}

# 深拷贝
deep_copy = copy.deepcopy(original)

# 修改嵌套对象不影响原字典
deep_copy['scores'].append(95)
print(original['scores'])  # [85, 90] ← 不受影响
print(deep_copy['scores'])  # [85, 90, 95]
```

---

## 11. 嵌套字典

```python
# 学生信息
students = {
    'Alice': {
        'age': 25,
        'scores': {'math': 85, 'english': 90},
        'address': {'city': 'Beijing', 'street': 'Chaoyang'}
    },
    'Bob': {
        'age': 23,
        'scores': {'math': 92, 'english': 88},
        'address': {'city': 'Shanghai', 'street': 'Pudong'}
    }
}

# 访问嵌套值
print(students['Alice']['age'])  # 25
print(students['Alice']['scores']['math'])  # 85
print(students['Bob']['address']['city'])  # 'Shanghai'

# 修改嵌套值
students['Alice']['age'] = 26
students['Alice']['scores']['math'] = 87

# 遍历嵌套字典
for name, info in students.items():
    print(f"{name}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

---

## 12. 字典的常用方法总结

| 方法 | 说明 | 返回值 | 修改原字典 |
|------|------|--------|-----------|
| `d[key]` | 访问键(不存在报错) | 值 | ❌ |
| `d.get(key, default)` | 访问键(不存在返回默认值) | 值或默认值 | ❌ |
| `d[key] = value` | 添加/修改键值对 | - | ✅ |
| `d.update(other)` | 批量更新 | None | ✅ |
| `d.setdefault(key, default)` | 设置默认值 | 值 | ✅ |
| `del d[key]` | 删除键(不存在报错) | - | ✅ |
| `d.pop(key, default)` | 删除并返回值 | 值或默认值 | ✅ |
| `d.popitem()` | 删除并返回最后一个键值对 | (key, value) | ✅ |
| `d.clear()` | 清空字典 | None | ✅ |
| `d.keys()` | 获取所有键 | dict_keys | ❌ |
| `d.values()` | 获取所有值 | dict_values | ❌ |
| `d.items()` | 获取所有键值对 | dict_items | ❌ |
| `d.copy()` | 浅拷贝 | 新字典 | ❌ |
| `key in d` | 检查键是否存在 | bool | ❌ |
| `len(d)` | 获取键值对数量 | int | ❌ |

---

## 13. defaultdict - 默认字典

```python
from collections import defaultdict

# 普通字典
d = {}
# d['key'].append(1)  # KeyError

# defaultdict - 自动创建默认值
d = defaultdict(list)
d['key'].append(1)  # 不报错
print(d)  # defaultdict(<class 'list'>, {'key': [1]})

# 常用场景:分组
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# 计数
word_count = defaultdict(int)
text = "hello world hello python"
for word in text.split():
    word_count[word] += 1

print(dict(word_count))  # {'hello': 2, 'world': 1, 'python': 1}
```

---

## 14. OrderedDict - 有序字典

```python
from collections import OrderedDict

# Python 3.7+ 普通字典已经有序,OrderedDict 主要用于兼容性
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# move_to_end() 方法
od.move_to_end('a')  # 移到末尾
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

od.move_to_end('c', last=False)  # 移到开头
print(od)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])
```

---

## 15. Counter - 计数器

```python
from collections import Counter

# 创建计数器
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = Counter(words)
print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# 访问计数
print(counter['apple'])  # 3
print(counter['grape'])  # 0 (不存在返回0,不报错)

# 最常见的元素
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]

# 计数器运算
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])

print(c1 + c2)  # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
print(c1 - c2)  # Counter({'a': 1, 'c': 1})
print(c1 & c2)  # Counter({'a': 1, 'b': 1}) 交集(取最小)
print(c1 | c2)  # Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1}) 并集(取最大)
```

---

## 16. 字典的限制

### 16.1 键必须可哈希

```python
# ✅ 可以作为键
d = {
    'string': 1,      # 字符串
    42: 2,            # 数字
    (1, 2): 3,        # 元组
    frozenset([1, 2]): 4  # frozenset
}

# ❌ 不能作为键
# d = {[1, 2]: 'value'}  # TypeError: unhashable type: 'list'
# d = {{1, 2}: 'value'}  # TypeError: unhashable type: 'set'
# d = {{'a': 1}: 'value'}  # TypeError: unhashable type: 'dict'
```

### 16.2 键不能重复

```python
# 重复的键,后者覆盖前者
d = {'a': 1, 'b': 2, 'a': 3}
print(d)  # {'a': 3, 'b': 2}
```

---

## 17. 实用技巧

### 17.1 字典的默认值处理

```python
# 方法1: get()
d = {'a': 1, 'b': 2}
print(d.get('c', 0))  # 0

# 方法2: setdefault()
d.setdefault('c', 0)
print(d)  # {'a': 1, 'b': 2, 'c': 0}

# 方法3: defaultdict
from collections import defaultdict
d = defaultdict(int)
print(d['c'])  # 0
```

### 17.2 字典的反转

```python
d = {'a': 1, 'b': 2, 'c': 3}

# 键值互换
reversed_d = {v: k for k, v in d.items()}
print(reversed_d)  # {1: 'a', 2: 'b', 3: 'c'}

# 注意:值重复时会丢失数据
d = {'a': 1, 'b': 2, 'c': 1}
reversed_d = {v: k for k, v in d.items()}
print(reversed_d)  # {1: 'c', 2: 'b'} ← 'a' 丢失了!
```

### 17.3 字典的过滤

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 过滤值
filtered = {k: v for k, v in d.items() if v > 2}
print(filtered)  # {'c': 3, 'd': 4}

# 过滤键
filtered = {k: v for k, v in d.items() if k in ['a', 'c']}
print(filtered)  # {'a': 1, 'c': 3}
```

### 17.4 字典的合并(保留所有值)

```python
from collections import defaultdict

d1 = {'a': [1, 2], 'b': [3]}
d2 = {'a': [4], 'c': [5]}

# 合并列表值
merged = defaultdict(list)
for d in [d1, d2]:
    for k, v in d.items():
        merged[k].extend(v)

print(dict(merged))  # {'a': [1, 2, 4], 'b': [3], 'c': [5]}
```

---

## 18. 常见应用场景

### 18.1 配置管理

```python
config = {
    'database': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root'
    },
    'cache': {
        'enabled': True,
        'ttl': 3600
    }
}

print(config['database']['host'])  # 'localhost'
```

### 18.2 数据统计

```python
# 统计字符出现次数
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### 18.3 缓存

```python
cache = {}

def expensive_function(n):
    if n in cache:
        print(f"从缓存获取 {n}")
        return cache[n]
    
    print(f"计算 {n}")
    result = n ** 2  # 模拟耗时计算
    cache[n] = result
    return result

print(expensive_function(5))  # 计算 5 → 25
print(expensive_function(5))  # 从缓存获取 5 → 25
```

### 18.4 JSON 数据处理

```python
import json

# 字典转 JSON
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
json_str = json.dumps(person, ensure_ascii=False)
print(json_str)  # {"name": "Alice", "age": 25, "city": "Beijing"}

# JSON 转字典
json_str = '{"name": "Bob", "age": 30}'
person = json.loads(json_str)
print(person)  # {'name': 'Bob', 'age': 30}
```

---

## 19. 性能考虑

```python
import time

# 字典查找 O(1)
d = {i: i for i in range(100000)}
start = time.time()
for _ in range(10000):
    _ = 99999 in d
print(f"字典: {time.time() - start:.4f}秒")

# 列表查找 O(n)
l = list(range(100000))
start = time.time()
for _ in range(10000):
    _ = 99999 in l
print(f"列表: {time.time() - start:.4f}秒")

# 字典快得多!
```

---

## 20. 总结

**字典的核心特点:**
- ✅ 键值对映射
- ✅ 快速查找 O(1)
- ✅ 有序(Python 3.7+)
- ✅ 键唯一且可哈希
- ✅ 值可以是任意类型

**使用场景:**
- 配置管理
- 数据统计/计数
- 缓存
- JSON 数据处理
- 快速查找

**选择建议:**
- 需要键值映射 → `dict`
- 需要默认值 → `defaultdict`
- 需要计数 → `Counter`
- 需要有序(旧版本) → `OrderedDict`
