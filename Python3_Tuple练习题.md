# Python3 Tuple 练习题

## 基础题 (10题)

### 1. 创建元组
创建一个包含你最喜欢的 5 种水果的元组,并打印出来。

<details>
<summary>点击查看答案</summary>

```python
fruits = ('apple', 'banana', 'orange', 'grape', 'mango')
print(fruits)
# 输出: ('apple', 'banana', 'orange', 'grape', 'mango')
```
</details>

---

### 2. 单元素元组
创建一个只包含数字 42 的元组,并验证它的类型是 tuple。

<details>
<summary>点击查看答案</summary>

```python
t = (42,)  # 注意:必须有逗号!
print(type(t))  # <class 'tuple'>
print(t)        # (42,)

# 错误示范
wrong = (42)
print(type(wrong))  # <class 'int'> - 这是整数,不是元组!
```
</details>

---

### 3. 访问元素
给定元组 `colors = ('red', 'green', 'blue', 'yellow', 'purple')`,打印第一个和最后一个颜色。

<details>
<summary>点击查看答案</summary>

```python
colors = ('red', 'green', 'blue', 'yellow', 'purple')
print(colors[0])   # red
print(colors[-1])  # purple
```
</details>

---

### 4. 切片操作
给定元组 `numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)`,使用切片获取:
- 前 3 个元素
- 最后 3 个元素
- 所有偶数索引的元素

<details>
<summary>点击查看答案</summary>

```python
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 前 3 个元素
print(numbers[:3])  # (0, 1, 2)

# 最后 3 个元素
print(numbers[-3:])  # (7, 8, 9)

# 所有偶数索引的元素
print(numbers[::2])  # (0, 2, 4, 6, 8)
```
</details>

---

### 5. 元组拼接
创建两个元组 `t1 = (1, 2, 3)` 和 `t2 = (4, 5, 6)`,将它们拼接成一个新元组。

<details>
<summary>点击查看答案</summary>

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)
```
</details>

---

### 6. 元组重复
创建元组 `t = ('Python',)`,将它重复 3 次。

<details>
<summary>点击查看答案</summary>

```python
t = ('Python',)
result = t * 3
print(result)  # ('Python', 'Python', 'Python')
```
</details>

---

### 7. 成员检查
给定元组 `fruits = ('apple', 'banana', 'cherry')`,检查 'banana' 和 'grape' 是否在元组中。

<details>
<summary>点击查看答案</summary>

```python
fruits = ('apple', 'banana', 'cherry')

print('banana' in fruits)  # True
print('grape' in fruits)   # False
print('grape' not in fruits)  # True
```
</details>

---

### 8. count 方法
给定元组 `numbers = (1, 2, 3, 2, 4, 2, 5, 2)`,统计数字 2 出现的次数。

<details>
<summary>点击查看答案</summary>

```python
numbers = (1, 2, 3, 2, 4, 2, 5, 2)
count = numbers.count(2)
print(count)  # 4
```
</details>

---

### 9. index 方法
给定元组 `letters = ('a', 'b', 'c', 'd', 'e')`,找出字母 'c' 的索引位置。

<details>
<summary>点击查看答案</summary>

```python
letters = ('a', 'b', 'c', 'd', 'e')
index = letters.index('c')
print(index)  # 2
```
</details>

---

### 10. 元组长度
创建一个包含 1 到 10 的元组,并打印它的长度。

<details>
<summary>点击查看答案</summary>

```python
numbers = tuple(range(1, 11))
print(numbers)      # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(numbers)) # 10
```
</details>

---

## 进阶题 (10题)

### 11. 元组解包
给定元组 `person = ('Alice', 25, 'Engineer', 'New York')`,将其解包为 4 个变量并打印。

<details>
<summary>点击查看答案</summary>

```python
person = ('Alice', 25, 'Engineer', 'New York')
name, age, job, city = person

print(name)  # Alice
print(age)   # 25
print(job)   # Engineer
print(city)  # New York
```
</details>

---

### 12. 交换变量
使用元组解包交换两个变量的值。

<details>
<summary>点击查看答案</summary>

```python
a = 100
b = 200

# 使用元组解包交换
a, b = b, a

print(a)  # 200
print(b)  # 100
```
</details>

---

### 13. * 解包
给定元组 `numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`,使用 `*` 解包。

<details>
<summary>点击查看答案</summary>

```python
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# 获取第一个元素和剩余元素
first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# 获取第一个、最后一个和中间元素
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4, 5, 6, 7, 8, 9]
print(last)    # 10
```
</details>

---

### 14. 嵌套元组
创建一个 3x3 的矩阵元组,并访问中心元素(值为 5)。

<details>
<summary>点击查看答案</summary>

```python
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# 访问中心元素
center = matrix[1][1]
print(center)  # 5
```
</details>

---

### 15. 元组转列表
给定元组 `t = (1, 2, 3, 4, 5)`,将其转换为列表,修改第一个元素为 100,再转回元组。

<details>
<summary>点击查看答案</summary>

```python
t = (1, 2, 3, 4, 5)

# 转换为列表
my_list = list(t)
print(my_list)  # [1, 2, 3, 4, 5]

# 修改第一个元素
my_list[0] = 100
print(my_list)  # [100, 2, 3, 4, 5]

# 转回元组
t = tuple(my_list)
print(t)  # (100, 2, 3, 4, 5)
```
</details>

---

### 16. 列表转元组
给定列表 `my_list = ['apple', 'banana', 'cherry']`,将其转换为元组。

<details>
<summary>点击查看答案</summary>

```python
my_list = ['apple', 'banana', 'cherry']
my_tuple = tuple(my_list)
print(my_tuple)  # ('apple', 'banana', 'cherry')
```
</details>

---

### 17. 函数返回多值
编写一个函数 `calculate(a, b)`,返回两个数的和、差、积、商(以元组形式返回)。

<details>
<summary>点击查看答案</summary>

```python
def calculate(a, b):
    return a + b, a - b, a * b, a / b

result = calculate(10, 5)
print(result)  # (15, 5, 50, 2.0)

# 解包结果
sum_val, diff, prod, quot = calculate(10, 5)
print(f"和:{sum_val}, 差:{diff}, 积:{prod}, 商:{quot}")
```
</details>

---

### 18. 元组作为字典键
创建一个字典,使用坐标元组作为键,城市名作为值。

<details>
<summary>点击查看答案</summary>

```python
cities = {
    (40.7128, -74.0060): 'New York',
    (34.0522, -118.2437): 'Los Angeles',
    (51.5074, -0.1278): 'London'
}

# 访问
print(cities[(40.7128, -74.0060)])  # New York

# 遍历
for coords, city in cities.items():
    print(f"{city}: {coords}")
```
</details>

---

### 19. zip 组合
给定两个元组,使用 `zip` 将它们组合。

<details>
<summary>点击查看答案</summary>

```python
names = ('Alice', 'Bob', 'Charlie')
scores = (85, 92, 78)

# 使用 zip 组合
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 输出:
# Alice: 85
# Bob: 92
# Charlie: 78

# 转换为元组列表
result = tuple(zip(names, scores))
print(result)  # (('Alice', 85), ('Bob', 92), ('Charlie', 78))
```
</details>

---

### 20. 元组排序
给定元组 `numbers = (5, 2, 8, 1, 9, 3)`,对其进行排序(升序和降序)。

<details>
<summary>点击查看答案</summary>

```python
numbers = (5, 2, 8, 1, 9, 3)

# 升序
ascending = tuple(sorted(numbers))
print(ascending)  # (1, 2, 3, 5, 8, 9)

# 降序
descending = tuple(sorted(numbers, reverse=True))
print(descending)  # (9, 8, 5, 3, 2, 1)
```
</details>

---

## 挑战题 (10题)

### 21. 统计元素
编写函数 `count_elements(t)`,统计元组中每个元素出现的次数,返回字典。

<details>
<summary>点击查看答案</summary>

```python
def count_elements(t):
    result = {}
    for item in t:
        result[item] = t.count(item)
    return result

# 测试
t = (1, 2, 2, 3, 3, 3)
print(count_elements(t))  # {1: 1, 2: 2, 3: 3}

# 方法2: 使用 Counter
from collections import Counter
print(dict(Counter(t)))  # {1: 1, 2: 2, 3: 3}
```
</details>

---

### 22. 查找所有索引
编写函数 `find_all_indices(t, value)`,返回元组中某个值的所有索引位置。

<details>
<summary>点击查看答案</summary>

```python
def find_all_indices(t, value):
    return [i for i, x in enumerate(t) if x == value]

# 测试
t = (1, 2, 3, 2, 4, 2)
print(find_all_indices(t, 2))  # [1, 3, 5]
```
</details>

---

### 23. 元组去重
编写函数 `remove_duplicates(t)`,去除元组中的重复元素,保持顺序。

<details>
<summary>点击查看答案</summary>

```python
def remove_duplicates(t):
    return tuple(dict.fromkeys(t))

# 测试
t = (1, 2, 2, 3, 3, 3, 4)
print(remove_duplicates(t))  # (1, 2, 3, 4)

# 方法2: 使用列表
def remove_duplicates_v2(t):
    seen = []
    for item in t:
        if item not in seen:
            seen.append(item)
    return tuple(seen)
```
</details>

---

### 24. 元组反转
编写函数 `reverse_tuple(t)`,反转元组(不使用 `reversed` 函数)。

<details>
<summary>点击查看答案</summary>

```python
def reverse_tuple(t):
    return t[::-1]

# 测试
t = (1, 2, 3, 4, 5)
print(reverse_tuple(t))  # (5, 4, 3, 2, 1)

# 方法2: 手动反转
def reverse_tuple_v2(t):
    result = []
    for i in range(len(t) - 1, -1, -1):
        result.append(t[i])
    return tuple(result)
```
</details>

---

### 25. 嵌套元组展平
编写函数 `flatten(t)`,将嵌套元组展平为一维元组。

<details>
<summary>点击查看答案</summary>

```python
def flatten(t):
    result = []
    for item in t:
        result.extend(item)
    return tuple(result)

# 测试
t = ((1, 2), (3, 4), (5, 6))
print(flatten(t))  # (1, 2, 3, 4, 5, 6)

# 方法2: 使用列表推导式
def flatten_v2(t):
    return tuple(x for sub in t for x in sub)

# 方法3: 使用 itertools
from itertools import chain
def flatten_v3(t):
    return tuple(chain.from_iterable(t))
```
</details>

---

### 26. 元组切片反转
给定元组 `t = (1, 2, 3, 4, 5, 6, 7, 8, 9)`,反转索引 2 到 6 之间的元素。

<details>
<summary>点击查看答案</summary>

```python
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 反转索引 2 到 6 (不包括6)
result = t[:2] + t[2:7][::-1] + t[7:]
print(result)  # (1, 2, 7, 6, 5, 4, 3, 8, 9)

# 注意:题目要求是索引2到6,所以是 t[2:7]
```
</details>

---

### 27. 学生成绩排序
给定学生成绩元组列表,按成绩从高到低排序。

<details>
<summary>点击查看答案</summary>

```python
students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 78),
    ('David', 95)
]

# 按成绩降序排序
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
# [('David', 95), ('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 打印排名
for i, (name, score) in enumerate(sorted_students, 1):
    print(f"{i}. {name}: {score}")
```
</details>

---

### 28. 坐标距离
编写函数 `distance(p1, p2)`,计算两个坐标点之间的欧几里得距离。

<details>
<summary>点击查看答案</summary>

```python
import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# 测试
p1 = (0, 0)
p2 = (3, 4)
print(distance(p1, p2))  # 5.0

# 方法2: 使用 math.dist (Python 3.8+)
print(math.dist(p1, p2))  # 5.0
```
</details>

---

### 29. 元组分组
编写函数 `group_by_length(tuples)`,将元组列表按长度分组。

<details>
<summary>点击查看答案</summary>

```python
def group_by_length(tuples):
    result = {}
    for t in tuples:
        length = len(t)
        if length not in result:
            result[length] = []
        result[length].append(t)
    return result

# 测试
tuples = [(1,), (1, 2), (1, 2, 3), (4, 5)]
print(group_by_length(tuples))
# {1: [(1,)], 2: [(1, 2), (4, 5)], 3: [(1, 2, 3)]}

# 方法2: 使用 defaultdict
from collections import defaultdict

def group_by_length_v2(tuples):
    result = defaultdict(list)
    for t in tuples:
        result[len(t)].append(t)
    return dict(result)
```
</details>

---

### 30. 命名元组应用
使用 `namedtuple` 创建一个 `Book` 类型,创建 3 本书的实例,并找出最贵的书。

<details>
<summary>点击查看答案</summary>

```python
from collections import namedtuple

# 定义 Book 类型
Book = namedtuple('Book', ['title', 'author', 'year', 'price'])

# 创建书籍实例
books = [
    Book('Python编程', '张三', 2023, 89.0),
    Book('数据结构', '李四', 2022, 120.0),
    Book('算法导论', '王五', 2021, 150.0)
]

# 找出最贵的书
most_expensive = max(books, key=lambda b: b.price)
print(f"最贵的书: {most_expensive.title}, 价格: {most_expensive.price}")
# 最贵的书: 算法导论, 价格: 150.0

# 打印所有书籍
for book in books:
    print(f"{book.title} by {book.author} ({book.year}) - ¥{book.price}")
```
</details>

---

## 综合应用题 (5题)

### 31. RGB 颜色转换
编写函数 `rgb_to_hex(rgb)`,将 RGB 元组转换为十六进制颜色代码。

<details>
<summary>点击查看答案</summary>

```python
def rgb_to_hex(rgb):
    return f'#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}'

# 测试
print(rgb_to_hex((255, 0, 0)))      # #FF0000 (红色)
print(rgb_to_hex((0, 255, 0)))      # #00FF00 (绿色)
print(rgb_to_hex((0, 0, 255)))      # #0000FF (蓝色)
print(rgb_to_hex((255, 255, 255)))  # #FFFFFF (白色)

# 方法2: 使用 format
def rgb_to_hex_v2(rgb):
    return '#{:02X}{:02X}{:02X}'.format(*rgb)
```
</details>

---

### 32. 数据分析
给定销售数据元组,计算总销售额、平均销售额和最高销售额的月份。

<details>
<summary>点击查看答案</summary>

```python
sales = (
    ('2024-01', 1000),
    ('2024-02', 1500),
    ('2024-03', 1200),
    ('2024-04', 1800)
)

# 总销售额
total = sum(amount for month, amount in sales)
print(f"总销售额: {total}")  # 5500

# 平均销售额
average = total / len(sales)
print(f"平均销售额: {average}")  # 1375.0

# 最高销售额的月份
best_month = max(sales, key=lambda x: x[1])
print(f"最高销售额月份: {best_month[0]}, 金额: {best_month[1]}")
# 最高销售额月份: 2024-04, 金额: 1800
```
</details>

---

### 33. 矩阵转置
编写函数 `transpose(matrix)`,转置一个矩阵元组。

<details>
<summary>点击查看答案</summary>

```python
def transpose(matrix):
    return tuple(zip(*matrix))

# 测试
matrix = ((1, 2, 3), (4, 5, 6))
result = transpose(matrix)
print(result)  # ((1, 4), (2, 5), (3, 6))

# 转换为列表形式
def transpose_list(matrix):
    return tuple(tuple(row) for row in zip(*matrix))

print(transpose_list(matrix))  # ((1, 4), (2, 5), (3, 6))
```
</details>

---

### 34. 元组压缩
编写函数 `compress(t)`,压缩连续重复的元素。

<details>
<summary>点击查看答案</summary>

```python
def compress(t):
    if not t:
        return ()
    
    result = []
    current = t[0]
    count = 1
    
    for i in range(1, len(t)):
        if t[i] == current:
            count += 1
        else:
            result.append((current, count))
            current = t[i]
            count = 1
    
    result.append((current, count))
    return tuple(result)

# 测试
t = (1, 1, 1, 2, 2, 3, 3, 3, 3, 4)
print(compress(t))  # ((1, 3), (2, 2), (3, 4), (4, 1))

# 方法2: 使用 itertools.groupby
from itertools import groupby

def compress_v2(t):
    return tuple((key, len(list(group))) for key, group in groupby(t))
```
</details>

---

### 35. 多维坐标系
创建一个 3D 坐标系统,实现相关功能。

<details>
<summary>点击查看答案</summary>

```python
from collections import namedtuple
import math

# 定义 3D 点
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])

def distance_3d(p1, p2):
    """计算两点之间的距离"""
    return math.sqrt(
        (p2.x - p1.x)**2 + 
        (p2.y - p1.y)**2 + 
        (p2.z - p1.z)**2
    )

def distance_to_origin(p):
    """计算点到原点的距离"""
    origin = Point3D(0, 0, 0)
    return distance_3d(p, origin)

def are_collinear(p1, p2, p3):
    """判断三个点是否共线"""
    # 使用向量叉乘判断
    # 如果 (p2-p1) × (p3-p1) = 0,则共线
    v1 = (p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
    v2 = (p3.x - p1.x, p3.y - p1.y, p3.z - p1.z)
    
    # 叉乘
    cross = (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    )
    
    # 判断叉乘是否为零向量
    return all(abs(c) < 1e-10 for c in cross)

# 测试
p1 = Point3D(0, 0, 0)
p2 = Point3D(1, 2, 3)
p3 = Point3D(2, 4, 6)

print(f"p1 到 p2 的距离: {distance_3d(p1, p2):.2f}")
print(f"p2 到原点的距离: {distance_to_origin(p2):.2f}")
print(f"p1, p2, p3 是否共线: {are_collinear(p1, p2, p3)}")
```
</details>

---

## 学习建议

1. **先做基础题** - 熟悉元组的基本操作
2. **理解不可变性** - 元组不能修改,但可以创建新元组
3. **掌握解包** - 这是元组最强大的特性之一
4. **对比列表** - 理解何时用元组,何时用列表
5. **实践应用** - 在实际项目中使用元组

祝学习愉快! 🎉
