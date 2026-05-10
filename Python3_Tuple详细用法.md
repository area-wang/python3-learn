# Python3 Tuple 详细用法

## 1. 什么是元组 (Tuple)

元组是 Python 中的**不可变序列**,用圆括号 `()` 表示。

### 特点对比

| 特性 | 列表 List | 元组 Tuple |
|------|----------|-----------|
| 符号 | `[]` | `()` |
| 可变性 | ✅ 可变 | ❌ 不可变 |
| 性能 | 较慢 | 较快 |
| 用途 | 动态数据 | 固定数据 |

```python
# 列表(可变)
my_list = [1, 2, 3]
my_list[0] = 100  # ✅ 可以修改

# 元组(不可变)
my_tuple = (1, 2, 3)
my_tuple[0] = 100  # ❌ TypeError: 'tuple' object does not support item assignment
```

---

## 2. 创建元组

### 2.1 基本创建

```python
# 空元组
empty = ()
empty = tuple()

# 单元素元组(必须有逗号!)
single = (1,)      # ✅ 正确
wrong = (1)        # ❌ 这是整数,不是元组
print(type(single))  # <class 'tuple'>
print(type(wrong))   # <class 'int'>

# 多元素元组
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# 省略括号(不推荐,但合法)
coords = 10, 20, 30
print(type(coords))  # <class 'tuple'>
```

### 2.2 从其他类型转换

```python
# 列表转元组
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# 字符串转元组
text = "hello"
chars = tuple(text)  # ('h', 'e', 'l', 'l', 'o')

# range 转元组
nums = tuple(range(5))  # (0, 1, 2, 3, 4)
```

---

## 3. 访问元组元素

### 3.1 索引访问

```python
fruits = ('apple', 'banana', 'cherry', 'date')

# 正向索引
print(fruits[0])   # 'apple'
print(fruits[2])   # 'cherry'

# 负向索引
print(fruits[-1])  # 'date'
print(fruits[-2])  # 'cherry'
```

### 3.2 切片操作

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(numbers[2:5])    # (2, 3, 4)
print(numbers[:3])     # (0, 1, 2)
print(numbers[7:])     # (7, 8, 9)
print(numbers[::2])    # (0, 2, 4, 6, 8)
print(numbers[::-1])   # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

---

## 4. 元组的方法

元组只有 **2 个方法**(因为不可变):

### 4.1 count() - 统计元素出现次数

```python
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))  # 3
print(numbers.count(10)) # 0
```

### 4.2 index() - 查找元素索引

```python
fruits = ('apple', 'banana', 'cherry', 'banana')

print(fruits.index('banana'))      # 1 (第一次出现的位置)
print(fruits.index('cherry'))      # 2

# 指定搜索范围
print(fruits.index('banana', 2))   # 3 (从索引2开始搜索)

# 元素不存在会报错
# print(fruits.index('grape'))     # ValueError
```

---

## 5. 元组操作

### 5.1 拼接

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# + 拼接(创建新元组)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)
```

### 5.2 重复

```python
t = (1, 2)
print(t * 3)  # (1, 2, 1, 2, 1, 2)
```

### 5.3 成员检查

```python
fruits = ('apple', 'banana', 'cherry')

print('apple' in fruits)   # True
print('grape' in fruits)   # False
print('grape' not in fruits)  # True
```

### 5.4 长度

```python
t = (1, 2, 3, 4, 5)
print(len(t))  # 5
```

---

## 6. 元组解包 (Unpacking)

### 6.1 基本解包

```python
# 基本解包
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# 多变量解包
person = ('Alice', 25, 'Engineer')
name, age, job = person
print(name, age, job)  # Alice 25 Engineer
```

### 6.2 使用 * 解包

```python
# * 收集剩余元素
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5] (注意:变成列表)

# 中间解包
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# 忽略某些值
x, _, z = (1, 2, 3)
print(x, z)  # 1 3
```

### 6.3 交换变量

```python
a = 10
b = 20

# 传统方式
temp = a
a = b
b = temp

# Python 方式(利用元组解包)
a, b = b, a
print(a, b)  # 20 10
```

---

## 7. 嵌套元组

```python
# 嵌套元组
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[0])      # (1, 2, 3)
print(matrix[1][2])   # 6

# 解包嵌套元组
point_3d = ((1, 2), 3)
(x, y), z = point_3d
print(x, y, z)  # 1 2 3
```

---

## 8. 元组 vs 列表

### 8.1 何时使用元组

✅ **使用元组的场景:**
- 数据不需要修改(如坐标、配置)
- 作为字典的键(列表不行)
- 函数返回多个值
- 性能要求高的场景

```python
# 坐标(不变)
position = (10, 20)

# 字典键
locations = {
    (0, 0): 'origin',
    (1, 0): 'right',
    (0, 1): 'up'
}

# 函数返回多值
def get_user():
    return ('Alice', 25, 'Engineer')

name, age, job = get_user()
```

### 8.2 何时使用列表

✅ **使用列表的场景:**
- 数据需要修改
- 需要添加/删除元素
- 需要排序

```python
# 购物车(会变化)
cart = ['apple', 'banana']
cart.append('orange')
```

---

## 9. 元组的不可变性

### 9.1 元组本身不可变

```python
t = (1, 2, 3)
# t[0] = 100  # ❌ TypeError
# t.append(4) # ❌ AttributeError
```

### 9.2 但元组内的可变对象可以修改

```python
# 元组包含列表
t = (1, 2, [3, 4])
print(t)  # (1, 2, [3, 4])

# 不能修改元组本身
# t[0] = 100  # ❌ 错误

# 但可以修改列表内容
t[2].append(5)
print(t)  # (1, 2, [3, 4, 5]) ✅ 可以!

# 元组的 id 没变
print(id(t))  # 地址不变
```

---

## 10. 元组推导式?

**注意:** Python 没有元组推导式!

```python
# 这不是元组推导式,是生成器表达式
gen = (x**2 for x in range(5))
print(type(gen))  # <class 'generator'>

# 要创建元组,需要转换
t = tuple(x**2 for x in range(5))
print(t)  # (0, 1, 4, 9, 16)
```

---

## 11. 常用内置函数

```python
numbers = (3, 1, 4, 1, 5, 9, 2, 6)

# 最大值/最小值
print(max(numbers))  # 9
print(min(numbers))  # 1

# 求和
print(sum(numbers))  # 31

# 排序(返回列表)
print(sorted(numbers))  # [1, 1, 2, 3, 4, 5, 6, 9]

# 反转(返回迭代器)
print(tuple(reversed(numbers)))  # (6, 2, 9, 5, 1, 4, 1, 3)

# 枚举
for i, val in enumerate(('a', 'b', 'c')):
    print(i, val)
# 0 a
# 1 b
# 2 c

# zip 组合
names = ('Alice', 'Bob', 'Charlie')
ages = (25, 30, 35)
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

---

## 12. 命名元组 (namedtuple)

普通元组的增强版,可以通过名字访问元素。

```python
from collections import namedtuple

# 定义命名元组
Point = namedtuple('Point', ['x', 'y'])

# 创建实例
p = Point(10, 20)

# 访问方式1: 索引
print(p[0])  # 10

# 访问方式2: 名字(更清晰)
print(p.x)   # 10
print(p.y)   # 20

# 解包
x, y = p
print(x, y)  # 10 20

# 转换为字典
print(p._asdict())  # {'x': 10, 'y': 20}
```

---

## 13. 性能对比

```python
import sys

# 内存占用
list_obj = [1, 2, 3, 4, 5]
tuple_obj = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_obj))   # 104 字节
print(sys.getsizeof(tuple_obj))  # 80 字节

# 元组更省内存!
```

---

## 14. 实用技巧

### 14.1 函数返回多值

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

data = [1, 2, 3, 4, 5]
min_val, max_val, total = get_stats(data)
print(f"最小:{min_val}, 最大:{max_val}, 总和:{total}")
```

### 14.2 作为字典键

```python
# 元组可以作为字典键(列表不行)
chess_board = {
    (0, 0): 'Rook',
    (0, 1): 'Knight',
    (0, 2): 'Bishop'
}

print(chess_board[(0, 1)])  # 'Knight'
```

### 14.3 多重赋值

```python
# 一行代码赋值多个变量
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3
```

---

## 15. 总结

| 操作 | 语法 | 说明 |
|------|------|------|
| 创建 | `(1, 2, 3)` | 圆括号 |
| 单元素 | `(1,)` | 必须有逗号 |
| 索引 | `t[0]` | 从 0 开始 |
| 切片 | `t[1:3]` | 左闭右开 |
| 拼接 | `t1 + t2` | 创建新元组 |
| 重复 | `t * 3` | 重复元素 |
| 成员 | `x in t` | 检查存在 |
| 长度 | `len(t)` | 元素个数 |
| 计数 | `t.count(x)` | 统计次数 |
| 查找 | `t.index(x)` | 查找索引 |
| 解包 | `a, b = t` | 多变量赋值 |

**核心特点:**
- ✅ 不可变(immutable)
- ✅ 有序(ordered)
- ✅ 可索引(indexable)
- ✅ 可迭代(iterable)
- ✅ 可作为字典键
- ✅ 性能优于列表
