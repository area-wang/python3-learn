# Python3 Set 详细用法

## 1. 什么是集合 (Set)

集合是 Python 中的**无序、不重复**元素的集合,用花括号 `{}` 或 `set()` 表示。

### 特点对比

| 特性 | 列表 List | 元组 Tuple | 集合 Set |
|------|----------|-----------|---------|
| 符号 | `[]` | `()` | `{}` |
| 可变性 | ✅ 可变 | ❌ 不可变 | ✅ 可变 |
| 有序性 | ✅ 有序 | ✅ 有序 | ❌ 无序 |
| 重复元素 | ✅ 允许 | ✅ 允许 | ❌ 不允许 |
| 索引访问 | ✅ 支持 | ✅ 支持 | ❌ 不支持 |
| 用途 | 动态数据 | 固定数据 | 去重/集合运算 |

```python
# 列表(可重复,有序)
my_list = [1, 2, 2, 3]
print(my_list)  # [1, 2, 2, 3]

# 集合(自动去重,无序)
my_set = {1, 2, 2, 3}
print(my_set)  # {1, 2, 3}

# 不能通过索引访问
# print(my_set[0])  # ❌ TypeError
```

---

## 2. 创建集合

### 2.1 使用花括号

```python
# 基本创建
s = {1, 2, 3}
print(s)  # {1, 2, 3}

# 自动去重
s = {1, 2, 2, 3, 3, 3}
print(s)  # {1, 2, 3}

# 混合类型
s = {1, 'hello', 3.14, True}
print(s)  # {1, 3.14, 'hello'} - True被当作1

# 注意:空集合不能用 {}
empty = {}  # ❌ 这是空字典!
print(type(empty))  # <class 'dict'>
```

### 2.2 使用 set() 函数

```python
# 空集合
s = set()
print(s)  # set()

# 从列表创建
s = set([1, 2, 2, 3])
print(s)  # {1, 2, 3}

# 从元组创建
s = set((1, 2, 2, 3))
print(s)  # {1, 2, 3}

# 从字符串创建
s = set('hello')
print(s)  # {'h', 'e', 'l', 'o'} - 自动去重

# 从字典创建(只取键)
s = set({'a': 1, 'b': 2})
print(s)  # {'a', 'b'}
```

### 2.3 集合推导式

```python
# 基本推导式
s = {x for x in range(10)}
print(s)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# 带条件
s = {x for x in range(10) if x % 2 == 0}
print(s)  # {0, 2, 4, 6, 8}

# 带转换
s = {x**2 for x in range(5)}
print(s)  # {0, 1, 4, 9, 16}
```

---

## 3. 集合的基本操作

### 3.1 添加元素

#### add() - 添加单个元素

```python
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

# 添加已存在的元素(无效果)
s.add(2)
print(s)  # {1, 2, 3, 4}

# 添加不同类型
s.add('hello')
print(s)  # {1, 2, 3, 4, 'hello'}
```

#### update() - 添加多个元素

```python
s = {1, 2, 3}

# 添加列表
s.update([4, 5, 6])
print(s)  # {1, 2, 3, 4, 5, 6}

# 添加元组
s.update((7, 8))
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 添加字符串(逐字符)
s.update('ab')
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b'}

# 添加多个可迭代对象
s = {1, 2}
s.update([3, 4], (5, 6), {7, 8})
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8}
```

### 3.2 删除元素

#### remove() - 删除指定元素(不存在会报错)

```python
s = {1, 2, 3, 4, 5}

s.remove(3)
print(s)  # {1, 2, 4, 5}

# 删除不存在的元素会报错
try:
    s.remove(10)
except KeyError as e:
    print(f"错误: {e}")  # 错误: 10
```

#### discard() - 删除指定元素(不存在不报错)

```python
s = {1, 2, 3, 4, 5}

s.discard(3)
print(s)  # {1, 2, 4, 5}

# 删除不存在的元素(不报错)
s.discard(10)
print(s)  # {1, 2, 4, 5}
```

#### pop() - 随机删除并返回一个元素

```python
s = {1, 2, 3, 4, 5}

element = s.pop()
print(f"删除的元素: {element}")
print(f"剩余集合: {s}")

# 空集合pop会报错
try:
    empty = set()
    empty.pop()
except KeyError:
    print("空集合不能pop")
```

#### clear() - 清空集合

```python
s = {1, 2, 3, 4, 5}
s.clear()
print(s)  # set()
print(len(s))  # 0
```

### 3.3 成员检查

```python
s = {1, 2, 3, 4, 5}

# in 运算符
print(3 in s)  # True
print(10 in s)  # False

# not in 运算符
print(10 not in s)  # True

# 性能:集合的成员检查是 O(1),列表是 O(n)
```

### 3.4 长度

```python
s = {1, 2, 3, 4, 5}
print(len(s))  # 5

empty = set()
print(len(empty))  # 0
```

---

## 4. 集合运算

### 4.1 并集 (Union)

```python
a = {1, 2, 3}
b = {3, 4, 5}

# 方法1: | 运算符
print(a | b)  # {1, 2, 3, 4, 5}

# 方法2: union() 方法
print(a.union(b))  # {1, 2, 3, 4, 5}

# 多个集合并集
c = {5, 6, 7}
print(a | b | c)  # {1, 2, 3, 4, 5, 6, 7}
print(a.union(b, c))  # {1, 2, 3, 4, 5, 6, 7}

# 原集合不变
print(a)  # {1, 2, 3}
```

### 4.2 交集 (Intersection)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 方法1: & 运算符
print(a & b)  # {3, 4}

# 方法2: intersection() 方法
print(a.intersection(b))  # {3, 4}

# 多个集合交集
c = {3, 4, 7, 8}
print(a & b & c)  # {3, 4}
print(a.intersection(b, c))  # {3, 4}
```

### 4.3 差集 (Difference)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 方法1: - 运算符
print(a - b)  # {1, 2} (a中有但b中没有)
print(b - a)  # {5, 6} (b中有但a中没有)

# 方法2: difference() 方法
print(a.difference(b))  # {1, 2}

# 多个集合差集
c = {2, 3}
print(a - b - c)  # {1}
print(a.difference(b, c))  # {1}
```

### 4.4 对称差集 (Symmetric Difference)

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 方法1: ^ 运算符
print(a ^ b)  # {1, 2, 5, 6} (在a或b中,但不同时在两者中)

# 方法2: symmetric_difference() 方法
print(a.symmetric_difference(b))  # {1, 2, 5, 6}

# 等价于
print((a - b) | (b - a))  # {1, 2, 5, 6}
print((a | b) - (a & b))  # {1, 2, 5, 6}
```

### 4.5 原地修改方法

```python
a = {1, 2, 3}
b = {3, 4, 5}

# update() - 并集并修改
a_copy = a.copy()
a_copy.update(b)
print(a_copy)  # {1, 2, 3, 4, 5}

# intersection_update() - 交集并修改
a_copy = a.copy()
a_copy.intersection_update(b)
print(a_copy)  # {3}

# difference_update() - 差集并修改
a_copy = a.copy()
a_copy.difference_update(b)
print(a_copy)  # {1, 2}

# symmetric_difference_update() - 对称差集并修改
a_copy = a.copy()
a_copy.symmetric_difference_update(b)
print(a_copy)  # {1, 2, 4, 5}
```

---

## 5. 集合关系判断

### 5.1 子集 (Subset)

```python
a = {1, 2}
b = {1, 2, 3, 4}

# 方法1: <= 运算符
print(a <= b)  # True (a是b的子集)
print(b <= a)  # False

# 方法2: issubset() 方法
print(a.issubset(b))  # True

# 真子集(不相等的子集)
print(a < b)  # True
print(a < a)  # False (自己不是自己的真子集)
```

### 5.2 超集 (Superset)

```python
a = {1, 2, 3, 4}
b = {1, 2}

# 方法1: >= 运算符
print(a >= b)  # True (a是b的超集)
print(b >= a)  # False

# 方法2: issuperset() 方法
print(a.issuperset(b))  # True

# 真超集
print(a > b)  # True
print(a > a)  # False
```

### 5.3 不相交 (Disjoint)

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

# isdisjoint() - 判断是否没有交集
print(a.isdisjoint(b))  # True (没有交集)
print(a.isdisjoint(c))  # False (有交集3)
```

---

## 6. 集合的其他方法

### 6.1 copy() - 浅拷贝

```python
a = {1, 2, 3}
b = a.copy()

b.add(4)
print(a)  # {1, 2, 3}
print(b)  # {1, 2, 3, 4}

# 注意:浅拷贝
a = {1, 2, frozenset([3, 4])}
b = a.copy()
print(a is b)  # False (不同对象)
```

### 6.2 遍历集合

```python
s = {1, 2, 3, 4, 5}

# for 循环
for item in s:
    print(item, end=' ')  # 顺序不确定
print()

# 转换为列表后排序
for item in sorted(s):
    print(item, end=' ')  # 1 2 3 4 5
print()

# enumerate
for i, item in enumerate(sorted(s)):
    print(f"{i}: {item}")
```

---

## 7. 冻结集合 (frozenset)

frozenset 是**不可变**的集合,可以作为字典的键或集合的元素。

```python
# 创建
fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})

# 不可修改
# fs.add(4)  # ❌ AttributeError

# 可以进行集合运算
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a | b)  # frozenset({1, 2, 3, 4, 5})
print(a & b)  # frozenset({3})

# 可以作为字典键
d = {frozenset([1, 2]): 'value'}
print(d[frozenset([1, 2])])  # 'value'

# 可以作为集合元素
s = {frozenset([1, 2]), frozenset([3, 4])}
print(s)  # {frozenset({1, 2}), frozenset({3, 4})}
```

---

## 8. 集合的限制

### 8.1 元素必须可哈希

```python
# ✅ 可以作为集合元素
s = {1, 2, 3}  # 数字
s = {'a', 'b', 'c'}  # 字符串
s = {(1, 2), (3, 4)}  # 元组
s = {frozenset([1, 2])}  # frozenset

# ❌ 不能作为集合元素
# s = {[1, 2]}  # TypeError: unhashable type: 'list'
# s = {{1, 2}}  # TypeError: unhashable type: 'set'
# s = {{'a': 1}}  # TypeError: unhashable type: 'dict'
```

### 8.2 无序性

```python
s = {5, 2, 8, 1, 9}
print(s)  # 顺序不确定,可能是 {1, 2, 5, 8, 9}

# 每次运行顺序可能不同
for i in range(3):
    print({5, 2, 8, 1, 9})
```

---

## 9. 实用技巧

### 9.1 去重

```python
# 列表去重
my_list = [1, 2, 2, 3, 3, 3, 4]
unique_list = list(set(my_list))
print(unique_list)  # [1, 2, 3, 4] (顺序可能不同)

# 保持顺序去重
def unique_ordered(items):
    return list(dict.fromkeys(items))

print(unique_ordered([5, 2, 8, 2, 1]))  # [5, 2, 8, 1]
```

### 9.2 查找共同元素

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = set(list1) & set(list2)
print(common)  # {4, 5}
```

### 9.3 查找唯一元素

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

unique_to_list1 = set(list1) - set(list2)
print(unique_to_list1)  # {1, 2, 3}

unique_to_list2 = set(list2) - set(list1)
print(unique_to_list2)  # {6, 7, 8}

# 所有唯一元素
all_unique = set(list1) ^ set(list2)
print(all_unique)  # {1, 2, 3, 6, 7, 8}
```

### 9.4 性能优势

```python
import time

# 列表成员检查 O(n)
my_list = list(range(10000))
start = time.time()
for _ in range(1000):
    9999 in my_list
print(f"列表: {time.time() - start:.4f}秒")

# 集合成员检查 O(1)
my_set = set(range(10000))
start = time.time()
for _ in range(1000):
    9999 in my_set
print(f"集合: {time.time() - start:.4f}秒")

# 集合快得多!
```

---

## 10. 常见应用场景

### 10.1 统计唯一值

```python
words = ['apple', 'banana', 'apple', 'cherry', 'banana']
unique_words = set(words)
print(f"唯一单词数: {len(unique_words)}")  # 3
```

### 10.2 权限检查

```python
user_permissions = {'read', 'write'}
required_permissions = {'read', 'write', 'execute'}

# 检查是否有所有权限
has_all = user_permissions >= required_permissions
print(has_all)  # False

# 缺少的权限
missing = required_permissions - user_permissions
print(missing)  # {'execute'}
```

### 10.3 标签系统

```python
post1_tags = {'python', 'programming', 'tutorial'}
post2_tags = {'python', 'data-science', 'tutorial'}

# 共同标签
common_tags = post1_tags & post2_tags
print(common_tags)  # {'python', 'tutorial'}

# 所有标签
all_tags = post1_tags | post2_tags
print(all_tags)  # {'python', 'programming', 'tutorial', 'data-science'}
```

---

## 11. 方法总结表

| 方法 | 说明 | 修改原集合 |
|------|------|-----------|
| `add(x)` | 添加元素 | ✅ |
| `update(iterable)` | 添加多个元素 | ✅ |
| `remove(x)` | 删除元素(不存在报错) | ✅ |
| `discard(x)` | 删除元素(不存在不报错) | ✅ |
| `pop()` | 随机删除并返回元素 | ✅ |
| `clear()` | 清空集合 | ✅ |
| `copy()` | 浅拷贝 | ❌ |
| `union()` / `\|` | 并集 | ❌ |
| `intersection()` / `&` | 交集 | ❌ |
| `difference()` / `-` | 差集 | ❌ |
| `symmetric_difference()` / `^` | 对称差集 | ❌ |
| `intersection_update()` / `&=` | 交集并修改 | ✅ |
| `difference_update()` / `-=` | 差集并修改 | ✅ |
| `symmetric_difference_update()` / `^=` | 对称差集并修改 | ✅ |
| `issubset()` / `<=` | 是否为子集 | ❌ |
| `issuperset()` / `>=` | 是否为超集 | ❌ |
| `isdisjoint()` | 是否不相交 | ❌ |

---

## 12. 总结

**集合的核心特点:**
- ✅ 自动去重
- ✅ 快速成员检查 O(1)
- ✅ 强大的集合运算
- ❌ 无序(不能索引)
- ❌ 元素必须可哈希

**使用场景:**
- 去重
- 成员检查
- 集合运算(并、交、差)
- 统计唯一值
- 权限/标签管理

**选择建议:**
- 需要去重 → `set`
- 需要有序 → `list` + `dict.fromkeys()`
- 需要不可变 → `frozenset`
- 需要索引 → `list`
