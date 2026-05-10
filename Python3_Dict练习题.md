# Python3 Dict 练习题

## 基础题 (10题)

### 1. 创建字典
创建一个包含你的姓名、年龄和城市的字典,并打印出来。

<details>
<summary>点击查看答案</summary>

```python
# 方法1: 使用花括号
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(person)

# 方法2: 使用 dict()
person = dict(name='Alice', age=25, city='Beijing')
print(person)

# 方法3: 从键值对列表
person = dict([('name', 'Alice'), ('age', 25), ('city', 'Beijing')])
print(person)
```
</details>

---

### 2. 访问字典元素
给定字典 `person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}`,访问姓名和年龄。

<details>
<summary>点击查看答案</summary>

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 方法1: 使用方括号
print(person['name'])  # 'Alice'
print(person['age'])   # 25

# 方法2: 使用 get()
print(person.get('name'))  # 'Alice'
print(person.get('age'))   # 25

# get() 的优势:访问不存在的键不报错
print(person.get('phone', 'N/A'))  # 'N/A'
```
</details>

---

### 3. 添加/修改元素
创建字典 `d = {'a': 1, 'b': 2}`,添加键 'c' 值为 3,修改键 'a' 的值为 10。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2}

# 添加新键
d['c'] = 3
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# 修改已存在的键
d['a'] = 10
print(d)  # {'a': 10, 'b': 2, 'c': 3}
```
</details>

---

### 4. 删除元素
给定字典 `d = {'a': 1, 'b': 2, 'c': 3}`,删除键 'b'。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3}

# 方法1: del
del d['b']
print(d)  # {'a': 1, 'c': 3}

# 方法2: pop()
d = {'a': 1, 'b': 2, 'c': 3}
value = d.pop('b')
print(value)  # 2
print(d)  # {'a': 1, 'c': 3}

# pop() 可以指定默认值
d = {'a': 1, 'c': 3}
value = d.pop('b', 'not found')
print(value)  # 'not found'
```
</details>

---

### 5. 检查键是否存在
给定字典 `d = {'a': 1, 'b': 2}`,检查键 'a' 和 'c' 是否存在。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2}

# 使用 in 运算符
print('a' in d)  # True
print('c' in d)  # False

# 使用 not in
print('c' not in d)  # True

# 先检查再访问
if 'c' in d:
    print(d['c'])
else:
    print('键不存在')
```
</details>

---

### 6. 获取字典长度
创建字典 `d = {'a': 1, 'b': 2, 'c': 3}`,获取字典的长度。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3}
print(len(d))  # 3

# 空字典
empty = {}
print(len(empty))  # 0
```
</details>

---

### 7. 遍历字典
给定字典 `person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}`,遍历并打印所有键值对。

<details>
<summary>点击查看答案</summary>

```python
person = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 方法1: 遍历键值对(推荐)
for key, value in person.items():
    print(f"{key}: {value}")

# 方法2: 遍历键
for key in person:
    print(f"{key}: {person[key]}")

# 方法3: 遍历键(显式)
for key in person.keys():
    print(f"{key}: {person[key]}")

# 方法4: 遍历值
for value in person.values():
    print(value)
```
</details>

---

### 8. 获取所有键和值
给定字典 `d = {'a': 1, 'b': 2, 'c': 3}`,获取所有键和所有值的列表。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3}

# 获取所有键
keys = list(d.keys())
print(keys)  # ['a', 'b', 'c']

# 获取所有值
values = list(d.values())
print(values)  # [1, 2, 3]

# 获取所有键值对
items = list(d.items())
print(items)  # [('a', 1), ('b', 2), ('c', 3)]
```
</details>

---

### 9. 字典合并
合并两个字典 `d1 = {'a': 1, 'b': 2}` 和 `d2 = {'c': 3, 'd': 4}`。

<details>
<summary>点击查看答案</summary>

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# 方法1: update() (修改 d1)
d1_copy = d1.copy()
d1_copy.update(d2)
print(d1_copy)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 方法2: ** 解包 (创建新字典)
d3 = {**d1, **d2}
print(d3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 方法3: | 运算符 (Python 3.9+)
d3 = d1 | d2
print(d3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
</details>

---

### 10. 清空字典
创建字典 `d = {'a': 1, 'b': 2, 'c': 3}`,清空它。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3}

d.clear()
print(d)  # {}
print(len(d))  # 0
```
</details>

---

## 进阶题 (10题)

### 11. 字典推导式
使用字典推导式创建一个字典,键为 1-5,值为键的平方。

<details>
<summary>点击查看答案</summary>

```python
# 基本推导式
d = {x: x**2 for x in range(1, 6)}
print(d)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 带条件
d = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(d)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 从列表创建
words = ['apple', 'banana', 'cherry']
d = {word: len(word) for word in words}
print(d)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```
</details>

---

### 12. setdefault() 使用
使用 `setdefault()` 统计列表中每个元素出现的次数。

<details>
<summary>点击查看答案</summary>

```python
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

word_count = {}
for word in words:
    word_count[word] = word_count.setdefault(word, 0) + 1

print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}

# 更简洁的方法
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```
</details>

---

### 13. 字典排序
给定字典 `d = {'banana': 3, 'apple': 1, 'cherry': 2}`,按值排序。

<details>
<summary>点击查看答案</summary>

```python
d = {'banana': 3, 'apple': 1, 'cherry': 2}

# 按值升序
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)  # {'apple': 1, 'cherry': 2, 'banana': 3}

# 按值降序
sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(sorted_d)  # {'banana': 3, 'cherry': 2, 'apple': 1}

# 按键排序
sorted_d = dict(sorted(d.items()))
print(sorted_d)  # {'apple': 1, 'banana': 3, 'cherry': 2}
```
</details>

---

### 14. 嵌套字典
创建一个嵌套字典表示学生信息,并访问嵌套值。

<details>
<summary>点击查看答案</summary>

```python
students = {
    'Alice': {
        'age': 25,
        'scores': {'math': 85, 'english': 90}
    },
    'Bob': {
        'age': 23,
        'scores': {'math': 92, 'english': 88}
    }
}

# 访问嵌套值
print(students['Alice']['age'])  # 25
print(students['Alice']['scores']['math'])  # 85
print(students['Bob']['scores']['english'])  # 88

# 修改嵌套值
students['Alice']['age'] = 26
students['Alice']['scores']['math'] = 87

# 遍历嵌套字典
for name, info in students.items():
    print(f"{name}:")
    print(f"  年龄: {info['age']}")
    print(f"  成绩: {info['scores']}")
```
</details>

---

### 15. 字典反转
给定字典 `d = {'a': 1, 'b': 2, 'c': 3}`,键值互换。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3}

# 键值互换
reversed_d = {v: k for k, v in d.items()}
print(reversed_d)  # {1: 'a', 2: 'b', 3: 'c'}

# 注意:值重复时会丢失数据
d = {'a': 1, 'b': 2, 'c': 1}
reversed_d = {v: k for k, v in d.items()}
print(reversed_d)  # {1: 'c', 2: 'b'} ← 'a' 丢失了!

# 处理重复值
d = {'a': 1, 'b': 2, 'c': 1}
reversed_d = {}
for k, v in d.items():
    if v not in reversed_d:
        reversed_d[v] = []
    reversed_d[v].append(k)
print(reversed_d)  # {1: ['a', 'c'], 2: ['b']}
```
</details>

---

### 16. 字典过滤
给定字典 `d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}`,过滤出值大于 2 的键值对。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 过滤值
filtered = {k: v for k, v in d.items() if v > 2}
print(filtered)  # {'c': 3, 'd': 4}

# 过滤键
filtered = {k: v for k, v in d.items() if k in ['a', 'c']}
print(filtered)  # {'a': 1, 'c': 3}

# 使用 filter()
filtered = dict(filter(lambda item: item[1] > 2, d.items()))
print(filtered)  # {'c': 3, 'd': 4}
```
</details>

---

### 17. 字典拷贝
创建字典的浅拷贝和深拷贝,并验证区别。

<details>
<summary>点击查看答案</summary>

```python
import copy

original = {'name': 'Alice', 'scores': [85, 90]}

# 浅拷贝
shallow = original.copy()
shallow['scores'].append(95)
print(original['scores'])  # [85, 90, 95] ← 被修改了!

# 深拷贝
original = {'name': 'Alice', 'scores': [85, 90]}
deep = copy.deepcopy(original)
deep['scores'].append(95)
print(original['scores'])  # [85, 90] ← 不受影响
print(deep['scores'])  # [85, 90, 95]
```
</details>

---

### 18. update() 方法
使用 `update()` 方法合并字典,处理键冲突。

<details>
<summary>点击查看答案</summary>

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# update() 会覆盖相同的键
d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

# 使用多种方式 update
d = {'a': 1}
d.update({'b': 2})  # 字典
d.update([('c', 3)])  # 键值对列表
d.update(d=4)  # 关键字参数
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
</details>

---

### 19. popitem() 方法
使用 `popitem()` 删除字典的最后一个元素。

<details>
<summary>点击查看答案</summary>

```python
d = {'a': 1, 'b': 2, 'c': 3}

# 删除并返回最后一个键值对
item = d.popitem()
print(item)  # ('c', 3)
print(d)  # {'a': 1, 'b': 2}

# 继续删除
item = d.popitem()
print(item)  # ('b', 2)
print(d)  # {'a': 1}

# 空字典会报错
try:
    empty = {}
    empty.popitem()
except KeyError:
    print('字典为空')
```
</details>

---

### 20. fromkeys() 方法
使用 `fromkeys()` 创建字典。

<details>
<summary>点击查看答案</summary>

```python
# 创建具有相同值的字典
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # {'a': 0, 'b': 0, 'c': 0}

# 默认值为 None
d = dict.fromkeys(keys)
print(d)  # {'a': None, 'b': None, 'c': None}

# 注意:可变对象陷阱
d = dict.fromkeys(['a', 'b'], [])
d['a'].append(1)
print(d)  # {'a': [1], 'b': [1]} ← 共享同一个列表!

# 正确做法
d = {k: [] for k in ['a', 'b']}
d['a'].append(1)
print(d)  # {'a': [1], 'b': []}
```
</details>

---

## 挑战题 (10题)

### 21. 统计字符频率
编写函数 `char_frequency(text)`,统计文本中每个字符出现的频率。

<details>
<summary>点击查看答案</summary>

```python
def char_frequency(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

# 测试
text = "hello world"
print(char_frequency(text))
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# 使用 Counter
from collections import Counter

def char_frequency_v2(text):
    return dict(Counter(text))

print(char_frequency_v2(text))
```
</details>

---

### 22. 分组
编写函数 `group_by(items, key_func)`,按指定函数分组。

<details>
<summary>点击查看答案</summary>

```python
def group_by(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# 测试:按长度分组
words = ['apple', 'hi', 'banana', 'cat', 'dog']
grouped = group_by(words, len)
print(grouped)
# {5: ['apple'], 2: ['hi'], 6: ['banana'], 3: ['cat', 'dog']}

# 按首字母分组
grouped = group_by(words, lambda x: x[0])
print(grouped)
# {'a': ['apple'], 'h': ['hi'], 'b': ['banana'], 'c': ['cat'], 'd': ['dog']}

# 使用 defaultdict
from collections import defaultdict

def group_by_v2(items, key_func):
    groups = defaultdict(list)
    for item in items:
        groups[key_func(item)].append(item)
    return dict(groups)
```
</details>

---

### 23. 字典合并(保留所有值)
编写函数合并多个字典,相同键的值合并为列表。

<details>
<summary>点击查看答案</summary>

```python
def merge_dicts(*dicts):
    from collections import defaultdict
    merged = defaultdict(list)
    
    for d in dicts:
        for k, v in d.items():
            if isinstance(v, list):
                merged[k].extend(v)
            else:
                merged[k].append(v)
    
    return dict(merged)

# 测试
d1 = {'a': 1, 'b': 2}
d2 = {'a': 3, 'c': 4}
d3 = {'a': 5, 'b': 6}

result = merge_dicts(d1, d2, d3)
print(result)  # {'a': [1, 3, 5], 'b': [2, 6], 'c': [4]}
```
</details>

---

### 24. 扁平化嵌套字典
编写函数将嵌套字典扁平化,使用点号连接键。

<details>
<summary>点击查看答案</summary>

```python
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# 测试
nested = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    },
    'f': 4
}

flat = flatten_dict(nested)
print(flat)
# {'a': 1, 'b.c': 2, 'b.d.e': 3, 'f': 4}
```
</details>

---

### 25. 字典差集
编写函数找出两个字典的差异(键或值不同的部分)。

<details>
<summary>点击查看答案</summary>

```python
def dict_diff(d1, d2):
    # 只在 d1 中的键
    only_in_d1 = {k: d1[k] for k in d1.keys() - d2.keys()}
    
    # 只在 d2 中的键
    only_in_d2 = {k: d2[k] for k in d2.keys() - d1.keys()}
    
    # 值不同的键
    different_values = {
        k: (d1[k], d2[k])
        for k in d1.keys() & d2.keys()
        if d1[k] != d2[k]
    }
    
    return {
        'only_in_d1': only_in_d1,
        'only_in_d2': only_in_d2,
        'different_values': different_values
    }

# 测试
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4, 'd': 5}

diff = dict_diff(d1, d2)
print(diff)
# {
#     'only_in_d1': {'a': 1},
#     'only_in_d2': {'d': 5},
#     'different_values': {'c': (3, 4)}
# }
```
</details>

---

### 26. 字典排序(多条件)
按多个条件对字典排序(先按值降序,值相同按键升序)。

<details>
<summary>点击查看答案</summary>

```python
d = {'apple': 3, 'banana': 1, 'cherry': 3, 'date': 2}

# 多条件排序
sorted_d = dict(sorted(
    d.items(),
    key=lambda x: (-x[1], x[0])  # 值降序,键升序
))

print(sorted_d)
# {'apple': 3, 'cherry': 3, 'date': 2, 'banana': 1}
```
</details>

---

### 27. 缓存装饰器
使用字典实现一个简单的缓存装饰器。

<details>
<summary>点击查看答案</summary>

```python
def memoize(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"从缓存获取: {args}")
            return cache[args]
        
        print(f"计算: {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 测试
print(fibonacci(5))  # 计算多次
print(fibonacci(5))  # 从缓存获取

# 使用 functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_v2(n):
    if n <= 1:
        return n
    return fibonacci_v2(n-1) + fibonacci_v2(n-2)

print(fibonacci_v2(100))  # 很快!
```
</details>

---

### 28. 反向索引
给定文档列表,创建单词到文档的反向索引。

<details>
<summary>点击查看答案</summary>

```python
def create_inverted_index(documents):
    index = {}
    
    for doc_id, doc in enumerate(documents):
        for word in doc.split():
            word = word.lower()
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    
    # 转换为列表
    return {word: list(docs) for word, docs in index.items()}

# 测试
documents = [
    "Python is great",
    "I love Python",
    "Python and Java"
]

index = create_inverted_index(documents)
print(index)
# {
#     'python': [0, 1, 2],
#     'is': [0],
#     'great': [0],
#     'i': [1],
#     'love': [1],
#     'and': [2],
#     'java': [2]
# }

# 搜索包含 "python" 的文档
print(f"包含 'python' 的文档: {index.get('python', [])}")
```
</details>

---

### 29. 配置管理器
实现一个支持嵌套访问的配置管理器。

<details>
<summary>点击查看答案</summary>

```python
class Config:
    def __init__(self, data):
        self.data = data
    
    def get(self, path, default=None):
        """
        使用点号路径访问嵌套值
        例: config.get('database.host')
        """
        keys = path.split('.')
        value = self.data
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, path, value):
        """设置嵌套值"""
        keys = path.split('.')
        data = self.data
        
        for key in keys[:-1]:
            if key not in data:
                data[key] = {}
            data = data[key]
        
        data[keys[-1]] = value

# 测试
config_data = {
    'database': {
        'host': 'localhost',
        'port': 3306
    },
    'cache': {
        'enabled': True
    }
}

config = Config(config_data)

# 获取值
print(config.get('database.host'))  # 'localhost'
print(config.get('database.user', 'root'))  # 'root' (默认值)

# 设置值
config.set('database.user', 'admin')
print(config.get('database.user'))  # 'admin'
```
</details>

---

### 30. 字典的深度合并
实现深度合并两个嵌套字典。

<details>
<summary>点击查看答案</summary>

```python
def deep_merge(dict1, dict2):
    """
    深度合并两个字典
    dict2 的值会覆盖 dict1
    """
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # 递归合并嵌套字典
            result[key] = deep_merge(result[key], value)
        else:
            # 直接覆盖
            result[key] = value
    
    return result

# 测试
d1 = {
    'a': 1,
    'b': {
        'c': 2,
        'd': 3
    },
    'e': 4
}

d2 = {
    'b': {
        'd': 5,
        'f': 6
    },
    'g': 7
}

merged = deep_merge(d1, d2)
print(merged)
# {
#     'a': 1,
#     'b': {'c': 2, 'd': 5, 'f': 6},
#     'e': 4,
#     'g': 7
# }
```
</details>

---

## 综合应用题 (5题)

### 31. 学生成绩管理系统
实现一个学生成绩管理系统,支持添加、查询、统计等功能。

<details>
<summary>点击查看答案</summary>

```python
class GradeManager:
    def __init__(self):
        # 学生 -> {科目: 成绩}
        self.grades = {}
    
    def add_grade(self, student, subject, score):
        """添加成绩"""
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][subject] = score
    
    def get_student_grades(self, student):
        """获取学生所有成绩"""
        return self.grades.get(student, {})
    
    def get_average(self, student):
        """计算学生平均分"""
        grades = self.grades.get(student, {})
        if not grades:
            return 0
        return sum(grades.values()) / len(grades)
    
    def get_subject_average(self, subject):
        """计算某科目的平均分"""
        scores = [
            grades[subject]
            for grades in self.grades.values()
            if subject in grades
        ]
        return sum(scores) / len(scores) if scores else 0
    
    def get_top_students(self, n=3):
        """获取平均分最高的 n 个学生"""
        averages = {
            student: self.get_average(student)
            for student in self.grades
        }
        sorted_students = sorted(
            averages.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_students[:n]

# 测试
manager = GradeManager()

# 添加成绩
manager.add_grade('Alice', 'Math', 85)
manager.add_grade('Alice', 'English', 90)
manager.add_grade('Bob', 'Math', 92)
manager.add_grade('Bob', 'English', 88)
manager.add_grade('Charlie', 'Math', 78)
manager.add_grade('Charlie', 'English', 95)

# 查询
print(manager.get_student_grades('Alice'))  # {'Math': 85, 'English': 90}
print(f"Alice 平均分: {manager.get_average('Alice'):.2f}")  # 87.50
print(f"Math 平均分: {manager.get_subject_average('Math'):.2f}")  # 85.00

# 排名
print("前3名:")
for i, (student, avg) in enumerate(manager.get_top_students(3), 1):
    print(f"{i}. {student}: {avg:.2f}")
```
</details>

---

### 32. 单词索引和搜索
实现一个简单的文本搜索引擎。

<details>
<summary>点击查看答案</summary>

```python
class SearchEngine:
    def __init__(self):
        # 单词 -> {文档ID: 出现次数}
        self.index = {}
        # 文档ID -> 文档内容
        self.documents = {}
    
    def add_document(self, doc_id, text):
        """添加文档"""
        self.documents[doc_id] = text
        
        # 建立索引
        for word in text.lower().split():
            if word not in self.index:
                self.index[word] = {}
            self.index[word][doc_id] = self.index[word].get(doc_id, 0) + 1
    
    def search(self, query):
        """搜索文档"""
        words = query.lower().split()
        
        # 找出包含所有查询词的文档
        if not words:
            return []
        
        # 第一个词的文档集合
        result_docs = set(self.index.get(words[0], {}).keys())
        
        # 取交集
        for word in words[1:]:
            result_docs &= set(self.index.get(word, {}).keys())
        
        # 按相关度排序(简单计数)
        scores = {}
        for doc_id in result_docs:
            score = sum(
                self.index.get(word, {}).get(doc_id, 0)
                for word in words
            )
            scores[doc_id] = score
        
        # 排序
        sorted_docs = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return [(doc_id, self.documents[doc_id]) for doc_id, _ in sorted_docs]

# 测试
engine = SearchEngine()

# 添加文档
engine.add_document(1, "Python is a great programming language")
engine.add_document(2, "I love Python programming")
engine.add_document(3, "Java is also a programming language")

# 搜索
results = engine.search("Python programming")
print("搜索结果:")
for doc_id, text in results:
    print(f"文档 {doc_id}: {text}")
```
</details>

---

### 33. 购物车系统
实现一个购物车系统,支持添加、删除、计算总价等功能。

<details>
<summary>点击查看答案</summary>

```python
class ShoppingCart:
    def __init__(self):
        # 商品ID -> {'name': 名称, 'price': 价格, 'quantity': 数量}
        self.items = {}
    
    def add_item(self, item_id, name, price, quantity=1):
        """添加商品"""
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
        else:
            self.items[item_id] = {
                'name': name,
                'price': price,
                'quantity': quantity
            }
    
    def remove_item(self, item_id):
        """删除商品"""
        if item_id in self.items:
            del self.items[item_id]
    
    def update_quantity(self, item_id, quantity):
        """更新数量"""
        if item_id in self.items:
            if quantity <= 0:
                self.remove_item(item_id)
            else:
                self.items[item_id]['quantity'] = quantity
    
    def get_total(self):
        """计算总价"""
        return sum(
            item['price'] * item['quantity']
            for item in self.items.values()
        )
    
    def get_item_count(self):
        """获取商品种类数"""
        return len(self.items)
    
    def get_total_quantity(self):
        """获取商品总数量"""
        return sum(item['quantity'] for item in self.items.values())
    
    def apply_discount(self, discount_rate):
        """应用折扣"""
        for item in self.items.values():
            item['price'] *= (1 - discount_rate)
    
    def display(self):
        """显示购物车"""
        print("购物车:")
        for item_id, item in self.items.items():
            print(f"  {item['name']}: "
                  f"¥{item['price']:.2f} x {item['quantity']} = "
                  f"¥{item['price'] * item['quantity']:.2f}")
        print(f"总计: ¥{self.get_total():.2f}")

# 测试
cart = ShoppingCart()

# 添加商品
cart.add_item(1, 'Apple', 5.0, 3)
cart.add_item(2, 'Banana', 3.0, 5)
cart.add_item(1, 'Apple', 5.0, 2)  # 再添加2个苹果

# 显示
cart.display()

# 应用折扣
cart.apply_discount(0.1)  # 9折
print("\n应用9折后:")
cart.display()
```
</details>

---

### 34. 图的邻接表表示
使用字典实现图的邻接表表示,并实现 BFS 遍历。

<details>
<summary>点击查看答案</summary>

```python
from collections import deque

class Graph:
    def __init__(self):
        # 顶点 -> [邻接顶点列表]
        self.graph = {}
    
    def add_edge(self, u, v):
        """添加边"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        # 如果是无向图,添加反向边
        # self.graph[v].append(u)
    
    def bfs(self, start):
        """广度优先搜索"""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # 添加邻接顶点
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs(self, start, visited=None):
        """深度优先搜索"""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result

# 测试
g = Graph()

# 添加边
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

# 遍历
print("BFS:", g.bfs('A'))  # ['A', 'B', 'C', 'D', 'E']
print("DFS:", g.dfs('A'))  # ['A', 'B', 'D', 'E', 'C']
```
</details>

---

### 35. LRU 缓存
实现一个 LRU (Least Recently Used) 缓存。

<details>
<summary>点击查看答案</summary>

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        """获取值"""
        if key not in self.cache:
            return -1
        
        # 移到末尾(最近使用)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """设置值"""
        if key in self.cache:
            # 更新并移到末尾
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # 超过容量,删除最久未使用的(开头)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
    def display(self):
        """显示缓存"""
        print(f"缓存 (容量: {self.capacity}):")
        for key, value in self.cache.items():
            print(f"  {key}: {value}")

# 测试
cache = LRUCache(3)

cache.put(1, 'a')
cache.put(2, 'b')
cache.put(3, 'c')
cache.display()
# 缓存: {1: 'a', 2: 'b', 3: 'c'}

cache.get(1)  # 访问 1
cache.put(4, 'd')  # 添加 4,删除最久未使用的 2
cache.display()
# 缓存: {3: 'c', 1: 'a', 4: 'd'}

print(cache.get(2))  # -1 (已被删除)
```
</details>

---

## 学习建议

1. **理解键值映射** - 字典的核心是键值对
2. **掌握常用方法** - get(), items(), update() 等
3. **注意键的限制** - 必须可哈希
4. **活用字典推导式** - 简洁高效
5. **实践应用** - 配置、缓存、索引等场景

祝学习愉快! 🎉
