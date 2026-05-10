# Python3 List 完整详细用法指南

## 目录
1. [List 基础](#list-基础)
2. [创建列表](#创建列表)
3. [访问列表元素](#访问列表元素)
4. [修改列表](#修改列表)
5. [列表方法详解](#列表方法详解)
6. [列表操作符](#列表操作符)
7. [列表推导式](#列表推导式)
8. [列表切片](#列表切片)
9. [列表遍历](#列表遍历)
10. [列表排序](#列表排序)
11. [列表复制](#列表复制)
12. [嵌套列表](#嵌套列表)
13. [内置函数](#内置函数)
14. [常用技巧](#常用技巧)
15. [性能分析](#性能分析)
16. [常见错误](#常见错误)

---

## List 基础

List（列表）是 Python 中最常用的数据结构之一，它是一个有序的、可变的集合，可以包含任意类型的元素。

**特点：**
- **有序性**：元素按照插入顺序排列，支持索引访问
- **可变性**：可以修改、添加、删除元素（mutable）
- **异构性**：可以包含不同类型的元素
- **动态性**：大小可以动态调整，无需预先声明大小
- **可嵌套**：列表可以包含其他列表
- **可重复**：允许重复元素

**内存结构：**
- 列表在内存中存储的是对象的引用，而不是对象本身
- 列表是动态数组实现，支持快速随机访问
- 时间复杂度：访问 O(1)，末尾添加 O(1)，插入/删除 O(n)

---

## 创建列表

### 1. 使用方括号 [] 创建

**语法：** `list_name = [element1, element2, ...]`

**特点：**
- 最常用、最直观的创建方式
- 可以包含任意类型的元素
- 可以创建空列表

```python
# 空列表
empty_list = []
print(type(empty_list))  # <class 'list'>

# 包含元素的列表
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# 混合类型列表
mixed = [1, 'hello', 3.14, True, None, [1, 2]]
print(mixed)  # [1, 'hello', 3.14, True, None, [1, 2]]

# 嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 2. 使用 list() 构造函数

**语法：** `list([iterable])`

**参数：**
- `iterable`（可选）：任何可迭代对象（字符串、元组、集合、字典、range等）
- 如果不提供参数，创建空列表

**返回值：** 返回一个新的列表对象

**时间复杂度：** O(n)，n 为可迭代对象的长度

```python
# 创建空列表
empty = list()
print(empty)  # []

# 从字符串创建（字符串是可迭代的）
chars = list('hello')
print(chars)  # ['h', 'e', 'l', 'l', 'o']

# 从元组创建
tuple_data = (1, 2, 3, 4, 5)
list_data = list(tuple_data)
print(list_data)  # [1, 2, 3, 4, 5]

# 从集合创建（注意：集合是无序的）
set_data = {3, 1, 2}
list_from_set = list(set_data)
print(list_from_set)  # [1, 2, 3] 或其他顺序

# 从字典创建（默认获取键）
dict_data = {'a': 1, 'b': 2, 'c': 3}
keys = list(dict_data)
print(keys)  # ['a', 'b', 'c']
values = list(dict_data.values())
print(values)  # [1, 2, 3]

# 从 range 创建
numbers = list(range(5))
print(numbers)  # [0, 1, 2, 3, 4]

numbers = list(range(1, 10, 2))
print(numbers)  # [1, 3, 5, 7, 9]

# 从生成器创建
gen = (x**2 for x in range(5))
squares = list(gen)
print(squares)  # [0, 1, 4, 9, 16]
```

**注意事项：**
- 传入非可迭代对象会引发 `TypeError`
- 字典默认迭代键，需要显式调用 `.values()` 或 `.items()` 获取值或键值对

```python
# 错误示例
try:
    list(123)  # TypeError: 'int' object is not iterable
except TypeError as e:
    print(f"错误: {e}")
```

### 3. 使用列表推导式

**语法：** `[expression for item in iterable if condition]`

**优点：**
- 代码简洁、可读性强
- 执行速度通常比等效的 for 循环快
- 可以包含条件过滤

```python
# 基本列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 带 if-else 的列表推导式
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# 多重循环
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

### 4. 使用 * 运算符创建重复列表

**语法：** `[element] * n`

**注意：** 对于可变对象（如列表），所有元素都是同一个对象的引用

```python
# 创建重复元素列表
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

# 注意：可变对象的陷阱
matrix = [[0] * 3] * 3  # 错误方式！
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] 所有行都被修改

# 正确方式：使用列表推导式
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] 只修改第一行
```

---

## 访问列表元素

### 1. 索引访问

**语法：** `list[index]`

**参数：**
- `index`：整数，表示元素位置
  - 正索引：从 0 开始，0 表示第一个元素
  - 负索引：从 -1 开始，-1 表示最后一个元素

**返回值：** 返回指定位置的元素

**异常：**
- `IndexError`：索引超出范围时抛出

**时间复杂度：** O(1)

```python
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

# 正向索引（从 0 开始）
print(fruits[0])   # 'apple' - 第一个元素
print(fruits[2])   # 'orange' - 第三个元素
print(fruits[4])   # 'mango' - 第五个元素

# 负向索引（从 -1 开始）
print(fruits[-1])  # 'mango' - 最后一个元素
print(fruits[-2])  # 'grape' - 倒数第二个元素
print(fruits[-5])  # 'apple' - 倒数第五个元素

# 索引越界错误
try:
    print(fruits[10])  # IndexError: list index out of range
except IndexError as e:
    print(f"错误: {e}")

try:
    print(fruits[-10])  # IndexError: list index out of range
except IndexError as e:
    print(f"错误: {e}")

# 动态索引
index = 2
print(fruits[index])  # 'orange'

# 使用变量计算索引
last_index = len(fruits) - 1
print(fruits[last_index])  # 'mango'
```

**索引对应关系：**
```
列表: ['apple', 'banana', 'orange', 'grape', 'mango']
正索引:   0        1         2        3        4
负索引:  -5       -4        -3       -2       -1
```

### 2. 切片访问

**语法：** `list[start:stop:step]`

**参数：**
- `start`（可选）：起始索引（包含），默认为 0
- `stop`（可选）：结束索引（不包含），默认为列表长度
- `step`（可选）：步长，默认为 1
  - 正数：从左到右
  - 负数：从右到左

**返回值：** 返回一个新的列表（浅拷贝）

**特点：**
- 切片不会引发 `IndexError`，超出范围会自动调整
- 返回新列表，不影响原列表
- 支持负索引

**时间复杂度：** O(k)，k 为切片长度

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基本切片 [start:stop]
print(numbers[2:5])      # [2, 3, 4] - 索引 2 到 4
print(numbers[0:3])      # [0, 1, 2] - 前 3 个元素

# 省略 start（从开头开始）
print(numbers[:5])       # [0, 1, 2, 3, 4] - 前 5 个元素
print(numbers[:])        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - 完整复制

# 省略 stop（到末尾结束）
print(numbers[5:])       # [5, 6, 7, 8, 9] - 从索引 5 到末尾
print(numbers[7:])       # [7, 8, 9]

# 使用步长 [start:stop:step]
print(numbers[::2])      # [0, 2, 4, 6, 8] - 每隔一个元素
print(numbers[1::2])     # [1, 3, 5, 7, 9] - 从索引 1 开始，每隔一个
print(numbers[::3])      # [0, 3, 6, 9] - 每隔两个元素
print(numbers[2:8:2])    # [2, 4, 6] - 索引 2 到 7，步长 2

# 负步长（反向）
print(numbers[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - 反转列表
print(numbers[::-2])     # [9, 7, 5, 3, 1] - 反向每隔一个
print(numbers[8:2:-1])   # [8, 7, 6, 5, 4, 3] - 从索引 8 到 3，反向
print(numbers[5::-1])    # [5, 4, 3, 2, 1, 0] - 从索引 5 反向到开头

# 负索引切片
print(numbers[-5:-2])    # [5, 6, 7] - 倒数第 5 到倒数第 3
print(numbers[-5:])      # [5, 6, 7, 8, 9] - 最后 5 个元素
print(numbers[:-3])      # [0, 1, 2, 3, 4, 5, 6] - 除了最后 3 个
print(numbers[-7:-2:2])  # [3, 5, 7]

# 超出范围的切片（不会报错）
print(numbers[5:100])    # [5, 6, 7, 8, 9] - 自动调整到列表末尾
print(numbers[-100:3])   # [0, 1, 2] - 自动调整到列表开头
print(numbers[100:200])  # [] - 返回空列表

# 空切片
print(numbers[5:2])      # [] - start > stop 返回空列表
print(numbers[5:5])      # [] - start == stop 返回空列表
```

**切片常用模式：**
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 复制列表
copy = lst[:]

# 反转列表
reversed_lst = lst[::-1]

# 获取前 n 个元素
first_n = lst[:n]

# 获取后 n 个元素
last_n = lst[-n:]

# 删除前 n 个元素
without_first_n = lst[n:]

# 删除后 n 个元素
without_last_n = lst[:-n]

# 获取奇数位置元素
odd_positions = lst[1::2]

# 获取偶数位置元素
even_positions = lst[::2]
```

---

## 修改列表

### 1. 修改单个元素

**语法：** `list[index] = new_value`

**参数：**
- `index`：要修改的元素索引
- `new_value`：新的值（任意类型）

**异常：**
- `IndexError`：索引超出范围

**时间复杂度：** O(1)

```python
fruits = ['apple', 'banana', 'orange']

# 修改单个元素
fruits[1] = 'mango'
print(fruits)  # ['apple', 'mango', 'orange']

# 使用负索引修改
fruits[-1] = 'grape'
print(fruits)  # ['apple', 'mango', 'grape']

# 修改为不同类型
fruits[0] = 123
print(fruits)  # [123, 'mango', 'grape']

# 索引越界会报错
try:
    fruits[10] = 'kiwi'  # IndexError
except IndexError as e:
    print(f"错误: {e}")
```

### 2. 修改切片

**语法：** `list[start:stop] = iterable`

**参数：**
- `start:stop`：要替换的切片范围
- `iterable`：任何可迭代对象

**特点：**
- 可以用不同长度的序列替换
- 可以插入或删除元素
- 右侧必须是可迭代对象

**时间复杂度：** O(n)

```python
numbers = [1, 2, 3, 4, 5]

# 替换切片（相同长度）
numbers[1:4] = [20, 30, 40]
print(numbers)  # [1, 20, 30, 40, 5]

# 替换为更短的序列
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [99]
print(numbers)  # [1, 99, 5]

# 替换为更长的序列
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [10, 20, 30, 40]
print(numbers)  # [1, 10, 20, 30, 40, 4, 5]

# 在指定位置插入（不删除）
numbers = [1, 2, 3, 4, 5]
numbers[2:2] = [99, 88]
print(numbers)  # [1, 2, 99, 88, 3, 4, 5]

# 删除切片（赋值为空列表）
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []
print(numbers)  # [1, 5]

# 使用字符串（可迭代对象）
letters = ['a', 'b', 'c']
letters[1:2] = 'xyz'
print(letters)  # ['a', 'x', 'y', 'z', 'c']

# 错误：右侧必须是可迭代对象
try:
    numbers[1:3] = 100  # TypeError
except TypeError as e:
    print(f"错误: {e}")
```

### 3. 使用 del 删除元素

**语法：** `del list[index]` 或 `del list[start:stop]`

**参数：**
- `index`：要删除的元素索引
- `start:stop`：要删除的切片范围

**特点：**
- 直接修改原列表
- 可以删除单个元素或切片
- 可以删除整个列表对象

**异常：**
- `IndexError`：索引超出范围（单个元素）
- `NameError`：删除列表后访问（del 整个列表）

**时间复杂度：** 
- 删除单个元素：O(n)
- 删除切片：O(n)

```python
# 删除单个元素
fruits = ['apple', 'banana', 'orange', 'grape']
del fruits[1]
print(fruits)  # ['apple', 'orange', 'grape']

# 使用负索引删除
del fruits[-1]
print(fruits)  # ['apple', 'orange']

# 删除切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:5]
print(numbers)  # [0, 1, 5, 6, 7, 8, 9]

# 删除带步长的切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]  # 删除所有偶数索引的元素
print(numbers)  # [1, 3, 5, 7, 9]

# 删除整个列表对象
my_list = [1, 2, 3]
del my_list
try:
    print(my_list)  # NameError: name 'my_list' is not defined
except NameError as e:
    print(f"错误: {e}")

# 索引越界
fruits = ['apple', 'banana']
try:
    del fruits[10]  # IndexError
except IndexError as e:
    print(f"错误: {e}")
```

---

## 列表方法详解

### 1. append() - 在末尾添加元素

**语法：** `list.append(object)`

**参数：**
- `object`：要添加的元素（任意类型）

**返回值：** `None`（直接修改原列表）

**时间复杂度：** O(1) 平摊

**特点：**
- 只能添加一个元素
- 如果添加列表，整个列表作为一个元素
- 修改原列表，不返回新列表

```python
fruits = ['apple', 'banana']

# 添加单个元素
fruits.append('orange')
print(fruits)  # ['apple', 'banana', 'orange']

# 添加不同类型
fruits.append(123)
print(fruits)  # ['apple', 'banana', 'orange', 123]

# 添加列表（作为单个元素）
fruits.append(['grape', 'mango'])
print(fruits)  # ['apple', 'banana', 'orange', 123, ['grape', 'mango']]

# append() 返回 None
result = fruits.append('kiwi')
print(result)  # None

# 常见错误：链式调用
numbers = [1, 2, 3]
# 错误：numbers.append(4).append(5)  # AttributeError
# 正确：
numbers.append(4)
numbers.append(5)
print(numbers)  # [1, 2, 3, 4, 5]
```

### 2. insert() - 在指定位置插入元素

**语法：** `list.insert(index, object)`

**参数：**
- `index`：插入位置的索引（整数）
  - 如果 index >= len(list)，在末尾插入
  - 如果 index < 0，从末尾计数
- `object`：要插入的元素（任意类型）

**返回值：** `None`（直接修改原列表）

**时间复杂度：** O(n)

**特点：**
- 在指定位置之前插入
- 不会替换现有元素
- 索引超出范围不会报错

```python
fruits = ['apple', 'banana', 'orange']

# 在索引 1 处插入
fruits.insert(1, 'mango')
print(fruits)  # ['apple', 'mango', 'banana', 'orange']

# 在开头插入
fruits.insert(0, 'grape')
print(fruits)  # ['grape', 'apple', 'mango', 'banana', 'orange']

# 在末尾插入（索引超出范围）
fruits.insert(100, 'kiwi')
print(fruits)  # ['grape', 'apple', 'mango', 'banana', 'orange', 'kiwi']

# 使用负索引
fruits = ['apple', 'banana', 'orange']
fruits.insert(-1, 'mango')  # 在倒数第一个元素之前插入
print(fruits)  # ['apple', 'banana', 'mango', 'orange']

# 插入列表（作为单个元素）
numbers = [1, 2, 3]
numbers.insert(1, [99, 88])
print(numbers)  # [1, [99, 88], 2, 3]

# 性能注意：在开头插入效率低
# 大量插入操作考虑使用 collections.deque
```

### 3. extend() - 扩展列表（添加多个元素）

**语法：** `list.extend(iterable)`

**参数：**
- `iterable`：任何可迭代对象（列表、元组、字符串、集合等）

**返回值：** `None`（直接修改原列表）

**时间复杂度：** O(k)，k 为可迭代对象的长度

**特点：**
- 将可迭代对象的所有元素添加到列表末尾
- 与 append() 不同，extend() 会展开可迭代对象
- 等价于 `list += iterable`

```python
fruits = ['apple', 'banana']

# 扩展列表
fruits.extend(['orange', 'grape'])
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

# 使用元组扩展
fruits.extend(('kiwi', 'mango'))
print(fruits)  # ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango']

# 使用字符串扩展（字符串是可迭代的）
letters = ['a', 'b']
letters.extend('cd')
print(letters)  # ['a', 'b', 'c', 'd']

# 使用集合扩展
numbers = [1, 2, 3]
numbers.extend({4, 5, 6})
print(numbers)  # [1, 2, 3, 4, 5, 6] 或其他顺序（集合无序）

# 使用生成器扩展
numbers = [1, 2, 3]
numbers.extend(x**2 for x in range(3))
print(numbers)  # [1, 2, 3, 0, 1, 4]

# extend() vs append()
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]] - 列表作为单个元素

list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5] - 列表被展开

# 使用 += 运算符（等价于 extend）
list3 = [1, 2, 3]
list3 += [4, 5]
print(list3)  # [1, 2, 3, 4, 5]

# 错误：传入非可迭代对象
try:
    numbers.extend(100)  # TypeError
except TypeError as e:
    print(f"错误: {e}")
```

### 4. remove() - 删除指定值的第一个匹配项

**语法：** `list.remove(value)`

**参数：**
- `value`：要删除的值（任意类型）

**返回值：** `None`（直接修改原列表）

**异常：**
- `ValueError`：如果值不存在于列表中

**时间复杂度：** O(n)

**特点：**
- 只删除第一个匹配的元素
- 如果有多个相同值，只删除第一个
- 值不存在会抛出异常

```python
fruits = ['apple', 'banana', 'orange', 'banana']

# 删除第一个匹配项
fruits.remove('banana')
print(fruits)  # ['apple', 'orange', 'banana'] - 只删除第一个

# 删除剩余的 'banana'
fruits.remove('banana')
print(fruits)  # ['apple', 'orange']

# 值不存在会报错
try:
    fruits.remove('grape')  # ValueError
except ValueError as e:
    print(f"错误: {e}")

# 安全删除（先检查是否存在）
fruits = ['apple', 'banana', 'orange']
if 'grape' in fruits:
    fruits.remove('grape')
else:
    print("'grape' 不在列表中")

# 删除所有匹配项
numbers = [1, 2, 3, 2, 4, 2, 5]
while 2 in numbers:
    numbers.remove(2)
print(numbers)  # [1, 3, 4, 5]

# 或使用列表推导式（更高效）
numbers = [1, 2, 3, 2, 4, 2, 5]
numbers = [x for x in numbers if x != 2]
print(numbers)  # [1, 3, 4, 5]
```

### 5. pop() - 删除并返回指定位置的元素

**语法：** `list.pop([index])`

**参数：**
- `index`（可选）：要删除的元素索引（整数）
  - 默认值：-1（最后一个元素）
  - 支持负索引

**返回值：** 被删除的元素

**异常：**
- `IndexError`：索引超出范围或列表为空

**时间复杂度：** 
- pop()：O(1)
- pop(0)：O(n)

**特点：**
- 删除并返回元素（与 remove() 不同）
- 常用于实现栈（LIFO）
- 默认删除最后一个元素

```python
fruits = ['apple', 'banana', 'orange']

# 删除并返回最后一个元素
last = fruits.pop()
print(last)    # 'orange'
print(fruits)  # ['apple', 'banana']

# 删除并返回指定位置的元素
first = fruits.pop(0)
print(first)   # 'apple'
print(fruits)  # ['banana']

# 使用负索引
numbers = [1, 2, 3, 4, 5]
second_last = numbers.pop(-2)
print(second_last)  # 4
print(numbers)      # [1, 2, 3, 5]

# 空列表 pop() 会报错
empty = []
try:
    empty.pop()  # IndexError: pop from empty list
except IndexError as e:
    print(f"错误: {e}")

# 索引越界
numbers = [1, 2, 3]
try:
    numbers.pop(10)  # IndexError
except IndexError as e:
    print(f"错误: {e}")

# 实现栈（LIFO - 后进先出）
stack = []
stack.append(1)  # 压栈
stack.append(2)
stack.append(3)
print(stack.pop())  # 3 - 弹栈
print(stack.pop())  # 2
print(stack)        # [1]

# 实现队列（FIFO - 先进先出）- 不推荐，效率低
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.pop(0))  # 1 - O(n) 操作
# 推荐使用 collections.deque 实现队列
```

### 6. clear() - 清空列表

**语法：** `list.clear()`

**参数：** 无

**返回值：** `None`（直接修改原列表）

**时间复杂度：** O(n)

**特点：**
- 删除所有元素
- 等价于 `del list[:]` 或 `list[:] = []`
- 列表对象仍然存在，只是变为空列表

```python
fruits = ['apple', 'banana', 'orange']

# 清空列表
fruits.clear()
print(fruits)  # []
print(type(fruits))  # <class 'list'>

# 等价操作
numbers = [1, 2, 3, 4, 5]
del numbers[:]
print(numbers)  # []

numbers = [1, 2, 3, 4, 5]
numbers[:] = []
print(numbers)  # []

# 注意：clear() vs 重新赋值
list1 = [1, 2, 3]
list2 = list1  # list2 引用 list1

list1.clear()  # 清空原列表
print(list1)  # []
print(list2)  # [] - list2 也被清空

list1 = [1, 2, 3]
list2 = list1

list1 = []  # 重新赋值，创建新列表
print(list1)  # []
print(list2)  # [1, 2, 3] - list2 不受影响
```

### 7. index() - 查找元素的索引

**语法：** `list.index(value[, start[, stop]])`

**参数：**
- `value`：要查找的值（任意类型）
- `start`（可选）：搜索起始位置，默认 0
- `stop`（可选）：搜索结束位置，默认列表长度

**返回值：** 第一个匹配项的索引（整数）

**异常：**
- `ValueError`：值不存在于列表中

**时间复杂度：** O(n)

**特点：**
- 返回第一个匹配项的索引
- 可以指定搜索范围
- 值不存在会抛出异常

```python
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']

# 查找第一个匹配项的索引
idx = fruits.index('banana')
print(idx)  # 1

# 指定搜索起始位置
idx = fruits.index('banana', 2)  # 从索引 2 开始搜索
print(idx)  # 3

# 指定搜索范围 [start, stop)
idx = fruits.index('banana', 0, 3)  # 在索引 0-2 范围内搜索
print(idx)  # 1

# 值不存在会报错
try:
    idx = fruits.index('kiwi')  # ValueError
except ValueError as e:
    print(f"错误: {e}")

# 安全查找
if 'kiwi' in fruits:
    idx = fruits.index('kiwi')
else:
    print("'kiwi' 不在列表中")

# 查找所有匹配项的索引
numbers = [1, 2, 3, 2, 4, 2, 5]
indices = [i for i, x in enumerate(numbers) if x == 2]
print(indices)  # [1, 3, 5]

# 在指定范围内查找
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
try:
    idx = fruits.index('grape', 0, 3)  # 在前 3 个元素中查找
except ValueError:
    print("'grape' 不在指定范围内")
```

### 8. count() - 统计元素出现次数

**语法：** `list.count(value)`

**参数：**
- `value`：要统计的值（任意类型）

**返回值：** 元素出现的次数（整数，>= 0）

**时间复杂度：** O(n)

**特点：**
- 返回值出现的总次数
- 值不存在返回 0（不抛出异常）
- 使用 == 比较元素

```python
numbers = [1, 2, 3, 2, 4, 2, 5, 2]

# 统计元素出现次数
count = numbers.count(2)
print(count)  # 4

# 元素不存在返回 0
count = numbers.count(10)
print(count)  # 0

# 统计字符串
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
count = fruits.count('apple')
print(count)  # 3

# 统计列表中的列表
nested = [[1, 2], [3, 4], [1, 2], [5, 6]]
count = nested.count([1, 2])
print(count)  # 2

# 统计所有元素的出现次数
numbers = [1, 2, 3, 2, 4, 2, 5, 1]
from collections import Counter
counts = Counter(numbers)
print(counts)  # Counter({2: 3, 1: 2, 3: 1, 4: 1, 5: 1})

# 或使用字典
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1
print(counts)  # {1: 2, 2: 3, 3: 1, 4: 1, 5: 1}

# 找出出现次数最多的元素
most_common = max(set(numbers), key=numbers.count)
print(most_common)  # 2
```

### 9. sort() - 原地排序列表

**语法：** `list.sort(*, key=None, reverse=False)`

**参数：**
- `key`（可选）：指定一个函数，用于从每个元素中提取比较键
  - 默认值：None（直接比较元素）
  - 常用：`len`, `str.lower`, `abs`, lambda 函数
- `reverse`（可选）：布尔值，是否降序排序
  - 默认值：False（升序）
  - True：降序

**返回值：** `None`（直接修改原列表）

**异常：**
- `TypeError`：元素类型不可比较

**时间复杂度：** O(n log n)

**特点：**
- 原地排序，修改原列表
- 稳定排序（相等元素保持原有顺序）
- 使用 Timsort 算法

```python
# 基本排序（升序）
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# 降序排序
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# 按字符串长度排序
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)
print(words)  # ['pie', 'book', 'banana', 'Washington']

# 忽略大小写排序
words = ['banana', 'Pie', 'Washington', 'book']
words.sort(key=str.lower)
print(words)  # ['banana', 'book', 'Pie', 'Washington']

# 使用 lambda 函数
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1])  # 按分数排序
print(students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# 降序排序
students.sort(key=lambda x: x[1], reverse=True)
print(students)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 多级排序（先按年龄，再按姓名）
people = [('Alice', 25), ('Bob', 30), ('Charlie', 25)]
people.sort(key=lambda x: (x[1], x[0]))
print(people)  # [('Alice', 25), ('Charlie', 25), ('Bob', 30)]

# 按绝对值排序
numbers = [-5, 2, -3, 8, -1]
numbers.sort(key=abs)
print(numbers)  # [-1, 2, -3, -5, 8]

# 自定义排序函数
def custom_key(x):
    return x % 10  # 按个位数排序

numbers = [23, 15, 42, 37, 19]
numbers.sort(key=custom_key)
print(numbers)  # [42, 23, 15, 37, 19]

# 错误：不可比较的类型
mixed = [1, 'hello', 3.14]
try:
    mixed.sort()  # TypeError
except TypeError as e:
    print(f"错误: {e}")

# sort() 返回 None
numbers = [3, 1, 4]
result = numbers.sort()
print(result)  # None
print(numbers)  # [1, 3, 4]

# 常见错误：链式调用
# 错误：numbers = [3, 1, 4].sort()  # numbers 会是 None
# 正确：
numbers = [3, 1, 4]
numbers.sort()
```

### 10. reverse() - 反转列表

**语法：** `list.reverse()`

**参数：** 无

**返回值：** `None`（直接修改原列表）

**时间复杂度：** O(n)

**特点：**
- 原地反转，修改原列表
- 不创建新列表
- 等价于 `list[::-1]`（但后者创建新列表）

```python
# 基本反转
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# 字符串列表反转
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)  # ['orange', 'banana', 'apple']

# reverse() 返回 None
numbers = [1, 2, 3]
result = numbers.reverse()
print(result)  # None
print(numbers)  # [3, 2, 1]

# reverse() vs 切片反转
list1 = [1, 2, 3, 4, 5]
list1.reverse()  # 原地修改
print(list1)  # [5, 4, 3, 2, 1]

list2 = [1, 2, 3, 4, 5]
list3 = list2[::-1]  # 创建新列表
print(list2)  # [1, 2, 3, 4, 5] - 原列表不变
print(list3)  # [5, 4, 3, 2, 1] - 新列表

# 使用 reversed() 函数（返回迭代器）
numbers = [1, 2, 3, 4, 5]
reversed_iter = reversed(numbers)
print(list(reversed_iter))  # [5, 4, 3, 2, 1]
print(numbers)  # [1, 2, 3, 4, 5] - 原列表不变

# 反转后再反转
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
numbers.reverse()
print(numbers)  # [1, 2, 3, 4, 5] - 恢复原状
```

### 11. copy() - 复制列表（浅拷贝）

**语法：** `list.copy()`

**参数：** 无

**返回值：** 列表的浅拷贝（新列表对象）

**时间复杂度：** O(n)

**特点：**
- 创建新列表对象
- 浅拷贝：只复制第一层元素的引用
- 等价于 `list[:]` 或 `list(list)`

```python
# 基本复制
original = [1, 2, 3]
copied = original.copy()

# 修改副本不影响原列表
copied[0] = 100
print(original)  # [1, 2, 3]
print(copied)    # [100, 2, 3]

# 浅拷贝的限制（嵌套列表）
original = [[1, 2], [3, 4]]
copied = original.copy()

# 修改嵌套列表会影响原列表
copied[0][0] = 100
print(original)  # [[100, 2], [3, 4]] - 原列表也被修改
print(copied)    # [[100, 2], [3, 4]]

# 深拷贝（使用 copy 模块）
import copy
original = [[1, 2], [3, 4]]
deep_copied = copy.deepcopy(original)

deep_copied[0][0] = 100
print(original)     # [[1, 2], [3, 4]] - 原列表不受影响
print(deep_copied)  # [[100, 2], [3, 4]]

# 不同的复制方法
original = [1, 2, 3]

# 方法1：copy() 方法
copy1 = original.copy()

# 方法2：切片
copy2 = original[:]

# 方法3：list() 构造函数
copy3 = list(original)

# 方法4：copy 模块
import copy
copy4 = copy.copy(original)

# 所有方法都创建新对象
print(copy1 is original)  # False
print(copy2 is original)  # False
print(copy3 is original)  # False
print(copy4 is original)  # False

# 赋值不是复制
original = [1, 2, 3]
reference = original  # 只是创建引用

reference[0] = 100
print(original)   # [100, 2, 3] - 原列表被修改
print(reference)  # [100, 2, 3]
print(reference is original)  # True - 同一个对象
```

---

## 列表操作符

### 1. 连接列表

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 使用 + 运算符
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]
```

### 2. 重复列表

```python
numbers = [1, 2, 3]
repeated = numbers * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 3. 成员检查

```python
fruits = ['apple', 'banana', 'orange']

print('apple' in fruits)      # True
print('grape' in fruits)      # False
print('grape' not in fruits)  # True
```

### 4. 列表长度

```python
fruits = ['apple', 'banana', 'orange']
length = len(fruits)
print(length)  # 3
```

### 5. 最大值、最小值、求和

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

print(max(numbers))  # 9
print(min(numbers))  # 1
print(sum(numbers))  # 25
```

---

## 列表推导式

列表推导式提供了一种简洁的方式来创建列表。

### 1. 基本语法

```python
# 语法：[expression for item in iterable]
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2. 带条件的列表推导式

```python
# 语法：[expression for item in iterable if condition]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

### 3. 多重循环

```python
# 笛卡尔积
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
```

### 4. 嵌套列表推导式

```python
# 创建矩阵
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 转置矩阵
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

## 列表切片

切片是访问列表子序列的强大工具。

### 语法：list[start:end:step]

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基本切片
print(numbers[2:7])      # [2, 3, 4, 5, 6]
print(numbers[:5])       # [0, 1, 2, 3, 4]
print(numbers[5:])       # [5, 6, 7, 8, 9]
print(numbers[:])        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 完整复制

# 步长切片
print(numbers[::2])      # [0, 2, 4, 6, 8] 每隔一个
print(numbers[1::2])     # [1, 3, 5, 7, 9] 奇数位置
print(numbers[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 反转
print(numbers[::-2])     # [9, 7, 5, 3, 1] 反向每隔一个

# 负索引切片
print(numbers[-5:-2])    # [5, 6, 7]
print(numbers[-5:])      # [5, 6, 7, 8, 9]
```

---

## 列表遍历

### 1. 使用 for 循环

```python
fruits = ['apple', 'banana', 'orange']

# 遍历元素
for fruit in fruits:
    print(fruit)
```

### 2. 使用 enumerate() 获取索引和值

```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 输出：
# 0: apple
# 1: banana
# 2: orange

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

### 3. 使用 zip() 同时遍历多个列表

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['Beijing', 'Shanghai', 'Guangzhou']

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
```

### 4. 使用 while 循环

```python
fruits = ['apple', 'banana', 'orange']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

---

## 列表排序

### 1. sort() 方法 - 原地排序

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# 降序
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]
```

### 2. sorted() 函数 - 返回新列表

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(numbers)         # [3, 1, 4, 1, 5, 9, 2] 原列表不变
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

### 3. 自定义排序

```python
# 按字符串长度排序
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)
print(words)  # ['pie', 'book', 'banana', 'Washington']

# 按元组的第二个元素排序
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

---

## 列表复制

### 1. 浅拷贝

```python
# 方法1：使用切片
original = [1, 2, 3]
copied = original[:]

# 方法2：使用 copy() 方法
copied = original.copy()

# 方法3：使用 list() 构造函数
copied = list(original)

# 方法4：使用 copy 模块
import copy
copied = copy.copy(original)
```

### 2. 深拷贝（用于嵌套列表）

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

# 修改嵌套列表
original[0][0] = 100

print(original)  # [[100, 2], [3, 4]]
print(shallow)   # [[100, 2], [3, 4]] 浅拷贝受影响
print(deep)      # [[1, 2], [3, 4]] 深拷贝不受影响
```

---

## 嵌套列表

### 1. 创建二维列表

```python
# 方法1：直接创建
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 方法2：使用列表推导式
matrix = [[i*3 + j + 1 for j in range(3)] for i in range(3)]
```

### 2. 访问嵌套列表元素

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6
```

### 3. 遍历嵌套列表

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 遍历所有元素
for row in matrix:
    for element in row:
        print(element, end=' ')
# 输出：1 2 3 4 5 6 7 8 9

# 使用索引遍历
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

---

## 常用技巧

### 1. 列表去重

```python
# 方法1：使用 set（不保持顺序）
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))

# 方法2：保持顺序
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

# 方法3：使用字典（Python 3.7+保持插入顺序）
unique = list(dict.fromkeys(numbers))
```

### 2. 列表展平

```python
# 展平二维列表
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# 使用 itertools
import itertools
flattened = list(itertools.chain.from_iterable(nested))
```

### 3. 列表分组

```python
# 将列表分成固定大小的块
def chunk_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunks = chunk_list(numbers, 3)
print(chunks)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 4. 列表过滤

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用列表推导式
even = [x for x in numbers if x % 2 == 0]

# 使用 filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
```

### 5. 列表映射

```python
numbers = [1, 2, 3, 4, 5]

# 使用列表推导式
squares = [x**2 for x in numbers]

# 使用 map()
squares = list(map(lambda x: x**2, numbers))
```

### 6. 列表合并字典

```python
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Beijing']

# 使用 zip() 和 dict()
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
```

### 7. 查找列表中的最大/最小元素及其索引

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# 最大值及索引
max_value = max(numbers)
max_index = numbers.index(max_value)
print(f"最大值: {max_value}, 索引: {max_index}")

# 使用 enumerate
max_index, max_value = max(enumerate(numbers), key=lambda x: x[1])
```

### 8. 列表元素累加

```python
# 使用 itertools.accumulate
import itertools

numbers = [1, 2, 3, 4, 5]
cumsum = list(itertools.accumulate(numbers))
print(cumsum)  # [1, 3, 6, 10, 15]
```

### 9. 列表元素交换

```python
lst = [1, 2, 3, 4, 5]

# 交换两个元素
lst[0], lst[4] = lst[4], lst[0]
print(lst)  # [5, 2, 3, 4, 1]
```

### 10. 检查列表是否为空

```python
my_list = []

# 方法1：直接判断
if not my_list:
    print("列表为空")

# 方法2：使用 len()
if len(my_list) == 0:
    print("列表为空")
```

---

## 性能注意事项

1. **append() vs insert(0)**：在列表末尾添加元素（append）是 O(1)，在开头插入（insert(0)）是 O(n)
2. **in 操作**：检查元素是否在列表中是 O(n)，对于大列表考虑使用 set
3. **列表推导式 vs 循环**：列表推导式通常比等效的 for 循环更快
4. **extend() vs +**：extend() 比使用 + 运算符更高效
5. **深拷贝开销**：深拷贝嵌套列表的开销较大，仅在必要时使用

---

## 总结

Python 的 list 是一个功能强大且灵活的数据结构，掌握其各种方法和操作技巧对于编写高效的 Python 代码至关重要。本文档涵盖了从基础到高级的各种用法，希望能帮助你更好地使用 Python 列表。

**核心要点：**
- 列表是可变的、有序的集合
- 支持丰富的内置方法和操作
- 列表推导式提供了简洁的创建方式
- 切片操作功能强大
- 注意浅拷贝和深拷贝的区别
- 考虑性能影响选择合适的操作方法

### 1. + 运算符 - 连接列表

**语法：** `list1 + list2`

**参数：**
- `list1`, `list2`：要连接的列表

**返回值：** 新列表（不修改原列表）

**异常：**
- `TypeError`：操作数必须都是列表

**时间复杂度：** O(n + m)

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 连接列表
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]
print(list1)   # [1, 2, 3] - 原列表不变

# 连接多个列表
list3 = [7, 8, 9]
result = list1 + list2 + list3
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 错误：不能与其他类型连接
try:
    result = list1 + 4  # TypeError
except TypeError as e:
    print(f"错误: {e}")
```

### 2. * 运算符 - 重复列表

**语法：** `list * n` 或 `n * list`

**参数：**
- `list`：要重复的列表
- `n`：重复次数（整数）

**返回值：** 新列表（不修改原列表）

**时间复杂度：** O(n * k)，k 为列表长度

```python
numbers = [1, 2, 3]
repeated = numbers * 3
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# n * list 也可以
repeated = 3 * numbers
print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 重复 0 次或负数次
print(numbers * 0)   # []
print(numbers * -1)  # []
```

### 3. in 和 not in - 成员检查

**语法：** `value in list` 或 `value not in list`

**返回值：** 布尔值

**时间复杂度：** O(n)

```python
fruits = ['apple', 'banana', 'orange']

print('apple' in fruits)      # True
print('grape' in fruits)      # False
print('grape' not in fruits)  # True

# 用于条件判断
if 'apple' in fruits:
    print("找到苹果")
```

### 4. += 运算符 - 原地扩展

**语法：** `list += iterable`

**特点：**
- 等价于 `list.extend(iterable)`
- 原地修改列表
- 与 `list = list + iterable` 不同

```python
numbers = [1, 2, 3]
numbers += [4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

# += vs +
list1 = [1, 2, 3]
list2 = list1
list1 += [4, 5]  # 原地修改
print(list1)  # [1, 2, 3, 4, 5]
print(list2)  # [1, 2, 3, 4, 5] - list2 也被修改

list1 = [1, 2, 3]
list2 = list1
list1 = list1 + [4, 5]  # 创建新列表
print(list1)  # [1, 2, 3, 4, 5]
print(list2)  # [1, 2, 3] - list2 不受影响
```

### 5. *= 运算符 - 原地重复

**语法：** `list *= n`

**特点：**
- 原地修改列表
- 等价于 `list = list * n`（但更高效）

```python
numbers = [1, 2, 3]
numbers *= 3
print(numbers)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 6. 比较运算符

**语法：** `list1 == list2`, `list1 != list2`, `list1 < list2` 等

**特点：**
- 按字典序比较
- 逐元素比较

```python
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] != [1, 2, 4])  # True
print([1, 2, 3] < [1, 2, 4])   # True
print([1, 2] < [1, 2, 3])      # True
```

---

## 列表推导式

**语法：** `[expression for item in iterable if condition]`

**优点：**
- 代码简洁、可读性强
- 执行速度快
- 可以包含条件过滤

### 1. 基本列表推导式

```python
# 生成平方数
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 转换字符串
words = ['hello', 'world']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD']
```

### 2. 带条件的列表推导式

```python
# 过滤偶数
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 过滤并转换
positive_squares = [x**2 for x in range(-5, 6) if x > 0]
print(positive_squares)  # [1, 4, 9, 16, 25]
```

### 3. 带 if-else 的列表推导式

```python
# 标记奇偶
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even']

# 替换负数为 0
numbers = [-2, 3, -1, 5, -4]
result = [x if x > 0 else 0 for x in numbers]
print(result)  # [0, 3, 0, 5, 0]
```

### 4. 嵌套列表推导式

```python
# 创建矩阵
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 展平二维列表
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

### 5. 多重循环

```python
# 笛卡尔积
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# 带条件的多重循环
result = [(x, y) for x in range(5) for y in range(5) if x + y == 4]
print(result)  # [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
```

---

## 内置函数

### 1. len() - 获取列表长度

**语法：** `len(list)`

**返回值：** 列表元素个数（整数）

**时间复杂度：** O(1)

```python
fruits = ['apple', 'banana', 'orange']
print(len(fruits))  # 3

empty = []
print(len(empty))  # 0
```

### 2. max() - 获取最大值

**语法：** `max(list[, key=func])`

**参数：**
- `list`：列表
- `key`（可选）：指定比较函数

**返回值：** 最大元素

**异常：**
- `ValueError`：空列表
- `TypeError`：元素不可比较

**时间复杂度：** O(n)

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
print(max(numbers))  # 9

# 使用 key 参数
words = ['banana', 'pie', 'Washington']
print(max(words, key=len))  # 'Washington'

# 空列表报错
try:
    max([])  # ValueError
except ValueError as e:
    print(f"错误: {e}")
```

### 3. min() - 获取最小值

**语法：** `min(list[, key=func])`

**参数和特点与 max() 相同**

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
print(min(numbers))  # 1

words = ['banana', 'pie', 'Washington']
print(min(words, key=len))  # 'pie'
```

### 4. sum() - 求和

**语法：** `sum(list[, start])`

**参数：**
- `list`：数值列表
- `start`（可选）：初始值，默认 0

**返回值：** 总和

**异常：**
- `TypeError`：元素不是数值类型

**时间复杂度：** O(n)

```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15

# 指定初始值
print(sum(numbers, 10))  # 25

# 空列表
print(sum([]))  # 0

# 字符串列表不能求和
try:
    sum(['a', 'b'])  # TypeError
except TypeError as e:
    print(f"错误: {e}")
```

### 5. sorted() - 返回排序后的新列表

**语法：** `sorted(list[, key=func, reverse=False])`

**参数：**
- `list`：可迭代对象
- `key`（可选）：排序函数
- `reverse`（可选）：是否降序

**返回值：** 新的排序列表（不修改原列表）

**时间复杂度：** O(n log n)

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
print(numbers)         # [3, 1, 4, 1, 5, 9, 2] - 原列表不变

# 降序
print(sorted(numbers, reverse=True))  # [9, 5, 4, 3, 2, 1, 1]

# 使用 key
words = ['banana', 'pie', 'Washington']
print(sorted(words, key=len))  # ['pie', 'banana', 'Washington']
```

### 6. reversed() - 返回反转迭代器

**语法：** `reversed(list)`

**返回值：** 反转迭代器（不修改原列表）

**时间复杂度：** O(1)（创建迭代器），O(n)（遍历）

```python
numbers = [1, 2, 3, 4, 5]
reversed_iter = reversed(numbers)
print(list(reversed_iter))  # [5, 4, 3, 2, 1]
print(numbers)  # [1, 2, 3, 4, 5] - 原列表不变

# 直接遍历
for num in reversed(numbers):
    print(num, end=' ')  # 5 4 3 2 1
```

### 7. enumerate() - 枚举索引和值

**语法：** `enumerate(list[, start=0])`

**参数：**
- `list`：可迭代对象
- `start`（可选）：起始索引，默认 0

**返回值：** 枚举对象（迭代器）

```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 输出：
# 0: apple
# 1: banana
# 2: orange

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 输出：
# 1: apple
# 2: banana
# 3: orange

# 转换为列表
print(list(enumerate(fruits)))  # [(0, 'apple'), (1, 'banana'), (2, 'orange')]
```

### 8. zip() - 并行迭代多个列表

**语法：** `zip(*iterables)`

**参数：**
- `*iterables`：多个可迭代对象

**返回值：** zip 对象（迭代器）

**特点：**
- 以最短列表为准
- 返回元组

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['Beijing', 'Shanghai', 'Guangzhou']

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# 转换为列表
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# 长度不同时
list1 = [1, 2, 3]
list2 = ['a', 'b']
print(list(zip(list1, list2)))  # [(1, 'a'), (2, 'b')]

# 解压
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')
```

### 9. all() - 检查所有元素是否为真

**语法：** `all(list)`

**返回值：** 布尔值

**特点：**
- 所有元素为真返回 True
- 空列表返回 True

```python
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))            # True
print(all([1, 0, 3]))            # False
print(all([]))                   # True

# 检查所有数字是否为正
numbers = [1, 2, 3, 4, 5]
print(all(x > 0 for x in numbers))  # True
```

### 10. any() - 检查是否有元素为真

**语法：** `any(list)`

**返回值：** 布尔值

**特点：**
- 至少一个元素为真返回 True
- 空列表返回 False

```python
print(any([False, False, True]))  # True
print(any([False, False, False])) # False
print(any([0, 0, 1]))             # True
print(any([]))                    # False

# 检查是否有负数
numbers = [1, 2, -3, 4, 5]
print(any(x < 0 for x in numbers))  # True
```

### 11. filter() - 过滤元素

**语法：** `filter(function, list)`

**参数：**
- `function`：过滤函数（返回布尔值）
- `list`：可迭代对象

**返回值：** filter 对象（迭代器）

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 过滤偶数
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6, 8, 10]

# 过滤空字符串
words = ['hello', '', 'world', '', 'python']
non_empty = list(filter(None, words))  # None 表示过滤假值
print(non_empty)  # ['hello', 'world', 'python']
```

### 12. map() - 映射转换

**语法：** `map(function, *iterables)`

**参数：**
- `function`：转换函数
- `*iterables`：一个或多个可迭代对象

**返回值：** map 对象（迭代器）

```python
numbers = [1, 2, 3, 4, 5]

# 计算平方
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# 转换为字符串
str_numbers = list(map(str, numbers))
print(str_numbers)  # ['1', '2', '3', '4', '5']

# 多个列表
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)  # [11, 22, 33]
```

---

## 性能分析

### 时间复杂度总结

| 操作 | 平均时间复杂度 | 最坏时间复杂度 | 说明 |
|------|---------------|---------------|------|
| `list[i]` | O(1) | O(1) | 索引访问 |
| `list[i] = x` | O(1) | O(1) | 索引赋值 |
| `len(list)` | O(1) | O(1) | 获取长度 |
| `list.append(x)` | O(1) | O(1) | 末尾添加（平摊） |
| `list.pop()` | O(1) | O(1) | 删除末尾元素 |
| `list.pop(0)` | O(n) | O(n) | 删除首元素 |
| `list.insert(0, x)` | O(n) | O(n) | 开头插入 |
| `list.insert(i, x)` | O(n) | O(n) | 中间插入 |
| `list.remove(x)` | O(n) | O(n) | 删除指定值 |
| `x in list` | O(n) | O(n) | 成员检查 |
| `list.index(x)` | O(n) | O(n) | 查找索引 |
| `list.count(x)` | O(n) | O(n) | 统计出现次数 |
| `list.sort()` | O(n log n) | O(n log n) | 排序 |
| `list.reverse()` | O(n) | O(n) | 反转 |
| `list.copy()` | O(n) | O(n) | 复制 |
| `list.extend(iter)` | O(k) | O(k) | 扩展（k为iter长度） |
| `list1 + list2` | O(n+m) | O(n+m) | 连接 |
| `list * n` | O(n*k) | O(n*k) | 重复（k为list长度） |
| `list[i:j]` | O(j-i) | O(j-i) | 切片 |

### 性能优化建议

#### 1. 避免在开头插入/删除

```python
# 不推荐：O(n) 操作
my_list = []
for i in range(1000):
    my_list.insert(0, i)  # 每次都是 O(n)

# 推荐：使用 collections.deque
from collections import deque
my_deque = deque()
for i in range(1000):
    my_deque.appendleft(i)  # O(1) 操作
```

#### 2. 使用列表推导式代替循环

```python
# 不推荐：慢
result = []
for i in range(1000):
    result.append(i**2)

# 推荐：快
result = [i**2 for i in range(1000)]
```

#### 3. 预分配空间

```python
# 不推荐：多次扩容
my_list = []
for i in range(1000):
    my_list.append(i)

# 推荐：预分配
my_list = [None] * 1000
for i in range(1000):
    my_list[i] = i
```

#### 4. 使用 extend() 而不是 +

```python
# 不推荐：创建新列表
list1 = [1, 2, 3]
list1 = list1 + [4, 5, 6]

# 推荐：原地修改
list1 = [1, 2, 3]
list1.extend([4, 5, 6])
# 或
list1 += [4, 5, 6]
```

#### 5. 成员检查使用 set

```python
# 不推荐：O(n) 查找
my_list = list(range(10000))
if 5000 in my_list:  # O(n)
    print("找到了")

# 推荐：O(1) 查找
my_set = set(range(10000))
if 5000 in my_set:  # O(1)
    print("找到了")
```

---

## 常见错误

### 1. 索引越界

```python
my_list = [1, 2, 3]
try:
    print(my_list[10])  # IndexError
except IndexError as e:
    print(f"错误: {e}")

# 解决方案：先检查长度
if len(my_list) > 10:
    print(my_list[10])
```

### 2. 修改正在迭代的列表

```python
# 错误：迭代时修改列表
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # 可能跳过元素
print(numbers)  # [1, 3, 5] - 可能不是预期结果

# 正确方法1：使用列表推导式
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]

# 正确方法2：反向迭代
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)

# 正确方法3：复制列表
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # 迭代副本
    if num % 2 == 0:
        numbers.remove(num)
```

### 3. 浅拷贝陷阱

```python
# 错误：使用 * 创建嵌套列表
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - 所有行都被修改

# 正确：使用列表推导式
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 4. 混淆 append() 和 extend()

```python
# append() 添加单个元素
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]]

# extend() 展开添加
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5]
```

### 5. 忘记方法返回 None

```python
# 错误：sort() 返回 None
numbers = [3, 1, 4]
sorted_numbers = numbers.sort()
print(sorted_numbers)  # None

# 正确：sort() 原地修改
numbers = [3, 1, 4]
numbers.sort()
print(numbers)  # [1, 3, 4]

# 或使用 sorted() 返回新列表
numbers = [3, 1, 4]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 3, 4]
```

### 6. 列表作为默认参数

```python
# 错误：可变默认参数
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - 不是预期的 [2]

# 正确：使用 None 作为默认值
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [2]
```

### 7. 赋值 vs 复制

```python
# 错误：赋值只是创建引用
list1 = [1, 2, 3]
list2 = list1  # 引用同一个对象
list2[0] = 100
print(list1)  # [100, 2, 3] - list1 也被修改

# 正确：复制列表
list1 = [1, 2, 3]
list2 = list1.copy()  # 或 list1[:]
list2[0] = 100
print(list1)  # [1, 2, 3] - list1 不受影响
```

---

## 总结

### 核心要点

1. **列表特性**
   - 有序、可变、异构、动态
   - 支持索引和切片
   - 时间复杂度：访问 O(1)，插入/删除 O(n)

2. **常用方法**
   - 添加：`append()`, `insert()`, `extend()`
   - 删除：`remove()`, `pop()`, `clear()`
   - 查找：`index()`, `count()`
   - 排序：`sort()`, `reverse()`
   - 复制：`copy()`

3. **性能优化**
   - 避免在开头插入/删除
   - 使用列表推导式
   - 成员检查使用 set
   - 使用 extend() 而不是 +

4. **常见陷阱**
   - 索引越界
   - 迭代时修改列表
   - 浅拷贝问题
   - 可变默认参数
   - 赋值 vs 复制

5. **最佳实践**
   - 使用列表推导式提高可读性和性能
   - 选择合适的数据结构（list vs deque vs set）
   - 注意浅拷贝和深拷贝的区别
   - 避免修改正在迭代的列表
   - 使用内置函数和方法

### 何时使用列表

**适合使用列表：**
- 需要有序存储元素
- 需要通过索引快速访问
- 需要在末尾频繁添加/删除元素
- 元素可以重复

**不适合使用列表：**
- 需要在开头频繁插入/删除（使用 deque）
- 需要快速成员检查（使用 set）
- 需要键值对存储（使用 dict）
- 需要不可变序列（使用 tuple）

---

## 参考资源

- [Python 官方文档 - 列表](https://docs.python.org/3/tutorial/datastructures.html)
- [Python 官方文档 - 列表方法](https://docs.python.org/3/library/stdtypes.html#list)
- [Python 时间复杂度](https://wiki.python.org/moin/TimeComplexity)

---

**文档版本：** 1.0  
**适用版本：** Python 3.x  
**最后更新：** 2026-01-12
