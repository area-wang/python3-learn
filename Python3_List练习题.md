# Python3 List 练习题集

## 目录
1. [创建列表](#创建列表)
2. [访问列表元素](#访问列表元素)
3. [修改列表](#修改列表)
4. [列表方法 - append/insert/extend](#列表方法---appendinsertextend)
5. [列表方法 - remove/pop/clear](#列表方法---removepoplear)
6. [列表方法 - index/count](#列表方法---indexcount)
7. [列表方法 - sort/reverse/copy](#列表方法---sortreversecopy)
8. [列表操作符](#列表操作符)
9. [列表推导式](#列表推导式)
10. [内置函数](#内置函数)
11. [综合练习](#综合练习)

---

## 创建列表

### 练习题

**题目 1：基础创建**
创建以下列表：
1. 一个包含 1 到 10 的整数列表
2. 一个包含你最喜欢的 5 种水果的列表
3. 一个混合类型的列表，包含字符串、整数、浮点数和布尔值

**题目 2：使用 list() 构造函数**
1. 将字符串 "Python" 转换为字符列表
2. 将元组 (10, 20, 30, 40, 50) 转换为列表
3. 使用 range() 创建一个包含 0 到 99 的列表

**题目 3：列表推导式创建**
1. 创建一个包含 1 到 20 所有偶数的列表
2. 创建一个包含 1 到 10 每个数字的立方的列表
3. 创建一个 5x5 的二维列表（矩阵），所有元素初始化为 0

**题目 4：陷阱题**
以下代码有什么问题？如何修复？
```python
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)
```

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
numbers = list(range(1, 11))
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
mixed = ['hello', 42, 3.14, True]

# 题目 2
chars = list('Python')  # ['P', 'y', 't', 'h', 'o', 'n']
numbers = list((10, 20, 30, 40, 50))
hundred = list(range(100))

# 题目 3
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
cubes = [x**3 for x in range(1, 11)]
matrix = [[0 for _ in range(5)] for _ in range(5)]

# 题目 4
# 问题：所有行都是同一个列表对象的引用
# 修复：
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```
</details>

---

## 访问列表元素

### 练习题

**题目 1：索引访问**
给定列表 `fruits = ['apple', 'banana', 'orange', 'grape', 'mango']`
1. 获取第一个元素
2. 获取最后一个元素
3. 获取倒数第二个元素
4. 尝试访问索引 10，会发生什么？

**题目 2：切片基础**
给定列表 `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
1. 获取前 5 个元素
2. 获取后 5 个元素
3. 获取索引 2 到 7 的元素（不包括 7）
4. 获取所有奇数位置的元素（索引 1, 3, 5...）

**题目 3：切片高级**
给定列表 `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
1. 反转整个列表
2. 获取索引 7 到 2 的元素（反向）
3. 每隔两个元素取一个
4. 反向每隔两个元素取一个

**题目 4：实战应用**
编写一个函数，接收一个列表，返回：
- 第一个元素
- 最后一个元素
- 中间的元素（如果列表长度为奇数）
如果列表为空或只有一个元素，返回适当的提示。

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'mango'
print(fruits[-2])   # 'grape'
# fruits[10]  # IndexError: list index out of range

# 题目 2
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:5])   # [0, 1, 2, 3, 4]
print(numbers[-5:])  # [5, 6, 7, 8, 9]
print(numbers[2:7])  # [2, 3, 4, 5, 6]
print(numbers[1::2]) # [1, 3, 5, 7, 9]

# 题目 3
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[7:2:-1])  # [7, 6, 5, 4, 3]
print(numbers[::3])     # [0, 3, 6, 9]
print(numbers[::-3])    # [9, 6, 3, 0]

# 题目 4
def get_elements(lst):
    if not lst:
        return "列表为空"
    if len(lst) == 1:
        return f"只有一个元素: {lst[0]}"
    
    first = lst[0]
    last = lst[-1]
    
    if len(lst) % 2 == 1:
        middle = lst[len(lst) // 2]
        return f"第一个: {first}, 最后一个: {last}, 中间: {middle}"
    else:
        return f"第一个: {first}, 最后一个: {last}, 无中间元素（偶数长度）"

print(get_elements([1, 2, 3, 4, 5]))  # 第一个: 1, 最后一个: 5, 中间: 3
```
</details>


---

## 修改列表

### 练习题

**题目 1：修改单个元素**
给定列表 `colors = ['red', 'green', 'blue', 'yellow']`
1. 将第二个元素改为 'purple'
2. 将最后一个元素改为 'orange'
3. 将倒数第二个元素改为 'pink'

**题目 2：修改切片**
给定列表 `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
1. 将索引 2 到 5 的元素替换为 [99, 88, 77]
2. 将前 3 个元素替换为单个元素 100
3. 在索引 5 的位置插入 [50, 60]（不删除任何元素）

**题目 3：使用 del 删除**
给定列表 `items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']`
1. 删除第三个元素
2. 删除最后两个元素
3. 删除所有偶数索引的元素

**题目 4：实战应用**
编写一个函数，接收一个数字列表，将所有负数替换为 0。

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
colors = ['red', 'green', 'blue', 'yellow']
colors[1] = 'purple'
colors[-1] = 'orange'
colors[-2] = 'pink'
print(colors)  # ['red', 'purple', 'pink', 'orange']

# 题目 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[2:5] = [99, 88, 77]
print(numbers)  # [1, 2, 99, 88, 77, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[:3] = [100]
print(numbers)  # [100, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[5:5] = [50, 60]
print(numbers)  # [1, 2, 3, 4, 5, 50, 60, 6, 7, 8, 9, 10]

# 题目 3
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del items[2]
print(items)  # ['a', 'b', 'd', 'e', 'f', 'g']

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del items[-2:]
print(items)  # ['a', 'b', 'c', 'd', 'e']

items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del items[::2]
print(items)  # ['b', 'd', 'f']

# 题目 4
def replace_negative(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 0:
            numbers[i] = 0
    return numbers

# 或使用列表推导式
def replace_negative_v2(numbers):
    return [0 if x < 0 else x for x in numbers]

print(replace_negative([1, -2, 3, -4, 5]))  # [1, 0, 3, 0, 5]
```
</details>

---

## 列表方法 - append/insert/extend

### 练习题

**题目 1：append() 练习**
1. 创建一个空列表，使用循环添加 1 到 10
2. 创建一个列表 `[1, 2, 3]`，添加列表 `[4, 5]` 作为单个元素
3. append() 的返回值是什么？

**题目 2：insert() 练习**
给定列表 `fruits = ['apple', 'orange', 'grape']`
1. 在开头插入 'banana'
2. 在索引 2 的位置插入 'mango'
3. 在末尾插入 'kiwi'（使用 insert）

**题目 3：extend() 练习**
给定列表 `numbers = [1, 2, 3]`
1. 使用 extend() 添加 `[4, 5, 6]`
2. 使用 extend() 添加字符串 'abc'
3. extend() 和 append() 的区别是什么？

**题目 4：性能对比**
以下两种方法哪个更快？为什么？
```python
# 方法 1
result = []
for i in range(1000):
    result.insert(0, i)

# 方法 2
result = []
for i in range(1000):
    result.append(i)
```

**题目 5：实战应用**
编写一个函数，接收多个列表作为参数，将它们合并成一个列表。

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)  # [1, 2, 3, [4, 5]]

result = my_list.append(6)
print(result)  # None

# 题目 2
fruits = ['apple', 'orange', 'grape']
fruits.insert(0, 'banana')
print(fruits)  # ['banana', 'apple', 'orange', 'grape']

fruits.insert(2, 'mango')
print(fruits)  # ['banana', 'apple', 'mango', 'orange', 'grape']

fruits.insert(len(fruits), 'kiwi')  # 或 fruits.insert(100, 'kiwi')
print(fruits)

# 题目 3
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers.extend('abc')
print(numbers)  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

# extend() 展开可迭代对象，append() 添加单个元素

# 题目 4
# 方法 2 更快
# insert(0, i) 是 O(n) 操作，总复杂度 O(n²)
# append(i) 是 O(1) 操作，总复杂度 O(n)

# 题目 5
def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

# 或使用列表推导式
def merge_lists_v2(*lists):
    return [item for lst in lists for item in lst]

print(merge_lists([1, 2], [3, 4], [5, 6]))  # [1, 2, 3, 4, 5, 6]
```
</details>

---

## 列表方法 - remove/pop/clear

### 练习题

**题目 1：remove() 练习**
给定列表 `numbers = [1, 2, 3, 2, 4, 2, 5]`
1. 删除第一个 2
2. 删除所有的 2
3. 尝试删除不存在的元素 10，会发生什么？

**题目 2：pop() 练习**
给定列表 `stack = [1, 2, 3, 4, 5]`
1. 删除并返回最后一个元素
2. 删除并返回第一个元素
3. 删除并返回索引 2 的元素
4. 对空列表使用 pop()，会发生什么？

**题目 3：clear() 练习**
1. 创建列表 `[1, 2, 3, 4, 5]`，清空它
2. clear() 和重新赋值 `lst = []` 有什么区别？

**题目 4：实战应用 - 实现栈**
使用列表实现一个栈（LIFO），包含以下操作：
- push(item)：压栈
- pop()：弹栈
- peek()：查看栈顶元素
- is_empty()：检查栈是否为空

**题目 5：实战应用 - 删除重复元素**
编写一个函数，删除列表中的所有重复元素，保留第一次出现的元素。

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
numbers = [1, 2, 3, 2, 4, 2, 5]
numbers.remove(2)
print(numbers)  # [1, 3, 2, 4, 2, 5]

numbers = [1, 2, 3, 2, 4, 2, 5]
while 2 in numbers:
    numbers.remove(2)
print(numbers)  # [1, 3, 4, 5]

try:
    numbers.remove(10)  # ValueError: list.remove(x): x not in list
except ValueError as e:
    print(f"错误: {e}")

# 题目 2
stack = [1, 2, 3, 4, 5]
last = stack.pop()
print(last, stack)  # 5 [1, 2, 3, 4]

first = stack.pop(0)
print(first, stack)  # 1 [2, 3, 4]

middle = stack.pop(1)
print(middle, stack)  # 3 [2, 4]

try:
    [].pop()  # IndexError: pop from empty list
except IndexError as e:
    print(f"错误: {e}")

# 题目 3
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # []

# clear() 清空原列表，引用不变
# lst = [] 创建新列表，引用改变
list1 = [1, 2, 3]
list2 = list1
list1.clear()
print(list2)  # [] - list2 也被清空

list1 = [1, 2, 3]
list2 = list1
list1 = []
print(list2)  # [1, 2, 3] - list2 不受影响

# 题目 4
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0

# 测试
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # 3
print(s.pop())   # 3
print(s.pop())   # 2

# 题目 5
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

# 或使用字典（保持顺序，Python 3.7+）
def remove_duplicates_v2(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))  # [1, 2, 3, 4, 5]
```
</details>


---

## 列表方法 - index/count

### 练习题

**题目 1：index() 练习**
给定列表 `fruits = ['apple', 'banana', 'orange', 'banana', 'grape']`
1. 找到 'banana' 第一次出现的索引
2. 找到 'banana' 第二次出现的索引
3. 在索引 2 到 4 的范围内查找 'banana'
4. 查找不存在的元素 'kiwi'，会发生什么？

**题目 2：count() 练习**
给定列表 `numbers = [1, 2, 3, 2, 4, 2, 5, 2]`
1. 统计 2 出现的次数
2. 统计 10 出现的次数
3. 找出列表中出现次数最多的元素

**题目 3：实战应用 - 查找所有索引**
编写一个函数，返回某个元素在列表中所有出现的索引位置。

**题目 4：实战应用 - 统计频率**
编写一个函数，返回列表中每个元素出现的次数（字典形式）。

**题目 5：综合练习**
给定一个单词列表，找出出现次数最多的单词及其出现次数。

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
print(fruits.index('banana'))  # 1

first_index = fruits.index('banana')
second_index = fruits.index('banana', first_index + 1)
print(second_index)  # 3

print(fruits.index('banana', 2, 5))  # 3

try:
    fruits.index('kiwi')  # ValueError: 'kiwi' is not in list
except ValueError as e:
    print(f"错误: {e}")

# 题目 2
numbers = [1, 2, 3, 2, 4, 2, 5, 2]
print(numbers.count(2))   # 4
print(numbers.count(10))  # 0

most_common = max(set(numbers), key=numbers.count)
print(most_common)  # 2

# 题目 3
def find_all_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

# 或使用循环
def find_all_indices_v2(lst, value):
    indices = []
    start = 0
    while True:
        try:
            index = lst.index(value, start)
            indices.append(index)
            start = index + 1
        except ValueError:
            break
    return indices

print(find_all_indices([1, 2, 3, 2, 4, 2], 2))  # [1, 3, 5]

# 题目 4
def count_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# 或使用 Counter
from collections import Counter
def count_frequency_v2(lst):
    return dict(Counter(lst))

print(count_frequency([1, 2, 2, 3, 3, 3]))  # {1: 1, 2: 2, 3: 3}

# 题目 5
def most_frequent_word(words):
    if not words:
        return None, 0
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    most_common = max(freq, key=freq.get)
    return most_common, freq[most_common]

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word, count = most_frequent_word(words)
print(f"'{word}' 出现了 {count} 次")  # 'apple' 出现了 3 次
```
</details>

---

## 列表方法 - sort/reverse/copy

### 练习题

**题目 1：sort() 基础**
给定列表 `numbers = [3, 1, 4, 1, 5, 9, 2, 6]`
1. 升序排序
2. 降序排序
3. sort() 的返回值是什么？

**题目 2：sort() 高级**
1. 按字符串长度排序：`['banana', 'pie', 'Washington', 'book']`
2. 按元组第二个元素排序：`[('Alice', 85), ('Bob', 92), ('Charlie', 78)]`
3. 按绝对值排序：`[-5, 2, -3, 8, -1]`

**题目 3：reverse() 练习**
1. 反转列表 `[1, 2, 3, 4, 5]`
2. reverse() 和 `lst[::-1]` 有什么区别？

**题目 4：copy() 练习**
1. 复制列表 `[1, 2, 3]`
2. 浅拷贝和深拷贝的区别是什么？
3. 演示浅拷贝的问题（嵌套列表）

**题目 5：实战应用 - 多级排序**
给定学生列表 `[('Alice', 85, 20), ('Bob', 92, 19), ('Charlie', 85, 21)]`
按分数降序排序，分数相同按年龄升序排序。

**题目 6：实战应用 - 自定义排序**
编写一个函数，对字符串列表排序，忽略大小写，但保持原始大小写。

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

result = numbers.sort()
print(result)  # None

# 题目 2
words = ['banana', 'pie', 'Washington', 'book']
words.sort(key=len)
print(words)  # ['pie', 'book', 'banana', 'Washington']

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

numbers = [-5, 2, -3, 8, -1]
numbers.sort(key=abs)
print(numbers)  # [-1, 2, -3, -5, 8]

# 题目 3
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reverse() 原地修改，lst[::-1] 创建新列表
list1 = [1, 2, 3]
list1.reverse()  # 修改 list1
print(list1)  # [3, 2, 1]

list2 = [1, 2, 3]
list3 = list2[::-1]  # 创建新列表
print(list2)  # [1, 2, 3] - 不变
print(list3)  # [3, 2, 1]

# 题目 4
original = [1, 2, 3]
copied = original.copy()
copied[0] = 100
print(original)  # [1, 2, 3] - 不受影响

# 浅拷贝问题
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 100
print(original)  # [[100, 2], [3, 4]] - 被修改了

# 深拷贝解决方案
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 100
print(original)  # [[1, 2], [3, 4]] - 不受影响

# 题目 5
students = [('Alice', 85, 20), ('Bob', 92, 19), ('Charlie', 85, 21)]
students.sort(key=lambda x: (-x[1], x[2]))
print(students)  # [('Bob', 92, 19), ('Alice', 85, 20), ('Charlie', 85, 21)]

# 题目 6
def case_insensitive_sort(words):
    return sorted(words, key=str.lower)

words = ['banana', 'Apple', 'cherry', 'Date']
print(case_insensitive_sort(words))  # ['Apple', 'banana', 'cherry', 'Date']
```
</details>

---

## 列表操作符

### 练习题

**题目 1：+ 运算符**
1. 连接 `[1, 2, 3]` 和 `[4, 5, 6]`
2. 连接三个列表：`[1, 2]`, `[3, 4]`, `[5, 6]`
3. 尝试 `[1, 2] + 3`，会发生什么？

**题目 2：* 运算符**
1. 将 `[1, 2, 3]` 重复 3 次
2. 创建一个包含 10 个 0 的列表
3. `[1, 2] * 0` 的结果是什么？

**题目 3：in 运算符**
1. 检查 5 是否在 `[1, 2, 3, 4, 5]` 中
2. 检查 `[1, 2]` 是否在 `[[1, 2], [3, 4]]` 中
3. 编写函数检查列表是否包含任何负数

**题目 4：+= 和 *= 运算符**
1. 使用 += 扩展列表
2. += 和 + 的区别
3. 使用 *= 重复列表

**题目 5：比较运算符**
比较以下列表：
1. `[1, 2, 3]` 和 `[1, 2, 3]`
2. `[1, 2, 3]` 和 `[1, 2, 4]`
3. `[1, 2]` 和 `[1, 2, 3]`

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
result = [1, 2, 3] + [4, 5, 6]
print(result)  # [1, 2, 3, 4, 5, 6]

result = [1, 2] + [3, 4] + [5, 6]
print(result)  # [1, 2, 3, 4, 5, 6]

try:
    [1, 2] + 3  # TypeError: can only concatenate list to list
except TypeError as e:
    print(f"错误: {e}")

# 题目 2
result = [1, 2, 3] * 3
print(result)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

zeros = [0] * 10
print(zeros)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print([1, 2] * 0)  # []

# 题目 3
print(5 in [1, 2, 3, 4, 5])  # True

print([1, 2] in [[1, 2], [3, 4]])  # True

def has_negative(numbers):
    return any(x < 0 for x in numbers)

print(has_negative([1, 2, -3, 4]))  # True
print(has_negative([1, 2, 3, 4]))   # False

# 题目 4
numbers = [1, 2, 3]
numbers += [4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

# += 原地修改，+ 创建新列表
list1 = [1, 2]
list2 = list1
list1 += [3, 4]
print(list2)  # [1, 2, 3, 4] - 被修改

list1 = [1, 2]
list2 = list1
list1 = list1 + [3, 4]
print(list2)  # [1, 2] - 不受影响

numbers = [1, 2]
numbers *= 3
print(numbers)  # [1, 2, 1, 2, 1, 2]

# 题目 5
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] < [1, 2, 4])   # True
print([1, 2] < [1, 2, 3])      # True
```
</details>


---

## 列表推导式

### 练习题

**题目 1：基础列表推导式**
1. 生成 1 到 20 的平方数列表
2. 将字符串列表 `['hello', 'world', 'python']` 转换为大写
3. 从 1 到 100 中提取所有能被 3 整除的数

**题目 2：带条件的列表推导式**
1. 从 `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` 中提取所有偶数
2. 从 `[-5, -3, 0, 2, 8, -1]` 中提取所有正数
3. 从字符串列表中提取长度大于 5 的字符串

**题目 3：带 if-else 的列表推导式**
1. 将列表中的负数替换为 0：`[-2, 3, -1, 5, -4]`
2. 标记奇偶：`[1, 2, 3, 4, 5]` → `['odd', 'even', 'odd', 'even', 'odd']`
3. 将温度从摄氏度转换为华氏度，如果低于 0°C 则标记为 'freezing'

**题目 4：嵌套列表推导式**
1. 创建一个 3x3 的单位矩阵
2. 展平二维列表：`[[1, 2], [3, 4], [5, 6]]` → `[1, 2, 3, 4, 5, 6]`
3. 转置矩阵：`[[1, 2, 3], [4, 5, 6]]` → `[[1, 4], [2, 5], [3, 6]]`

**题目 5：多重循环**
1. 生成所有两位数（10-99）
2. 生成九九乘法表（元组列表）
3. 生成所有可能的坐标对 (x, y)，其中 x, y ∈ [0, 2]

**题目 6：实战应用**
1. 从字符串列表中提取所有以元音字母开头的单词
2. 将嵌套字典列表中的某个字段提取出来
3. 生成斐波那契数列的前 10 项（不使用推导式，然后用推导式优化）

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
squares = [x**2 for x in range(1, 21)]
print(squares)

words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

divisible_by_3 = [x for x in range(1, 101) if x % 3 == 0]
print(divisible_by_3)

# 题目 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in numbers if x % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]

numbers = [-5, -3, 0, 2, 8, -1]
positive = [x for x in numbers if x > 0]
print(positive)  # [2, 8]

words = ['hi', 'hello', 'world', 'python', 'code']
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['python']

# 题目 3
numbers = [-2, 3, -1, 5, -4]
result = [0 if x < 0 else x for x in numbers]
print(result)  # [0, 3, 0, 5, 0]

numbers = [1, 2, 3, 4, 5]
labels = ['odd' if x % 2 == 1 else 'even' for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

celsius = [-5, 0, 10, 20, 30]
fahrenheit = [c * 9/5 + 32 if c >= 0 else 'freezing' for c in celsius]
print(fahrenheit)  # ['freezing', 32.0, 50.0, 68.0, 86.0]

# 题目 4
# 单位矩阵
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identity)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# 展平
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# 转置
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4], [2, 5], [3, 6]]

# 题目 5
two_digit = [x for x in range(10, 100)]
print(two_digit[:10])  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

multiplication_table = [(i, j, i*j) for i in range(1, 10) for j in range(1, 10)]
print(multiplication_table[:5])  # [(1, 1, 1), (1, 2, 2), (1, 3, 3), (1, 4, 4), (1, 5, 5)]

coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 题目 6
words = ['apple', 'banana', 'orange', 'elephant', 'ice', 'umbrella']
vowels = 'aeiouAEIOU'
vowel_words = [word for word in words if word[0] in vowels]
print(vowel_words)  # ['apple', 'orange', 'elephant', 'ice', 'umbrella']

students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
names = [student['name'] for student in students]
print(names)  # ['Alice', 'Bob', 'Charlie']

# 斐波那契（传统方法）
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 使用推导式（需要辅助）
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
</details>

---

## 内置函数

### 练习题

**题目 1：len/max/min/sum**
给定列表 `numbers = [3, 1, 4, 1, 5, 9, 2, 6]`
1. 获取列表长度
2. 获取最大值和最小值
3. 计算总和和平均值

**题目 2：sorted() 和 reversed()**
1. 对 `[3, 1, 4, 1, 5, 9, 2]` 排序（不修改原列表）
2. 反转 `[1, 2, 3, 4, 5]`（不修改原列表）
3. sorted() 和 list.sort() 的区别

**题目 3：enumerate()**
1. 遍历 `['a', 'b', 'c']` 并打印索引和值
2. 从索引 1 开始枚举
3. 找出列表中所有偶数的索引

**题目 4：zip()**
1. 合并 `['a', 'b', 'c']` 和 `[1, 2, 3]`
2. 合并三个列表
3. 解压列表 `[(1, 'a'), (2, 'b'), (3, 'c')]`

**题目 5：all() 和 any()**
1. 检查 `[2, 4, 6, 8]` 是否全是偶数
2. 检查 `[1, 3, 5, 7]` 是否有偶数
3. 检查列表是否全是正数

**题目 6：filter() 和 map()**
1. 从 `[1, 2, 3, 4, 5, 6]` 中过滤出偶数
2. 将 `[1, 2, 3, 4, 5]` 中的每个数平方
3. 将字符串列表转换为整数列表

**题目 7：实战应用**
编写函数实现以下功能：
1. 找出列表中第 k 大的元素
2. 计算列表的中位数
3. 统计列表中大于平均值的元素个数

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numbers))  # 8
print(max(numbers))  # 9
print(min(numbers))  # 1
print(sum(numbers))  # 31
print(sum(numbers) / len(numbers))  # 3.875

# 题目 2
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] - 不变

numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)  # [5, 4, 3, 2, 1]
print(numbers)  # [1, 2, 3, 4, 5] - 不变

# sorted() 返回新列表，sort() 原地修改

# 题目 3
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(f"{index}: {letter}")

for index, letter in enumerate(letters, start=1):
    print(f"{index}: {letter}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_indices = [i for i, x in enumerate(numbers) if x % 2 == 0]
print(even_indices)  # [1, 3, 5, 7]

# 题目 4
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
result = list(zip(letters, numbers))
print(result)  # [('a', 1), ('b', 2), ('c', 3)]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]
result = list(zip(list1, list2, list3))
print(result)  # [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# 题目 5
numbers = [2, 4, 6, 8]
print(all(x % 2 == 0 for x in numbers))  # True

numbers = [1, 3, 5, 7]
print(any(x % 2 == 0 for x in numbers))  # False

numbers = [1, 2, 3, 4, 5]
print(all(x > 0 for x in numbers))  # True

# 题目 6
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6]

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # [1, 2, 3, 4, 5]

# 题目 7
def kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]

print(kth_largest([3, 1, 4, 1, 5, 9, 2], 2))  # 5

def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

print(median([1, 2, 3, 4, 5]))  # 3
print(median([1, 2, 3, 4]))     # 2.5

def count_above_average(lst):
    avg = sum(lst) / len(lst)
    return sum(1 for x in lst if x > avg)

print(count_above_average([1, 2, 3, 4, 5]))  # 2
```
</details>


---

## 综合练习

### 练习题

**题目 1：列表去重并排序**
编写一个函数，接收一个列表，去除重复元素并按升序排序。

**题目 2：列表旋转**
编写一个函数，将列表向右旋转 k 个位置。
例如：`[1, 2, 3, 4, 5]` 旋转 2 位 → `[4, 5, 1, 2, 3]`

**题目 3：合并两个有序列表**
编写一个函数，合并两个已排序的列表，返回一个新的有序列表。

**题目 4：查找缺失的数字**
给定一个包含 0 到 n 中 n 个数的列表，找出缺失的那个数字。
例如：`[0, 1, 3, 4, 5]` 缺失 2

**题目 5：移动零**
编写一个函数，将列表中的所有 0 移到末尾，保持非零元素的相对顺序。
例如：`[0, 1, 0, 3, 12]` → `[1, 3, 12, 0, 0]`

**题目 6：两数之和**
给定一个整数列表和一个目标值，找出列表中和为目标值的两个数的索引。
例如：`[2, 7, 11, 15]`, target=9 → `[0, 1]`

**题目 7：最大子数组和**
找出一个整数列表中连续子数组的最大和。
例如：`[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → 6（子数组 `[4, -1, 2, 1]`）

**题目 8：买卖股票的最佳时机**
给定一个列表，第 i 个元素是股票第 i 天的价格。
找出最大利润（只能买卖一次）。
例如：`[7, 1, 5, 3, 6, 4]` → 5（第 2 天买入，第 5 天卖出）

**题目 9：数组中的第 K 个最大元素**
在未排序的数组中找到第 k 个最大的元素。
例如：`[3, 2, 1, 5, 6, 4]`, k=2 → 5

**题目 10：螺旋矩阵**
给定一个 m x n 的矩阵，按螺旋顺序返回所有元素。
例如：
```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```
输出：`[1, 2, 3, 6, 9, 8, 7, 4, 5]`

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1：列表去重并排序
def unique_and_sort(lst):
    return sorted(list(set(lst)))

# 或保持原有顺序
def unique_and_sort_v2(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return sorted(seen)

print(unique_and_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # [1, 2, 3, 4, 5, 6, 9]

# 题目 2：列表旋转
def rotate_right(lst, k):
    if not lst:
        return lst
    k = k % len(lst)  # 处理 k 大于列表长度的情况
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]

# 题目 3：合并两个有序列表
def merge_sorted_lists(list1, list2):
    result = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]

# 题目 4：查找缺失的数字
def find_missing_number(lst):
    n = len(lst)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

print(find_missing_number([0, 1, 3, 4, 5]))  # 2

# 题目 5：移动零
def move_zeros(lst):
    # 方法1：创建新列表
    non_zero = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zero))
    return non_zero + zeros

# 方法2：原地修改
def move_zeros_inplace(lst):
    write_pos = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[write_pos] = lst[i]
            write_pos += 1
    
    for i in range(write_pos, len(lst)):
        lst[i] = 0
    
    return lst

print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]

# 题目 6：两数之和
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# 题目 7：最大子数组和（Kadane算法）
def max_subarray_sum(nums):
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

# 题目 8：买卖股票的最佳时机
def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # 5

# 题目 9：数组中的第 K 个最大元素
def find_kth_largest(nums, k):
    return sorted(nums, reverse=True)[k-1]

# 或使用堆（更高效）
import heapq
def find_kth_largest_heap(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5

# 题目 10：螺旋矩阵
def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # 从左到右
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # 从上到下
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # 从右到左
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # 从下到上
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_order(matrix))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
</details>

---

## 挑战题

### 练习题

**题目 1：三数之和**
给定一个整数列表，找出所有和为 0 的三元组。
例如：`[-1, 0, 1, 2, -1, -4]` → `[[-1, -1, 2], [-1, 0, 1]]`

**题目 2：接雨水**
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算下雨后能接多少水。
例如：`[0,1,0,2,1,0,1,3,2,1,2,1]` → 6

**题目 3：最长连续序列**
给定一个未排序的整数数组，找出最长连续序列的长度。
例如：`[100, 4, 200, 1, 3, 2]` → 4（连续序列 `[1, 2, 3, 4]`）

**题目 4：下一个排列**
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
例如：`[1, 2, 3]` → `[1, 3, 2]`

**题目 5：滑动窗口最大值**
给定一个数组和滑动窗口的大小，找出所有滑动窗口里的最大值。
例如：`[1,3,-1,-3,5,3,6,7]`, k=3 → `[3,3,5,5,6,7]`

### 参考答案

<details>
<summary>点击查看答案</summary>

```python
# 题目 1：三数之和
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]

# 题目 2：接雨水
def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6

# 题目 3：最长连续序列
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # 序列的起点
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            longest = max(longest, current_length)
    
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4

# 题目 4：下一个排列
def next_permutation(nums):
    # 从右向左找第一个升序对
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i >= 0:
        # 从右向左找第一个大于 nums[i] 的数
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    
    # 反转 i 之后的部分
    nums[i+1:] = reversed(nums[i+1:])
    return nums

print(next_permutation([1, 2, 3]))  # [1, 3, 2]
print(next_permutation([3, 2, 1]))  # [1, 2, 3]

# 题目 5：滑动窗口最大值
from collections import deque

def max_sliding_window(nums, k):
    if not nums:
        return []
    
    result = []
    dq = deque()  # 存储索引
    
    for i in range(len(nums)):
        # 移除窗口外的元素
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # 移除比当前元素小的元素
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # 窗口形成后添加最大值
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [3, 3, 5, 5, 6, 7]
```
</details>

---

## 总结

通过这些练习题，你应该能够：

1. ✅ 熟练掌握列表的创建、访问和修改
2. ✅ 熟练使用所有列表方法
3. ✅ 理解列表操作符的使用和区别
4. ✅ 掌握列表推导式的各种用法
5. ✅ 熟练使用内置函数处理列表
6. ✅ 解决实际编程问题
7. ✅ 理解时间复杂度和性能优化

### 学习建议

1. **循序渐进**：从基础题开始，逐步挑战难题
2. **动手实践**：每道题都要自己编写代码运行
3. **理解原理**：不要只记住答案，要理解为什么这样写
4. **多种方法**：尝试用不同方法解决同一个问题
5. **性能意识**：思考不同方法的时间和空间复杂度
6. **总结归纳**：做完题后总结常见模式和技巧

### 常见模式总结

1. **双指针**：两数之和、三数之和、接雨水
2. **滑动窗口**：最大子数组和、滑动窗口最大值
3. **哈希表**：查找、去重、频率统计
4. **排序**：合并有序列表、第 K 大元素
5. **动态规划**：最大子数组和、买卖股票
6. **贪心算法**：移动零、下一个排列

继续练习，你会越来越熟练！🚀
