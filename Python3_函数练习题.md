# Python3 函数练习题

## 目录
1. [基础练习（10题）](#基础练习)
2. [参数练习（10题）](#参数练习)
3. [高阶函数练习（10题）](#高阶函数练习)
4. [装饰器练习（10题）](#装饰器练习)
5. [生成器练习（10题）](#生成器练习)
6. [递归练习（10题）](#递归练习)
7. [综合应用（15题）](#综合应用)

---

## 基础练习

### 1. 简单函数定义
编写一个函数 `greet(name)`，接收一个姓名参数，返回问候语 "Hello, {name}!"。

<details>
<summary>答案</summary>

```python
def greet(name):
    """返回问候语"""
    return f"Hello, {name}!"

# 测试
print(greet("Alice"))  # Hello, Alice!
print(greet("Bob"))    # Hello, Bob!
```
</details>

---

### 2. 计算圆的面积
编写函数 `circle_area(radius)`，计算并返回圆的面积（π ≈ 3.14159）。

<details>
<summary>答案</summary>

```python
def circle_area(radius):
    """计算圆的面积"""
    pi = 3.14159
    return pi * radius ** 2

# 测试
print(circle_area(5))   # 78.53975
print(circle_area(10))  # 314.159

# 方法2：使用 math 模块
import math

def circle_area_v2(radius):
    return math.pi * radius ** 2

print(circle_area_v2(5))  # 78.53981633974483
```
</details>

---

### 3. 判断奇偶
编写函数 `is_even(n)`，判断一个数是否为偶数，返回 True 或 False。

<details>
<summary>答案</summary>

```python
def is_even(n):
    """判断是否为偶数"""
    return n % 2 == 0

# 测试
print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True
print(is_even(-2))  # True
```
</details>

---

### 4. 字符串反转
编写函数 `reverse_string(s)`，返回字符串的反转。

<details>
<summary>答案</summary>

```python
def reverse_string(s):
    """反转字符串"""
    return s[::-1]

# 测试
print(reverse_string("hello"))    # olleh
print(reverse_string("Python"))   # nohtyP
print(reverse_string("12345"))    # 54321

# 方法2：使用 reversed()
def reverse_string_v2(s):
    return "".join(reversed(s))

# 方法3：使用循环
def reverse_string_v3(s):
    result = ""
    for char in s:
        result = char + result
    return result
```
</details>

---

### 5. 查找最大值
编写函数 `find_max(a, b, c)`，返回三个数中的最大值（不使用内置 max 函数）。

<details>
<summary>答案</summary>

```python
def find_max(a, b, c):
    """返回三个数中的最大值"""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# 测试
print(find_max(3, 7, 5))   # 7
print(find_max(10, 2, 8))  # 10
print(find_max(1, 1, 1))   # 1

# 方法2：使用条件表达式
def find_max_v2(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)

# 方法3：逐步比较
def find_max_v3(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val
```
</details>

---

### 6. 温度转换
编写函数 `celsius_to_fahrenheit(celsius)`，将摄氏度转换为华氏度。
公式：F = C × 9/5 + 32

<details>
<summary>答案</summary>

```python
def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return celsius * 9 / 5 + 32

# 测试
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(celsius_to_fahrenheit(37))   # 98.6

# 扩展：双向转换
def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(32))   # 0.0
print(fahrenheit_to_celsius(212))  # 100.0
```
</details>

---

### 7. 列表求和
编写函数 `sum_list(numbers)`，计算列表中所有数字的和（不使用内置 sum 函数）。

<details>
<summary>答案</summary>

```python
def sum_list(numbers):
    """计算列表元素的和"""
    total = 0
    for num in numbers:
        total += num
    return total

# 测试
print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([10, 20, 30]))     # 60
print(sum_list([]))               # 0

# 方法2：使用 reduce
from functools import reduce
def sum_list_v2(numbers):
    return reduce(lambda x, y: x + y, numbers, 0)

# 方法3：递归
def sum_list_v3(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list_v3(numbers[1:])
```
</details>

---

### 8. 统计字符
编写函数 `count_char(s, char)`，统计字符串中某个字符出现的次数。

<details>
<summary>答案</summary>

```python
def count_char(s, char):
    """统计字符出现次数"""
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

# 测试
print(count_char("hello", "l"))      # 2
print(count_char("Python", "o"))     # 1
print(count_char("banana", "a"))     # 3

# 方法2：使用 count 方法
def count_char_v2(s, char):
    return s.count(char)

# 方法3：使用列表推导式
def count_char_v3(s, char):
    return len([c for c in s if c == char])
```
</details>

---

### 9. 判断回文
编写函数 `is_palindrome(s)`，判断字符串是否为回文（正读反读都一样）。

<details>
<summary>答案</summary>

```python
def is_palindrome(s):
    """判断是否为回文"""
    return s == s[::-1]

# 测试
print(is_palindrome("radar"))    # True
print(is_palindrome("hello"))    # False
print(is_palindrome("level"))    # True
print(is_palindrome("a"))        # True

# 方法2：双指针
def is_palindrome_v2(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# 方法3：忽略大小写和空格
def is_palindrome_v3(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome_v3("A man a plan a canal Panama"))  # True
```
</details>

---

### 10. 计算阶乘
编写函数 `factorial(n)`，计算 n 的阶乘（n! = n × (n-1) × ... × 1）。

<details>
<summary>答案</summary>

```python
def factorial(n):
    """计算阶乘"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 测试
print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(10))  # 3628800

# 方法2：递归
def factorial_v2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_v2(n - 1)

# 方法3：使用 reduce
from functools import reduce
def factorial_v3(n):
    if n == 0 or n == 1:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

# 方法4：使用 math 模块
import math
print(math.factorial(5))  # 120
```
</details>

---

## 参数练习

### 11. 默认参数
编写函数 `power(base, exponent=2)`，计算 base 的 exponent 次方，默认计算平方。

<details>
<summary>答案</summary>

```python
def power(base, exponent=2):
    """计算幂运算"""
    return base ** exponent

# 测试
print(power(5))       # 25（默认平方）
print(power(5, 3))    # 125
print(power(2, 10))   # 1024

# 扩展：支持负指数
def power_v2(base, exponent=2):
    if exponent < 0:
        return 1 / (base ** abs(exponent))
    return base ** exponent

print(power_v2(2, -3))  # 0.125
```
</details>

---

### 12. 可变参数求和
编写函数 `sum_all(*numbers)`，接收任意数量的数字参数，返回它们的和。

<details>
<summary>答案</summary>

```python
def sum_all(*numbers):
    """计算所有参数的和"""
    return sum(numbers)

# 测试
print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100
print(sum_all(5))                 # 5
print(sum_all())                  # 0

# 方法2：不使用内置 sum
def sum_all_v2(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
```
</details>

---

### 13. 关键字参数
编写函数 `print_info(**info)`，接收任意关键字参数，格式化打印所有信息。

<details>
<summary>答案</summary>

```python
def print_info(**info):
    """打印所有信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

# 测试
print_info(name="Alice", age=25, city="北京")
# 输出:
# name: Alice
# age: 25
# city: 北京

print_info(product="iPhone", price=5999, stock=100)
# 输出:
# product: iPhone
# price: 5999
# stock: 100

# 扩展：返回格式化字符串
def format_info(**info):
    return "\n".join(f"{k}: {v}" for k, v in info.items())

print(format_info(name="Bob", score=95))
```
</details>

---

### 14. 混合参数
编写函数 `create_profile(name, age, *hobbies, **other_info)`，创建用户档案。

<details>
<summary>答案</summary>

```python
def create_profile(name, age, *hobbies, **other_info):
    """创建用户档案"""
    profile = {
        "name": name,
        "age": age,
        "hobbies": list(hobbies),
        "other": other_info
    }
    return profile

# 测试
profile = create_profile(
    "Alice", 25,
    "读书", "旅游", "摄影",
    city="北京",
    email="alice@example.com"
)
print(profile)
# {
#     'name': 'Alice',
#     'age': 25,
#     'hobbies': ['读书', '旅游', '摄影'],
#     'other': {'city': '北京', 'email': 'alice@example.com'}
# }
```
</details>

---

### 15. 仅限关键字参数
编写函数 `divide(a, b, *, precision=2)`，执行除法并保留指定小数位数。

<details>
<summary>答案</summary>

```python
def divide(a, b, *, precision=2):
    """除法运算，保留指定小数位"""
    if b == 0:
        raise ValueError("除数不能为零")
    result = a / b
    return round(result, precision)

# 测试
print(divide(10, 3))                    # 3.33
print(divide(10, 3, precision=4))       # 3.3333
# print(divide(10, 3, 4))               # TypeError（必须使用关键字）

# 扩展：返回商和余数
def divide_v2(a, b, *, return_remainder=False):
    if b == 0:
        raise ValueError("除数不能为零")
    if return_remainder:
        return divmod(a, b)
    return a / b

print(divide_v2(17, 5))                      # 3.4
print(divide_v2(17, 5, return_remainder=True))  # (3, 2)
```
</details>

---

### 16. 参数解包
编写函数 `calculate_rectangle(length, width)`，计算矩形面积和周长。
使用列表解包调用该函数。

<details>
<summary>答案</summary>

```python
def calculate_rectangle(length, width):
    """计算矩形面积和周长"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# 使用解包
dimensions = [5, 3]
area, perimeter = calculate_rectangle(*dimensions)
print(f"面积: {area}, 周长: {perimeter}")  # 面积: 15, 周长: 16

# 使用字典解包
def create_user(name, age, email):
    return {"name": name, "age": age, "email": email}

user_data = {"name": "Alice", "age": 25, "email": "alice@example.com"}
user = create_user(**user_data)
print(user)
```
</details>

---

### 17. 默认参数陷阱
修复以下函数的默认参数陷阱：
```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```

<details>
<summary>答案</summary>

```python
# 问题代码
def add_item_wrong(item, lst=[]):
    lst.append(item)
    return lst

print(add_item_wrong(1))  # [1]
print(add_item_wrong(2))  # [1, 2]（意外！）

# ✅ 正确做法
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [2]（正确）

# 扩展：其他可变默认参数
def add_to_dict(key, value, d=None):
    if d is None:
        d = {}
    d[key] = value
    return d

print(add_to_dict("a", 1))  # {'a': 1}
print(add_to_dict("b", 2))  # {'b': 2}
```
</details>

---

### 18. 参数验证
编写函数 `create_user(name, age, email)`，验证参数的有效性：
- name 不能为空
- age 必须在 0-120 之间
- email 必须包含 @

<details>
<summary>答案</summary>

```python
def create_user(name, age, email):
    """创建用户，验证参数"""
    # 验证 name
    if not name or not name.strip():
        raise ValueError("姓名不能为空")
    
    # 验证 age
    if not isinstance(age, int) or age < 0 or age > 120:
        raise ValueError("年龄必须在 0-120 之间")
    
    # 验证 email
    if "@" not in email:
        raise ValueError("邮箱格式不正确")
    
    return {
        "name": name.strip(),
        "age": age,
        "email": email.lower()
    }

# 测试
try:
    user1 = create_user("Alice", 25, "alice@example.com")
    print(user1)  # 成功
    
    user2 = create_user("", 25, "alice@example.com")
except ValueError as e:
    print(f"错误: {e}")  # 错误: 姓名不能为空

try:
    user3 = create_user("Bob", 150, "bob@example.com")
except ValueError as e:
    print(f"错误: {e}")  # 错误: 年龄必须在 0-120 之间
```
</details>

---

### 19. 可选参数组合
编写函数 `format_name(first, last, middle=None, title=None)`，格式化姓名。

<details>
<summary>答案</summary>

```python
def format_name(first, last, middle=None, title=None):
    """格式化姓名"""
    parts = []
    
    if title:
        parts.append(title)
    
    parts.append(first)
    
    if middle:
        parts.append(middle)
    
    parts.append(last)
    
    return " ".join(parts)

# 测试
print(format_name("John", "Doe"))                    # John Doe
print(format_name("John", "Doe", middle="Smith"))    # John Smith Doe
print(format_name("John", "Doe", title="Dr."))       # Dr. John Doe
print(format_name("John", "Doe", "Smith", "Dr."))    # Dr. John Smith Doe

# 扩展：支持不同格式
def format_name_v2(first, last, middle=None, title=None, format="full"):
    if format == "full":
        return format_name(first, last, middle, title)
    elif format == "last_first":
        return f"{last}, {first}"
    elif format == "initials":
        initials = first[0] + last[0]
        if middle:
            initials = first[0] + middle[0] + last[0]
        return initials.upper()

print(format_name_v2("John", "Doe", format="last_first"))  # Doe, John
print(format_name_v2("John", "Doe", "Smith", format="initials"))  # JSD
```
</details>

---

### 20. 参数类型提示
为以下函数添加完整的类型注解：
```python
def process_data(data, multiplier, options):
    # data 是整数列表
    # multiplier 是浮点数
    # options 是字典，键为字符串，值为布尔值
    # 返回浮点数列表
    pass
```

<details>
<summary>答案</summary>

```python
from typing import List, Dict

def process_data(
    data: List[int],
    multiplier: float,
    options: Dict[str, bool]
) -> List[float]:
    """
    处理数据
    
    参数:
        data: 整数列表
        multiplier: 乘数
        options: 配置选项
    
    返回:
        处理后的浮点数列表
    """
    result = []
    for num in data:
        value = num * multiplier
        if options.get("round", False):
            value = round(value, 2)
        result.append(value)
    return result

# 测试
data = [1, 2, 3, 4, 5]
result = process_data(data, 1.5, {"round": True})
print(result)  # [1.5, 3.0, 4.5, 6.0, 7.5]

# 更复杂的类型注解
from typing import Union, Optional, Callable, Tuple

def advanced_function(
    items: List[Union[int, str]],
    callback: Optional[Callable[[int], int]] = None,
    config: Dict[str, Union[str, int, bool]] = None
) -> Tuple[List[int], int]:
    """复杂类型注解示例"""
    pass
```
</details>

---

## 高阶函数练习

### 21. 函数作为参数
编写函数 `apply_to_list(func, lst)`，将函数应用到列表的每个元素。

<details>
<summary>答案</summary>

```python
def apply_to_list(func, lst):
    """将函数应用到列表每个元素"""
    return [func(item) for item in lst]

# 测试
def square(x):
    return x ** 2

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
print(apply_to_list(square, numbers))  # [1, 4, 9, 16, 25]
print(apply_to_list(double, numbers))  # [2, 4, 6, 8, 10]

# 使用 lambda
print(apply_to_list(lambda x: x + 10, numbers))  # [11, 12, 13, 14, 15]

# 方法2：使用 map
def apply_to_list_v2(func, lst):
    return list(map(func, lst))
```
</details>

---

### 22. 函数作为返回值
编写函数 `make_adder(n)`，返回一个函数，该函数将参数加上 n。

<details>
<summary>答案</summary>

```python
def make_adder(n):
    """创建加法函数"""
    def adder(x):
        return x + n
    return adder

# 测试
add_5 = make_adder(5)
add_10 = make_adder(10)

print(add_5(3))   # 8
print(add_5(10))  # 15
print(add_10(3))  # 13

# 扩展：创建各种运算函数
def make_operator(operation):
    """创建运算函数"""
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    return operations.get(operation)

add = make_operator("add")
multiply = make_operator("multiply")

print(add(3, 5))       # 8
print(multiply(3, 5))  # 15
```
</details>

---


### 23. map 函数应用
使用 `map()` 将字符串列表转换为整数列表。

<details>
<summary>答案</summary>

```python
# 基本用法
strings = ["1", "2", "3", "4", "5"]
numbers = list(map(int, strings))
print(numbers)  # [1, 2, 3, 4, 5]

# 多个可迭代对象
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # [11, 22, 33]

# 实际应用：数据清洗
prices = ["$10.50", "$20.30", "$15.80"]
clean_prices = list(map(lambda x: float(x.replace("$", "")), prices))
print(clean_prices)  # [10.5, 20.3, 15.8]

# 扩展：处理字典列表
students = [
    {"name": "Alice", "score": "85"},
    {"name": "Bob", "score": "92"},
    {"name": "Charlie", "score": "78"}
]

# 将分数转换为整数
def convert_score(student):
    student["score"] = int(student["score"])
    return student

students = list(map(convert_score, students))
print(students)
```
</details>

---

### 24. filter 函数应用
使用 `filter()` 筛选出列表中的偶数。

<details>
<summary>答案</summary>

```python
# 基本用法
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 筛选正数
numbers = [-5, -2, 0, 3, 7, -1, 10]
positive = list(filter(lambda x: x > 0, numbers))
print(positive)  # [3, 7, 10]

# 实际应用：筛选及格学生
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 58},
    {"name": "David", "score": 75}
]

passed = list(filter(lambda s: s["score"] >= 60, students))
print(passed)
# [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}, {'name': 'David', 'score': 75}]

# 扩展：筛选非空字符串
strings = ["hello", "", "world", "  ", "python", ""]
non_empty = list(filter(lambda s: s.strip(), strings))
print(non_empty)  # ['hello', 'world', 'python']
```
</details>

---

### 25. reduce 函数应用
使用 `reduce()` 计算列表中所有数字的乘积。

<details>
<summary>答案</summary>

```python
from functools import reduce

# 计算乘积
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# 带初始值
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# 实际应用：找最大值
numbers = [3, 7, 2, 9, 1, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # 9

# 扩展：展平嵌套列表
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, nested)
print(flattened)  # [1, 2, 3, 4, 5, 6]

# 扩展：统计单词出现次数
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = reduce(
    lambda acc, word: {**acc, word: acc.get(word, 0) + 1},
    words,
    {}
)
print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```
</details>

---

### 26. 组合 map、filter、reduce
从数字列表中筛选出偶数，平方后求和。

<details>
<summary>答案</summary>

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 方法1：分步骤
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x ** 2, even_numbers)
total = reduce(lambda x, y: x + y, squared)
print(total)  # 220 (4 + 16 + 36 + 64 + 100)

# 方法2：链式调用
total = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(total)  # 220

# 方法3：使用列表推导式（更 Pythonic）
total = sum(x ** 2 for x in numbers if x % 2 == 0)
print(total)  # 220

# 实际应用：处理学生数据
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 58},
    {"name": "David", "score": 75}
]

# 计算及格学生的平均分
passed_students = filter(lambda s: s["score"] >= 60, students)
scores = map(lambda s: s["score"], passed_students)
total_score = reduce(lambda x, y: x + y, scores)
count = len(list(filter(lambda s: s["score"] >= 60, students)))
average = total_score / count
print(f"及格学生平均分: {average:.2f}")  # 84.00
```
</details>

---

### 27. 自定义排序
编写函数 `sort_by_key(lst, key_func)`，根据自定义键函数排序。

<details>
<summary>答案</summary>

```python
def sort_by_key(lst, key_func):
    """根据键函数排序"""
    return sorted(lst, key=key_func)

# 测试：按长度排序
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sort_by_key(words, len)
print(sorted_words)  # ['pie', 'apple', 'banana', 'cherry']

# 测试：按第二个元素排序
pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_pairs = sort_by_key(pairs, lambda x: x[1])
print(sorted_pairs)  # [(4, 1), (3, 2), (1, 5), (2, 8)]

# 实际应用：多条件排序
students = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 23, "score": 92},
    {"name": "Charlie", "age": 25, "score": 78},
    {"name": "David", "age": 23, "score": 88}
]

# 先按年龄，再按分数排序
sorted_students = sort_by_key(students, lambda s: (s["age"], -s["score"]))
for s in sorted_students:
    print(f"{s['name']}: {s['age']}岁, {s['score']}分")
# Bob: 23岁, 92分
# David: 23岁, 88分
# Alice: 25岁, 85分
# Charlie: 25岁, 78分
```
</details>

---

### 28. 函数组合
编写函数 `compose(*functions)`，组合多个函数。

<details>
<summary>答案</summary>

```python
def compose(*functions):
    """组合多个函数"""
    def inner(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return inner

# 测试
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# 组合：先加1，再翻倍，最后平方
combined = compose(square, double, add_one)
print(combined(3))  # ((3 + 1) * 2) ** 2 = 64

# 方法2：使用 reduce
from functools import reduce

def compose_v2(*functions):
    return lambda x: reduce(lambda acc, f: f(acc), reversed(functions), x)

combined = compose_v2(square, double, add_one)
print(combined(3))  # 64

# 实际应用：数据处理管道
def remove_spaces(s):
    return s.replace(" ", "")

def to_upper(s):
    return s.upper()

def add_prefix(s):
    return f"PREFIX_{s}"

process = compose(add_prefix, to_upper, remove_spaces)
print(process("hello world"))  # PREFIX_HELLOWORLD
```
</details>

---

### 29. 柯里化
编写函数 `curry(func, arity)`，将多参数函数柯里化。

<details>
<summary>答案</summary>

```python
def curry(func, arity):
    """柯里化函数"""
    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])
        return lambda *more_args: curried(*(args + more_args))
    return curried

# 测试
def add_three(a, b, c):
    return a + b + c

curried_add = curry(add_three, 3)

# 可以一次传入所有参数
print(curried_add(1, 2, 3))  # 6

# 也可以分步传入
print(curried_add(1)(2)(3))  # 6
print(curried_add(1, 2)(3))  # 6
print(curried_add(1)(2, 3))  # 6

# 实际应用：创建专用函数
def multiply(a, b, c):
    return a * b * c

curried_multiply = curry(multiply, 3)

# 创建"乘以2"的函数
times_2 = curried_multiply(2)
print(times_2(3, 4))  # 24

# 创建"乘以2再乘以3"的函数
times_2_3 = curried_multiply(2)(3)
print(times_2_3(4))  # 24
```
</details>

---

### 30. 偏函数应用
使用 `functools.partial` 创建专用的日志函数。

<details>
<summary>答案</summary>

```python
from functools import partial
import time

def log(level, message, timestamp=None):
    """日志函数"""
    if timestamp is None:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

# 创建专用日志函数
info = partial(log, "INFO")
warning = partial(log, "WARNING")
error = partial(log, "ERROR")

# 使用
info("程序启动")
warning("内存使用率较高")
error("连接数据库失败")

# 实际应用：数学运算
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125

# 实际应用：数据验证
def validate(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        raise ValueError(f"{name} 必须在 {min_val} 到 {max_val} 之间")
    return True

validate_age = partial(validate, min_val=0, max_val=120, name="年龄")
validate_score = partial(validate, min_val=0, max_val=100, name="分数")

try:
    validate_age(25)    # 通过
    validate_age(150)   # 抛出异常
except ValueError as e:
    print(e)  # 年龄 必须在 0 到 120 之间
```
</details>

---

## 装饰器练习

### 31. 简单装饰器
编写装饰器 `@timer`，测量函数执行时间。

<details>
<summary>答案</summary>

```python
import time
from functools import wraps

def timer(func):
    """计时装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f}秒")
        return result
    return wrapper

# 测试
@timer
def slow_function():
    time.sleep(1)
    return "完成"

@timer
def calculate_sum(n):
    return sum(range(n))

slow_function()  # slow_function 耗时: 1.0001秒
calculate_sum(1000000)  # calculate_sum 耗时: 0.0234秒

# 扩展：支持多次测量取平均值
def timer_avg(times=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None
            for _ in range(times):
                start = time.time()
                result = func(*args, **kwargs)
                total_time += time.time() - start
            avg_time = total_time / times
            print(f"{func.__name__} 平均耗时: {avg_time:.4f}秒 (测试{times}次)")
            return result
        return wrapper
    return decorator

@timer_avg(times=5)
def test_function():
    time.sleep(0.1)

test_function()
```
</details>

---

### 32. 带参数的装饰器
编写装饰器 `@repeat(n)`，重复执行函数 n 次。

<details>
<summary>答案</summary>

```python
from functools import wraps

def repeat(times):
    """重复执行装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

# 测试
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

results = greet("Alice")
print(results)
# 输出:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
# ['Greeted Alice', 'Greeted Alice', 'Greeted Alice']

# 扩展：只返回最后一次结果
def repeat_v2(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_v2(3)
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# Hello!
# Hello!
# Hello!
```
</details>

---

### 33. 缓存装饰器
编写装饰器 `@cache`，缓存函数的返回值。

<details>
<summary>答案</summary>

```python
from functools import wraps

def cache(func):
    """缓存装饰器"""
    cached_results = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"从缓存获取: {args}")
            return cached_results[args]
        
        print(f"计算中: {args}")
        result = func(*args)
        cached_results[args] = result
        return result
    
    return wrapper

# 测试
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 55
print(fibonacci(10))  # 从缓存获取

# 使用内置的 lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_v2(n):
    if n < 2:
        return n
    return fibonacci_v2(n-1) + fibonacci_v2(n-2)

print(fibonacci_v2(100))  # 很快计算出结果

# 扩展：带过期时间的缓存
import time

def cache_with_ttl(ttl_seconds):
    """带过期时间的缓存"""
    def decorator(func):
        cache = {}
        
        @wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if now - timestamp < ttl_seconds:
                    print(f"从缓存获取: {args}")
                    return result
            
            print(f"计算中: {args}")
            result = func(*args)
            cache[args] = (result, now)
            return result
        
        return wrapper
    return decorator

@cache_with_ttl(ttl_seconds=5)
def expensive_operation(x):
    time.sleep(1)
    return x * 2

print(expensive_operation(5))  # 计算中
print(expensive_operation(5))  # 从缓存获取
time.sleep(6)
print(expensive_operation(5))  # 缓存过期，重新计算
```
</details>

---

### 34. 权限检查装饰器
编写装饰器 `@require_auth`，检查用户是否已登录。

<details>
<summary>答案</summary>

```python
from functools import wraps

def require_auth(func):
    """权限检查装饰器"""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("需要登录")
        return func(user, *args, **kwargs)
    return wrapper

# 测试
@require_auth
def view_profile(user):
    return f"查看 {user['name']} 的个人资料"

@require_auth
def delete_account(user):
    return f"删除 {user['name']} 的账户"

# 已登录用户
logged_in_user = {"name": "Alice", "is_authenticated": True}
print(view_profile(logged_in_user))  # 查看 Alice 的个人资料

# 未登录用户
guest_user = {"name": "Guest", "is_authenticated": False}
try:
    print(view_profile(guest_user))
except PermissionError as e:
    print(f"错误: {e}")  # 错误: 需要登录

# 扩展：检查特定权限
def require_permission(permission):
    """检查特定权限"""
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not user.get("is_authenticated"):
                raise PermissionError("需要登录")
            if permission not in user.get("permissions", []):
                raise PermissionError(f"需要 {permission} 权限")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_permission("admin")
def delete_user(user, target_user_id):
    return f"删除用户 {target_user_id}"

admin_user = {
    "name": "Admin",
    "is_authenticated": True,
    "permissions": ["admin", "moderator"]
}

normal_user = {
    "name": "User",
    "is_authenticated": True,
    "permissions": ["read", "write"]
}

print(delete_user(admin_user, 123))  # 删除用户 123

try:
    print(delete_user(normal_user, 123))
except PermissionError as e:
    print(f"错误: {e}")  # 错误: 需要 admin 权限
```
</details>

---

### 35. 日志装饰器
编写装饰器 `@log`，记录函数的调用信息。

<details>
<summary>答案</summary>

```python
from functools import wraps
import time

def log(func):
    """日志装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] 调用 {func.__name__}")
        print(f"  参数: args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            print(f"  返回: {result}")
            return result
        except Exception as e:
            print(f"  异常: {type(e).__name__}: {e}")
            raise
    
    return wrapper

# 测试
@log
def add(a, b):
    return a + b

@log
def divide(a, b):
    return a / b

add(3, 5)
# [2024-01-01 12:00:00] 调用 add
#   参数: args=(3, 5), kwargs={}
#   返回: 8

try:
    divide(10, 0)
except ZeroDivisionError:
    pass
# [2024-01-01 12:00:00] 调用 divide
#   参数: args=(10, 0), kwargs={}
#   异常: ZeroDivisionError: division by zero

# 扩展：支持日志级别
def log_v2(level="INFO"):
    """支持日志级别的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{level}] 调用 {func.__name__}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@log_v2("DEBUG")
def debug_function():
    print("调试信息")

@log_v2("ERROR")
def error_function():
    print("错误信息")

debug_function()
error_function()
```
</details>

---

### 36. 多个装饰器组合
为函数同时添加 `@timer` 和 `@log` 装饰器，观察执行顺序。

<details>
<summary>答案</summary>

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Timer] 开始计时")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Timer] {func.__name__} 耗时: {end - start:.4f}秒")
        return result
    return wrapper

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Log] 调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[Log] {func.__name__} 完成")
        return result
    return wrapper

# 装饰器从下到上应用，从上到下执行
@timer
@log
def slow_function():
    print("[Function] 执行中...")
    time.sleep(1)
    return "完成"

slow_function()
# 输出:
# [Timer] 开始计时
# [Log] 调用 slow_function
# [Function] 执行中...
# [Log] slow_function 完成
# [Timer] slow_function 耗时: 1.0001秒
```
</details>

---

### 37. 类装饰器
编写类装饰器 `CountCalls`，统计函数调用次数。

<details>
<summary>答案</summary>

```python
class CountCalls:
    """统计函数调用次数的装饰器"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数: {self.count}")
        return self.func(*args, **kwargs)
    
    def reset(self):
        """重置计数"""
        self.count = 0

@CountCalls
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # 调用次数: 1
print(greet("Bob"))    # 调用次数: 2
print(greet("Charlie"))  # 调用次数: 3

greet.reset()
print(greet("David"))  # 调用次数: 1
```
</details>

---

### 38. 装饰器工厂
编写装饰器工厂 `retry(max_attempts)`，失败时自动重试。

<details>
<summary>答案</summary>

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    """重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"尝试 {attempt}/{max_attempts}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        print(f"失败: {e}")
                        raise
                    print(f"失败: {e}，{delay}秒后重试...")
                    time.sleep(delay)
        return wrapper
    return decorator

# 测试
import random

@retry(max_attempts=5, delay=0.5)
def unstable_function():
    """模拟不稳定的函数"""
    if random.random() < 0.7:  # 70% 失败率
        raise ConnectionError("连接失败")
    return "成功"

try:
    result = unstable_function()
    print(f"结果: {result}")
except ConnectionError:
    print("最终失败")
```
</details>

---

### 39. 参数验证装饰器
编写装饰器 `@validate_types`，验证函数参数类型。

<details>
<summary>答案</summary>

```python
from functools import wraps

def validate_types(**type_checks):
    """类型验证装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数参数名
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 验证类型
            for param_name, expected_type in type_checks.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"参数 {param_name} 应为 {expected_type.__name__}，"
                            f"实际为 {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 测试
@validate_types(name=str, age=int, score=float)
def create_student(name, age, score):
    return {"name": name, "age": age, "score": score}

# 正确调用
print(create_student("Alice", 25, 85.5))

# 错误调用
try:
    create_student("Bob", "25", 90.0)  # age 应为 int
except TypeError as e:
    print(f"错误: {e}")
```
</details>

---

### 40. 单例装饰器
编写装饰器 `@singleton`，确保类只有一个实例。

<details>
<summary>答案</summary>

```python
from functools import wraps

def singleton(cls):
    """单例装饰器"""
    instances = {}
    
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

# 测试
@singleton
class Database:
    def __init__(self):
        print("创建数据库连接")
        self.connection = "Connected"

db1 = Database()  # 创建数据库连接
db2 = Database()  # 不会再次创建

print(db1 is db2)  # True（同一个实例）
```
</details>

---

## 生成器练习

### 41. 简单生成器
编写生成器函数 `count_up_to(n)`，生成 0 到 n-1 的数字。

<details>
<summary>答案</summary>

```python
def count_up_to(n):
    """生成 0 到 n-1 的数字"""
    i = 0
    while i < n:
        yield i
        i += 1

# 测试
for num in count_up_to(5):
    print(num, end=' ')  # 0 1 2 3 4

# 手动迭代
counter = count_up_to(3)
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
# print(next(counter))  # StopIteration
```
</details>

---

### 42. 斐波那契生成器
编写生成器函数 `fibonacci()`，生成无限斐波那契数列。

<details>
<summary>答案</summary>

```python
def fibonacci():
    """无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 测试：获取前10个
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=' ')  # 0 1 1 2 3 5 8 13 21 34

# 使用 itertools.islice
from itertools import islice
fib = fibonacci()
first_10 = list(islice(fib, 10))
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
</details>

---

### 43. 文件行读取生成器
编写生成器函数 `read_lines(filename)`，逐行读取文件。

<details>
<summary>答案</summary>

```python
def read_lines(filename):
    """逐行读取文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# 测试（假设有 test.txt 文件）
# for line in read_lines('test.txt'):
#     print(line)

# 扩展：过滤空行
def read_non_empty_lines(filename):
    """读取非空行"""
    for line in read_lines(filename):
        if line:
            yield line

# 扩展：批量读取
def read_in_chunks(filename, chunk_size=1024):
    """分块读取文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk
```
</details>

---

### 44. 范围生成器
编写生成器函数 `my_range(start, stop, step)`，模拟内置 range 函数。

<details>
<summary>答案</summary>

```python
def my_range(start, stop=None, step=1):
    """模拟 range 函数"""
    if stop is None:
        start, stop = 0, start
    
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("step 不能为 0")

# 测试
print(list(my_range(5)))           # [0, 1, 2, 3, 4]
print(list(my_range(2, 8)))        # [2, 3, 4, 5, 6, 7]
print(list(my_range(0, 10, 2)))    # [0, 2, 4, 6, 8]
print(list(my_range(10, 0, -2)))   # [10, 8, 6, 4, 2]
```
</details>

---

### 45. 展平嵌套列表
编写生成器函数 `flatten(nested_list)`，展平嵌套列表。

<details>
<summary>答案</summary>

```python
def flatten(nested_list):
    """展平嵌套列表"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# 测试
nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 方法2：不使用 yield from
def flatten_v2(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            for sub_item in flatten_v2(item):
                yield sub_item
        else:
            yield item
```
</details>

---

### 46. 数据管道
使用生成器创建数据处理管道：读取数字 → 过滤偶数 → 平方 → 求和。

<details>
<summary>答案</summary>

```python
def read_numbers(n):
    """生成数字"""
    for i in range(n):
        yield i

def filter_even(numbers):
    """过滤偶数"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def square(numbers):
    """平方"""
    for num in numbers:
        yield num ** 2

# 组合管道
pipeline = square(filter_even(read_numbers(10)))
result = sum(pipeline)
print(result)  # 0 + 4 + 16 + 36 + 64 = 120

# 方法2：使用生成器表达式
result = sum(x**2 for x in range(10) if x % 2 == 0)
print(result)  # 120
```
</details>

---

### 47. 窗口滑动生成器
编写生成器函数 `sliding_window(iterable, size)`，生成滑动窗口。

<details>
<summary>答案</summary>

```python
from collections import deque

def sliding_window(iterable, size):
    """滑动窗口生成器"""
    it = iter(iterable)
    window = deque(maxlen=size)
    
    # 填充初始窗口
    for _ in range(size):
        try:
            window.append(next(it))
        except StopIteration:
            return
    
    yield tuple(window)
    
    # 滑动窗口
    for item in it:
        window.append(item)
        yield tuple(window)

# 测试
data = [1, 2, 3, 4, 5, 6, 7, 8]
for window in sliding_window(data, 3):
    print(window)
# (1, 2, 3)
# (2, 3, 4)
# (3, 4, 5)
# (4, 5, 6)
# (5, 6, 7)
# (6, 7, 8)

# 应用：计算移动平均
def moving_average(data, window_size):
    for window in sliding_window(data, window_size):
        yield sum(window) / len(window)

prices = [10, 12, 13, 11, 14, 15, 13, 16]
ma = list(moving_average(prices, 3))
print(ma)  # [11.67, 12.0, 12.67, 13.33, 14.0, 14.67]
```
</details>

---

### 48. 生成器表达式
将以下列表推导式改写为生成器表达式，并比较内存使用。

<details>
<summary>答案</summary>

```python
import sys

# 列表推导式
squares_list = [x**2 for x in range(1000000)]
print(f"列表大小: {sys.getsizeof(squares_list)} 字节")

# 生成器表达式
squares_gen = (x**2 for x in range(1000000))
print(f"生成器大小: {sys.getsizeof(squares_gen)} 字节")

# 列表大小: 约 8MB
# 生成器大小: 约 128 字节

# 实际应用：处理大数据
def process_large_file(filename):
    # ❌ 内存占用大
    # lines = [line.strip() for line in open(filename)]
    
    # ✅ 内存友好
    lines = (line.strip() for line in open(filename))
    return lines
```
</details>

---

### 49. 生成器的 send 方法
编写生成器，使用 `send()` 方法接收外部值。

<details>
<summary>答案</summary>

```python
def echo_generator():
    """回显生成器"""
    print("生成器启动")
    while True:
        value = yield
        if value is not None:
            print(f"收到: {value}")
            yield f"回显: {value}"

# 测试
gen = echo_generator()
next(gen)  # 启动生成器

print(gen.send("Hello"))  # 收到: Hello, 回显: Hello
print(gen.send("World"))  # 收到: World, 回显: World

# 实际应用：累加器
def accumulator():
    """累加器生成器"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
next(acc)  # 启动
print(acc.send(10))  # 10
print(acc.send(20))  # 30
print(acc.send(5))   # 35
```
</details>

---

### 50. 协程模拟
使用生成器模拟简单的协程。

<details>
<summary>答案</summary>

```python
def producer(consumer):
    """生产者"""
    print("生产者启动")
    for i in range(5):
        print(f"生产: {i}")
        consumer.send(i)
    consumer.close()

def consumer_gen():
    """消费者生成器"""
    print("消费者启动")
    while True:
        value = yield
        print(f"消费: {value}")

# 测试
consumer = consumer_gen()
next(consumer)  # 启动消费者
producer(consumer)

# 输出:
# 消费者启动
# 生产者启动
# 生产: 0
# 消费: 0
# 生产: 1
# 消费: 1
# ...
```
</details>

---

## 递归练习

### 51. 计算阶乘
使用递归计算 n 的阶乘。

<details>
<summary>答案</summary>

```python
def factorial(n):
    """递归计算阶乘"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(10))  # 3628800

# 尾递归优化版本
def factorial_tail(n, acc=1):
    if n == 0 or n == 1:
        return acc
    return factorial_tail(n - 1, n * acc)

print(factorial_tail(5))  # 120
```
</details>

---

### 52. 斐波那契数列
使用递归计算第 n 个斐波那契数。

<details>
<summary>答案</summary>

```python
def fibonacci(n):
    """递归计算斐波那契数"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 优化：使用记忆化
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n
    return fibonacci_memo(n-1) + fibonacci_memo(n-2)

print(fibonacci_memo(100))  # 很快计算出结果
```
</details>

---

### 53. 二分查找
使用递归实现二分查找。

<details>
<summary>答案</summary>

```python
def binary_search(arr, target, left, right):
    """递归二分查找"""
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

# 测试
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(numbers, 7, 0, len(numbers)-1))   # 3
print(binary_search(numbers, 15, 0, len(numbers)-1))  # 7
print(binary_search(numbers, 20, 0, len(numbers)-1))  # -1

# 简化版本
def binary_search_v2(arr, target):
    if not arr:
        return -1
    
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_v2(arr[:mid], target)
    else:
        result = binary_search_v2(arr[mid+1:], target)
        return -1 if result == -1 else mid + 1 + result
```
</details>

---

### 54. 汉诺塔
使用递归解决汉诺塔问题。

<details>
<summary>答案</summary>

```python
def hanoi(n, source, target, auxiliary):
    """
    汉诺塔问题
    n: 盘子数量
    source: 起始柱
    target: 目标柱
    auxiliary: 辅助柱
    """
    if n == 1:
        print(f"移动盘子 1 从 {source} 到 {target}")
        return
    
    # 将 n-1 个盘子从 source 移到 auxiliary
    hanoi(n-1, source, auxiliary, target)
    
    # 将最大的盘子从 source 移到 target
    print(f"移动盘子 {n} 从 {source} 到 {target}")
    
    # 将 n-1 个盘子从 auxiliary 移到 target
    hanoi(n-1, auxiliary, target, source)

# 测试
hanoi(3, 'A', 'C', 'B')
# 输出:
# 移动盘子 1 从 A 到 C
# 移动盘子 2 从 A 到 B
# 移动盘子 1 从 C 到 B
# 移动盘子 3 从 A 到 C
# 移动盘子 1 从 B 到 A
# 移动盘子 2 从 B 到 C
# 移动盘子 1 从 A 到 C

# 统计移动次数
def hanoi_count(n):
    if n == 1:
        return 1
    return 2 * hanoi_count(n-1) + 1

print(f"3个盘子需要移动 {hanoi_count(3)} 次")  # 7次
```
</details>

---

### 55. 树的遍历
使用递归遍历二叉树。

<details>
<summary>答案</summary>

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(node):
    """中序遍历：左 → 根 → 右"""
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=' ')
    inorder(node.right)

def preorder(node):
    """前序遍历：根 → 左 → 右"""
    if node is None:
        return
    print(node.value, end=' ')
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    """后序遍历：左 → 右 → 根"""
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=' ')

# 构建测试树
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("中序遍历:", end=' ')
inorder(root)    # 4 2 5 1 3
print("\n前序遍历:", end=' ')
preorder(root)   # 1 2 4 5 3
print("\n后序遍历:", end=' ')
postorder(root)  # 4 5 2 3 1
```
</details>

---

### 56. 全排列
使用递归生成列表的所有排列。

<details>
<summary>答案</summary>

```python
def permutations(arr):
    """生成所有排列"""
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        # 选择当前元素
        current = arr[i]
        # 剩余元素
        remaining = arr[:i] + arr[i+1:]
        # 递归生成剩余元素的排列
        for perm in permutations(remaining):
            result.append([current] + perm)
    
    return result

# 测试
print(permutations([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# 使用内置函数
from itertools import permutations as perm
print(list(perm([1, 2, 3])))
```
</details>

---

### 57. 组合
使用递归生成列表的所有组合。

<details>
<summary>答案</summary>

```python
def combinations(arr, k):
    """生成长度为 k 的所有组合"""
    if k == 0:
        return [[]]
    if not arr:
        return []
    
    # 包含第一个元素的组合
    with_first = [[arr[0]] + combo for combo in combinations(arr[1:], k-1)]
    # 不包含第一个元素的组合
    without_first = combinations(arr[1:], k)
    
    return with_first + without_first

# 测试
print(combinations([1, 2, 3, 4], 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# 使用内置函数
from itertools import combinations as comb
print(list(comb([1, 2, 3, 4], 2)))
```
</details>

---

### 58. 幂集
使用递归生成集合的幂集（所有子集）。

<details>
<summary>答案</summary>

```python
def power_set(arr):
    """生成幂集"""
    if not arr:
        return [[]]
    
    # 递归生成剩余元素的幂集
    subsets = power_set(arr[1:])
    
    # 将当前元素添加到每个子集中
    with_first = [[arr[0]] + subset for subset in subsets]
    
    return subsets + with_first

# 测试
print(power_set([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

# 方法2：使用位运算
def power_set_v2(arr):
    n = len(arr)
    result = []
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    return result

print(power_set_v2([1, 2, 3]))
```
</details>

---

### 59. 路径和
给定二叉树，判断是否存在从根到叶子的路径，其节点值之和等于目标值。

<details>
<summary>答案</summary>

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def has_path_sum(root, target_sum):
    """判断是否存在路径和等于目标值"""
    if root is None:
        return False
    
    # 叶子节点
    if root.left is None and root.right is None:
        return root.value == target_sum
    
    # 递归检查左右子树
    remaining = target_sum - root.value
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))

# 测试
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(has_path_sum(root, 22))  # True (5→4→11→2)
print(has_path_sum(root, 26))  # True (5→8→13)
print(has_path_sum(root, 100)) # False
```
</details>

---

### 60. 字符串反转
使用递归反转字符串。

<details>
<summary>答案</summary>

```python
def reverse_string(s):
    """递归反转字符串"""
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

# 测试
print(reverse_string("hello"))   # olleh
print(reverse_string("Python"))  # nohtyP

# 方法2：使用切片（更高效）
def reverse_string_v2(s):
    return s[::-1]

# 方法3：尾递归
def reverse_string_tail(s, acc=""):
    if not s:
        return acc
    return reverse_string_tail(s[1:], s[0] + acc)

print(reverse_string_tail("hello"))  # olleh
```
</details>

---

## 综合应用

### 61. 实现 map 函数
自己实现 `map()` 函数的功能。

<details>
<summary>答案</summary>

```python
def my_map(func, iterable):
    """自定义 map 函数"""
    result = []
    for item in iterable:
        result.append(func(item))
    return result

# 测试
numbers = [1, 2, 3, 4, 5]
squared = my_map(lambda x: x ** 2, numbers)
print(squared)  # [1, 4, 9, 16, 25]

# 生成器版本
def my_map_gen(func, iterable):
    for item in iterable:
        yield func(item)

squared_gen = my_map_gen(lambda x: x ** 2, numbers)
print(list(squared_gen))  # [1, 4, 9, 16, 25]

# 支持多个可迭代对象
def my_map_multi(func, *iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            args = [next(it) for it in iterators]
            yield func(*args)
        except StopIteration:
            break

result = my_map_multi(lambda x, y: x + y, [1, 2, 3], [10, 20, 30])
print(list(result))  # [11, 22, 33]
```
</details>

---

### 62. 实现 filter 函数
自己实现 `filter()` 函数的功能。

<details>
<summary>答案</summary>

```python
def my_filter(func, iterable):
    """自定义 filter 函数"""
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

# 测试
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = my_filter(lambda x: x % 2 == 0, numbers)
print(even)  # [2, 4, 6, 8, 10]

# 生成器版本
def my_filter_gen(func, iterable):
    for item in iterable:
        if func(item):
            yield item

even_gen = my_filter_gen(lambda x: x % 2 == 0, numbers)
print(list(even_gen))  # [2, 4, 6, 8, 10]

# 支持 None 作为函数（过滤假值）
def my_filter_v2(func, iterable):
    if func is None:
        func = bool
    for item in iterable:
        if func(item):
            yield item

mixed = [0, 1, False, True, "", "hello", None, [1, 2]]
print(list(my_filter_v2(None, mixed)))  # [1, True, 'hello', [1, 2]]
```
</details>

---

### 63. 实现 reduce 函数
自己实现 `reduce()` 函数的功能。

<details>
<summary>答案</summary>

```python
def my_reduce(func, iterable, initializer=None):
    """自定义 reduce 函数"""
    it = iter(iterable)
    
    # 确定初始值
    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value")
    else:
        value = initializer
    
    # 累积计算
    for item in it:
        value = func(value, item)
    
    return value

# 测试
numbers = [1, 2, 3, 4, 5]
sum_result = my_reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15

product = my_reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# 实际应用：展平列表
nested = [[1, 2], [3, 4], [5, 6]]
flattened = my_reduce(lambda x, y: x + y, nested)
print(flattened)  # [1, 2, 3, 4, 5, 6]
```
</details>

---

### 64. 函数缓存实现
实现一个通用的函数缓存装饰器。

<details>
<summary>答案</summary>

```python
from functools import wraps
import time

def cache_with_expiry(ttl_seconds=None, maxsize=128):
    """
    带过期时间和大小限制的缓存装饰器
    ttl_seconds: 缓存过期时间（秒）
    maxsize: 最大缓存数量
    """
    def decorator(func):
        cache = {}
        cache_order = []  # 记录缓存顺序（LRU）
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            
            # 检查缓存
            if key in cache:
                result, timestamp = cache[key]
                # 检查是否过期
                if ttl_seconds is None or now - timestamp < ttl_seconds:
                    # 更新访问顺序（LRU）
                    cache_order.remove(key)
                    cache_order.append(key)
                    return result
                else:
                    # 过期，删除缓存
                    del cache[key]
                    cache_order.remove(key)
            
            # 计算结果
            result = func(*args, **kwargs)
            
            # 存入缓存
            cache[key] = (result, now)
            cache_order.append(key)
            
            # 检查缓存大小
            if len(cache) > maxsize:
                # 删除最旧的缓存（LRU）
                oldest_key = cache_order.pop(0)
                del cache[oldest_key]
            
            return result
        
        # 添加缓存管理方法
        def cache_info():
            return {
                "size": len(cache),
                "maxsize": maxsize,
                "ttl": ttl_seconds
            }
        
        def cache_clear():
            cache.clear()
            cache_order.clear()
        
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear
        
        return wrapper
    return decorator

# 测试
@cache_with_expiry(ttl_seconds=5, maxsize=3)
def expensive_function(x):
    print(f"计算 {x}")
    time.sleep(1)
    return x * 2

print(expensive_function(5))  # 计算 5
print(expensive_function(5))  # 从缓存获取
print(expensive_function.cache_info())  # {'size': 1, 'maxsize': 3, 'ttl': 5}

time.sleep(6)
print(expensive_function(5))  # 缓存过期，重新计算
```
</details>

---

### 65. 实现管道函数
实现一个管道函数，将多个函数串联起来。

<details>
<summary>答案</summary>

```python
def pipe(*functions):
    """管道函数：从左到右依次应用函数"""
    def inner(arg):
        result = arg
        for func in functions:
            result = func(result)
        return result
    return inner

# 测试
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# 创建管道：加1 → 翻倍 → 平方
pipeline = pipe(add_one, double, square)
print(pipeline(3))  # ((3 + 1) * 2) ** 2 = 64

# 实际应用：数据处理
def remove_spaces(s):
    return s.replace(" ", "")

def to_lower(s):
    return s.lower()

def reverse(s):
    return s[::-1]

process_string = pipe(remove_spaces, to_lower, reverse)
print(process_string("Hello World"))  # dlrowolleh
```
</details>

---

### 66. 函数重试机制
实现一个通用的函数重试装饰器，支持指数退避。

<details>
<parameter name="summary">答案</summary>

```python
import time
from functools import wraps

def retry_with_backoff(max_attempts=3, base_delay=1, max_delay=60, backoff_factor=2):
    """
    带指数退避的重试装饰器
    max_attempts: 最大尝试次数
    base_delay: 基础延迟时间（秒）
    max_delay: 最大延迟时间（秒）
    backoff_factor: 退避因子
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = base_delay
            
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"尝试 {attempt}/{max_attempts}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        print(f"最终失败: {e}")
                        raise
                    
                    print(f"失败: {e}，{delay}秒后重试...")
                    time.sleep(delay)
                    
                    # 指数退避
                    delay = min(delay * backoff_factor, max_delay)
        
        return wrapper
    return decorator

# 测试
import random

@retry_with_backoff(max_attempts=5, base_delay=0.5, backoff_factor=2)
def unstable_api_call():
    """模拟不稳定的 API 调用"""
    if random.random() < 0.7:
        raise ConnectionError("网络错误")
    return "成功"

try:
    result = unstable_api_call()
    print(f"结果: {result}")
except ConnectionError:
    print("所有尝试都失败了")
```
</details>

---

### 67. 函数调用统计
实现一个装饰器，统计函数的调用次数、总耗时、平均耗时等信息。

<details>
<summary>答案</summary>

```python
import time
from functools import wraps

def profile(func):
    """性能分析装饰器"""
    stats = {
        "calls": 0,
        "total_time": 0,
        "min_time": float('inf'),
        "max_time": 0
    }
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        
        # 更新统计信息
        stats["calls"] += 1
        stats["total_time"] += elapsed
        stats["min_time"] = min(stats["min_time"], elapsed)
        stats["max_time"] = max(stats["max_time"], elapsed)
        
        return result
    
    def get_stats():
        if stats["calls"] == 0:
            return "函数未被调用"
        
        avg_time = stats["total_time"] / stats["calls"]
        return {
            "调用次数": stats["calls"],
            "总耗时": f"{stats['total_time']:.4f}秒",
            "平均耗时": f"{avg_time:.4f}秒",
            "最小耗时": f"{stats['min_time']:.4f}秒",
            "最大耗时": f"{stats['max_time']:.4f}秒"
        }
    
    def reset_stats():
        stats["calls"] = 0
        stats["total_time"] = 0
        stats["min_time"] = float('inf')
        stats["max_time"] = 0
    
    wrapper.get_stats = get_stats
    wrapper.reset_stats = reset_stats
    
    return wrapper

# 测试
@profile
def calculate(n):
    time.sleep(0.1)
    return sum(range(n))

for i in range(5):
    calculate(1000)

print(calculate.get_stats())
# {
#     '调用次数': 5,
#     '总耗时': '0.5012秒',
#     '平均耗时': '0.1002秒',
#     '最小耗时': '0.1001秒',
#     '最大耗时': '0.1005秒'
# }
```
</details>

---

### 68. 函数参数验证器
实现一个通用的参数验证装饰器。

<details>
<summary>答案</summary>

```python
from functools import wraps

def validate(**validators):
    """
    参数验证装饰器
    validators: 参数名 -> 验证函数的映射
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数签名
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # 验证每个参数
            for param_name, validator_func in validators.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not validator_func(value):
                        raise ValueError(
                            f"参数 {param_name} 验证失败: {value}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 定义验证函数
def is_positive(x):
    return x > 0

def is_email(s):
    return "@" in s and "." in s

def is_adult(age):
    return 18 <= age <= 120

# 测试
@validate(
    age=is_adult,
    email=is_email,
    salary=is_positive
)
def create_employee(name, age, email, salary):
    return {
        "name": name,
        "age": age,
        "email": email,
        "salary": salary
    }

# 正确调用
emp = create_employee("Alice", 25, "alice@example.com", 50000)
print(emp)

# 错误调用
try:
    create_employee("Bob", 15, "bob@example.com", 50000)
except ValueError as e:
    print(f"错误: {e}")  # 错误: 参数 age 验证失败: 15
```
</details>

---

### 69. 实现 partial 函数
自己实现 `functools.partial` 的功能。

<details>
<summary>答案</summary>

```python
class Partial:
    """自定义 partial 类"""
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def __call__(self, *more_args, **more_kwargs):
        # 合并参数
        all_args = self.args + more_args
        all_kwargs = {**self.kwargs, **more_kwargs}
        return self.func(*all_args, **all_kwargs)

# 测试
def power(base, exponent):
    return base ** exponent

square = Partial(power, exponent=2)
cube = Partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125

# 函数版本
def my_partial(func, *args, **kwargs):
    """函数式 partial 实现"""
    def wrapper(*more_args, **more_kwargs):
        all_args = args + more_args
        all_kwargs = {**kwargs, **more_kwargs}
        return func(*all_args, **all_kwargs)
    return wrapper

double = my_partial(power, exponent=2)
print(double(10))  # 100
```
</details>

---

### 70. 实现函数组合器
实现一个函数组合器，支持链式调用。

<details>
<summary>答案</summary>

```python
class FunctionComposer:
    """函数组合器"""
    def __init__(self, value):
        self.value = value
    
    def map(self, func):
        """应用函数"""
        self.value = func(self.value)
        return self
    
    def filter(self, predicate):
        """过滤（仅对列表有效）"""
        if isinstance(self.value, list):
            self.value = [x for x in self.value if predicate(x)]
        return self
    
    def reduce(self, func, initial=None):
        """归约（仅对列表有效）"""
        if isinstance(self.value, list):
            from functools import reduce
            if initial is None:
                self.value = reduce(func, self.value)
            else:
                self.value = reduce(func, self.value, initial)
        return self
    
    def get(self):
        """获取最终值"""
        return self.value

# 测试
result = (FunctionComposer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    .filter(lambda x: x % 2 == 0)  # 过滤偶数
    .map(lambda lst: [x ** 2 for x in lst])  # 平方
    .reduce(lambda x, y: x + y)  # 求和
    .get())

print(result)  # 220 (4 + 16 + 36 + 64 + 100)

# 字符串处理示例
result = (FunctionComposer("  Hello World  ")
    .map(str.strip)
    .map(str.lower)
    .map(lambda s: s.replace(" ", "_"))
    .get())

print(result)  # hello_world
```
</details>

---

### 71. 实现记忆化装饰器
实现一个支持任意参数的记忆化装饰器。

<details>
<summary>答案</summary>

```python
from functools import wraps
import pickle

def memoize(func):
    """记忆化装饰器"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 生成缓存键（处理不可哈希的参数）
        try:
            key = (args, tuple(sorted(kwargs.items())))
        except TypeError:
            # 参数不可哈希，使用 pickle 序列化
            key = pickle.dumps((args, kwargs))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        
        return cache[key]
    
    # 添加缓存管理方法
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    wrapper.cache_info = lambda: {"size": len(cache)}
    
    return wrapper

# 测试
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # 很快计算出结果
print(fibonacci.cache_info())  # {'size': 101}

# 支持复杂参数
@memoize
def complex_function(a, b, options=None):
    if options is None:
        options = {}
    return a + b + options.get("offset", 0)

print(complex_function(1, 2, {"offset": 10}))  # 13
print(complex_function(1, 2, {"offset": 10}))  # 从缓存获取
```
</details>

---

### 72. 实现函数调度器
实现一个简单的函数调度器，根据条件选择执行不同的函数。

<details>
<summary>答案</summary>

```python
class FunctionDispatcher:
    """函数调度器"""
    def __init__(self):
        self.handlers = []
    
    def register(self, condition):
        """注册处理函数"""
        def decorator(func):
            self.handlers.append((condition, func))
            return func
        return decorator
    
    def dispatch(self, *args, **kwargs):
        """调度执行"""
        for condition, handler in self.handlers:
            if condition(*args, **kwargs):
                return handler(*args, **kwargs)
        raise ValueError("没有匹配的处理函数")

# 测试：根据类型处理数据
dispatcher = FunctionDispatcher()

@dispatcher.register(lambda x: isinstance(x, int))
def handle_int(x):
    return f"整数: {x * 2}"

@dispatcher.register(lambda x: isinstance(x, str))
def handle_str(x):
    return f"字符串: {x.upper()}"

@dispatcher.register(lambda x: isinstance(x, list))
def handle_list(x):
    return f"列表: {sum(x)}"

# 使用
print(dispatcher.dispatch(42))        # 整数: 84
print(dispatcher.dispatch("hello"))   # 字符串: HELLO
print(dispatcher.dispatch([1, 2, 3])) # 列表: 6

# 实际应用：HTTP 请求处理
http_dispatcher = FunctionDispatcher()

@http_dispatcher.register(lambda method, path: method == "GET" and path == "/")
def handle_home(method, path):
    return "首页"

@http_dispatcher.register(lambda method, path: method == "GET" and path.startswith("/user/"))
def handle_user(method, path):
    user_id = path.split("/")[-1]
    return f"用户页面: {user_id}"

@http_dispatcher.register(lambda method, path: method == "POST" and path == "/api/data")
def handle_api(method, path):
    return "API 处理"

print(http_dispatcher.dispatch("GET", "/"))           # 首页
print(http_dispatcher.dispatch("GET", "/user/123"))   # 用户页面: 123
print(http_dispatcher.dispatch("POST", "/api/data"))  # API 处理
```
</details>

---

### 73. 实现异步函数模拟
使用生成器模拟简单的异步函数执行。

<details>
<summary>答案</summary>

```python
import time

class Task:
    """任务类"""
    def __init__(self, gen):
        self.gen = gen
    
    def step(self):
        """执行一步"""
        try:
            next(self.gen)
            return True  # 继续执行
        except StopIteration:
            return False  # 任务完成

class EventLoop:
    """简单的事件循环"""
    def __init__(self):
        self.tasks = []
    
    def create_task(self, gen):
        """创建任务"""
        task = Task(gen)
        self.tasks.append(task)
    
    def run(self):
        """运行事件循环"""
        while self.tasks:
            for task in self.tasks[:]:
                if not task.step():
                    self.tasks.remove(task)

# 模拟异步函数
def async_function(name, count):
    """模拟异步函数"""
    for i in range(count):
        print(f"{name}: {i}")
        yield  # 让出控制权

# 测试
loop = EventLoop()
loop.create_task(async_function("任务A", 3))
loop.create_task(async_function("任务B", 3))
loop.create_task(async_function("任务C", 3))
loop.run()

# 输出（交替执行）:
# 任务A: 0
# 任务B: 0
# 任务C: 0
# 任务A: 1
# 任务B: 1
# 任务C: 1
# 任务A: 2
# 任务B: 2
# 任务C: 2
```
</details>

---

### 74. 实现函数管道验证
实现一个函数管道，每一步都进行数据验证。

<details>
<summary>答案</summary>

```python
class Pipeline:
    """带验证的函数管道"""
    def __init__(self, initial_value):
        self.value = initial_value
        self.steps = []
    
    def add_step(self, func, validator=None, error_msg="验证失败"):
        """添加处理步骤"""
        self.steps.append((func, validator, error_msg))
        return self
    
    def execute(self):
        """执行管道"""
        for i, (func, validator, error_msg) in enumerate(self.steps):
            try:
                # 执行函数
                self.value = func(self.value)
                
                # 验证结果
                if validator and not validator(self.value):
                    raise ValueError(f"步骤 {i+1} {error_msg}: {self.value}")
            
            except Exception as e:
                print(f"步骤 {i+1} 失败: {e}")
                raise
        
        return self.value

# 测试：数据处理管道
pipeline = (Pipeline("  hello world  ")
    .add_step(
        str.strip,
        lambda x: len(x) > 0,
        "字符串不能为空"
    )
    .add_step(
        str.lower,
        lambda x: x.islower(),
        "必须是小写"
    )
    .add_step(
        lambda s: s.replace(" ", "_"),
        lambda x: "_" in x,
        "必须包含下划线"
    ))

result = pipeline.execute()
print(result)  # hello_world

# 数值处理管道
num_pipeline = (Pipeline(10)
    .add_step(
        lambda x: x * 2,
        lambda x: x > 0,
        "结果必须为正数"
    )
    .add_step(
        lambda x: x - 5,
        lambda x: x >= 10,
        "结果必须 >= 10"
    ))

result = num_pipeline.execute()
print(result)  # 15
```
</details>

---

### 75. 综合项目：函数式计算器
实现一个函数式风格的计算器，支持链式调用。

<details>
<summary>答案</summary>

```python
class Calculator:
    """函数式计算器"""
    def __init__(self, value=0):
        self.value = value
        self.history = []
    
    def add(self, n):
        """加法"""
        self.history.append(f"{self.value} + {n}")
        self.value += n
        return self
    
    def subtract(self, n):
        """减法"""
        self.history.append(f"{self.value} - {n}")
        self.value -= n
        return self
    
    def multiply(self, n):
        """乘法"""
        self.history.append(f"{self.value} * {n}")
        self.value *= n
        return self
    
    def divide(self, n):
        """除法"""
        if n == 0:
            raise ValueError("除数不能为零")
        self.history.append(f"{self.value} / {n}")
        self.value /= n
        return self
    
    def power(self, n):
        """幂运算"""
        self.history.append(f"{self.value} ** {n}")
        self.value **= n
        return self
    
    def sqrt(self):
        """平方根"""
        import math
        self.history.append(f"sqrt({self.value})")
        self.value = math.sqrt(self.value)
        return self
    
    def abs(self):
        """绝对值"""
        self.history.append(f"abs({self.value})")
        self.value = abs(self.value)
        return self
    
    def round(self, decimals=0):
        """四舍五入"""
        self.history.append(f"round({self.value}, {decimals})")
        self.value = round(self.value, decimals)
        return self
    
    def get(self):
        """获取结果"""
        return self.value
    
    def show_history(self):
        """显示计算历史"""
        print("计算历史:")
        for step in self.history:
            print(f"  {step}")
        print(f"结果: {self.value}")

# 测试
calc = Calculator(10)
result = (calc
    .add(5)        # 10 + 5 = 15
    .multiply(2)   # 15 * 2 = 30
    .subtract(10)  # 30 - 10 = 20
    .divide(4)     # 20 / 4 = 5
    .power(2)      # 5 ** 2 = 25
    .sqrt()        # sqrt(25) = 5
    .get())

print(f"最终结果: {result}")  # 5.0
calc.show_history()

# 复杂计算
calc2 = Calculator(100)
result2 = (calc2
    .subtract(50)
    .multiply(2)
    .divide(5)
    .add(10)
    .round(2)
    .get())

print(f"\n最终结果: {result2}")  # 30.0
calc2.show_history()
```
</details>

---

## 总结

通过这 75 道练习题，你应该已经掌握了：

1. **基础函数**：定义、调用、参数、返回值
2. **参数类型**：位置参数、默认参数、*args、**kwargs
3. **高阶函数**：map、filter、reduce、函数作为参数和返回值
4. **装饰器**：简单装饰器、带参数装饰器、类装饰器
5. **生成器**：yield、生成器表达式、yield from
6. **递归**：基础递归、尾递归、递归优化
7. **综合应用**：实现内置函数、缓存、管道、调度器等

### 学习建议

1. **循序渐进**：从基础题开始，逐步挑战高级题目
2. **多种解法**：尝试用不同方法解决同一问题
3. **理解原理**：不仅要会写，还要理解为什么这样写
4. **实际应用**：将学到的知识应用到实际项目中
5. **代码审查**：与他人交流，学习更好的实现方式

继续加油！🚀

