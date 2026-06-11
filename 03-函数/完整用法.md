# Python3 函数详细用法

## 目录
1. [函数基础](#1-函数基础)
2. [参数详解](#2-参数详解)
3. [返回值](#3-返回值)
4. [作用域与命名空间](#4-作用域与命名空间)
5. [高阶函数](#5-高阶函数)
6. [Lambda 表达式](#6-lambda-表达式)
7. [装饰器](#7-装饰器)
8. [生成器函数](#8-生成器函数)
9. [递归函数](#9-递归函数)
10. [内置函数详解](#10-内置函数详解)
11. [函数式编程](#11-函数式编程)
12. [闭包](#12-闭包)
13. [函数注解](#13-函数注解)
14. [最佳实践](#14-最佳实践)

---

## 1. 函数基础

### 1.1 什么是函数

函数是**可重用的代码块**，用于执行特定任务。

**函数的优点：**
- 代码复用
- 模块化
- 易于维护
- 提高可读性

### 1.2 函数定义

```python
# 基本语法
def function_name(parameters):
    """文档字符串（docstring）"""
    # 函数体
    return result

# 示例：简单函数
def greet():
    """打印问候语"""
    print("Hello, World!")

greet()  # 调用函数
# 输出: Hello, World!
```

### 1.3 函数命名规范

```python
# ✅ 推荐：使用小写字母和下划线
def calculate_sum():
    pass

def get_user_name():
    pass

# ❌ 不推荐：驼峰命名（Python 风格）
def calculateSum():
    pass

# ❌ 不推荐：大写开头（保留给类）
def CalculateSum():
    pass
```

### 1.4 文档字符串（Docstring）

```python
def add(a, b):
    """
    计算两个数的和
    
    参数:
        a (int/float): 第一个数
        b (int/float): 第二个数
    
    返回:
        int/float: 两数之和
    
    示例:
        >>> add(2, 3)
        5
    """
    return a + b

# 查看文档字符串
print(add.__doc__)
help(add)
```

### 1.5 函数调用

```python
def multiply(x, y):
    return x * y

# 位置参数调用
result = multiply(3, 4)  # 12

# 关键字参数调用
result = multiply(x=3, y=4)  # 12
result = multiply(y=4, x=3)  # 12（顺序无关）

# 混合调用（位置参数必须在前）
result = multiply(3, y=4)  # 12
# result = multiply(x=3, 4)  # SyntaxError
```

---

## 2. 参数详解

### 2.1 位置参数（Positional Arguments）

```python
def introduce(name, age, city):
    print(f"我叫{name}，{age}岁，来自{city}")

# 必须按顺序传递
introduce("Alice", 25, "北京")
# 输出: 我叫Alice，25岁，来自北京

# 顺序错误会导致逻辑错误
introduce(25, "Alice", "北京")
# 输出: 我叫25，Alice岁，来自北京（错误！）
```

### 2.2 默认参数（Default Arguments）

```python
def greet(name, greeting="你好"):
    print(f"{greeting}, {name}!")

greet("Alice")              # 你好, Alice!
greet("Bob", "Hello")       # Hello, Bob!
greet("Charlie", greeting="Hi")  # Hi, Charlie!

# ⚠️ 默认参数必须在位置参数之后
# def func(a=1, b):  # SyntaxError
#     pass

def func(b, a=1):  # ✅ 正确
    pass
```

#### 默认参数陷阱：可变对象

```python
# ❌ 危险：可变默认参数
def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] - 意外！
print(append_to_list(3))  # [1, 2, 3] - 继续累积

# 原因：默认参数在函数定义时创建一次，所有调用共享

# ✅ 正确做法
def append_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [2] - 正确
```

### 2.3 可变参数：*args

```python
# *args 收集任意数量的位置参数为元组
def sum_all(*numbers):
    """计算所有数字的和"""
    print(f"参数类型: {type(numbers)}")  # <class 'tuple'>
    return sum(numbers)

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all())                  # 0

# 示例：灵活的打印函数
def print_info(title, *items):
    print(f"{title}:")
    for item in items:
        print(f"  - {item}")

print_info("水果", "苹果", "香蕉", "橙子")
# 输出:
# 水果:
#   - 苹果
#   - 香蕉
#   - 橙子
```

### 2.4 关键字参数：**kwargs

```python
# **kwargs 收集任意数量的关键字参数为字典
def print_user_info(**info):
    """打印用户信息"""
    print(f"参数类型: {type(info)}")  # <class 'dict'>
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, city="北京")
# 输出:
# 参数类型: <class 'dict'>
# name: Alice
# age: 25
# city: 北京

# 示例：配置函数
def configure_server(host, port, **options):
    print(f"服务器: {host}:{port}")
    print("配置选项:")
    for key, value in options.items():
        print(f"  {key} = {value}")

configure_server("localhost", 8080, 
                 debug=True, 
                 timeout=30, 
                 max_connections=100)
```

### 2.5 参数顺序规则

```python
# 参数顺序：位置参数 → 默认参数 → *args → **kwargs
def complex_function(a, b, c=10, *args, **kwargs):
    print(f"a={a}, b={b}, c={c}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

complex_function(1, 2, 3, 4, 5, x=100, y=200)
# 输出:
# a=1, b=2, c=3
# args=(4, 5)
# kwargs={'x': 100, 'y': 200}

# 完整顺序示例
def full_example(pos1, pos2, default1=10, *args, kw_only, **kwargs):
    pass

# pos1, pos2: 位置参数
# default1: 默认参数
# *args: 可变位置参数
# kw_only: 仅限关键字参数（Python 3+）
# **kwargs: 可变关键字参数
```

### 2.6 仅限关键字参数（Keyword-Only Arguments）

```python
# * 后面的参数必须使用关键字传递
def create_user(name, age, *, email, phone):
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    print(f"邮箱: {email}")
    print(f"电话: {phone}")

# ✅ 正确
create_user("Alice", 25, email="alice@example.com", phone="123456")

# ❌ 错误：email 和 phone 必须使用关键字
# create_user("Alice", 25, "alice@example.com", "123456")  # TypeError

# 实际应用：强制使用关键字提高可读性
def connect_database(host, port, *, username, password, timeout=30):
    """
    连接数据库
    username 和 password 必须使用关键字，避免混淆
    """
    pass

connect_database("localhost", 5432, 
                 username="admin", 
                 password="secret")
```

### 2.7 仅限位置参数（Positional-Only Arguments）

```python
# Python 3.8+: / 前面的参数只能使用位置传递
def divide(a, b, /):
    """a 和 b 只能通过位置传递"""
    return a / b

# ✅ 正确
print(divide(10, 2))  # 5.0

# ❌ 错误：不能使用关键字
# print(divide(a=10, b=2))  # TypeError

# 混合使用
def func(pos_only, /, standard, *, kw_only):
    pass

# pos_only: 仅限位置
# standard: 位置或关键字都可以
# kw_only: 仅限关键字
```

### 2.8 参数解包

```python
# * 解包序列
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # 等同于 add(1, 2, 3)
print(result)  # 6

# ** 解包字典
def greet(name, age, city):
    print(f"{name}, {age}岁, 来自{city}")

info = {"name": "Alice", "age": 25, "city": "北京"}
greet(**info)  # 等同于 greet(name="Alice", age=25, city="北京")

# 混合解包
def func(a, b, c, d, e):
    print(a, b, c, d, e)

args = [1, 2]
kwargs = {"d": 4, "e": 5}
func(*args, 3, **kwargs)  # 1 2 3 4 5
```

---

## 3. 返回值

### 3.1 单个返回值

```python
def square(x):
    return x ** 2

result = square(5)
print(result)  # 25

# 没有 return 语句，默认返回 None
def no_return():
    print("执行中...")

result = no_return()
print(result)  # None
```

### 3.2 多个返回值

```python
# 返回多个值（实际返回元组）
def get_user_info():
    name = "Alice"
    age = 25
    city = "北京"
    return name, age, city

# 接收多个返回值
name, age, city = get_user_info()
print(name, age, city)  # Alice 25 北京

# 也可以作为元组接收
info = get_user_info()
print(info)  # ('Alice', 25, '北京')
print(type(info))  # <class 'tuple'>
```

### 3.3 返回不同类型

```python
def divide_safe(a, b):
    """安全除法，返回结果或错误信息"""
    if b == 0:
        return None, "除数不能为零"
    return a / b, None

# 使用
result, error = divide_safe(10, 2)
if error:
    print(f"错误: {error}")
else:
    print(f"结果: {result}")  # 结果: 5.0

result, error = divide_safe(10, 0)
if error:
    print(f"错误: {error}")  # 错误: 除数不能为零
```

### 3.4 提前返回

```python
def check_age(age):
    """检查年龄是否合法"""
    if age < 0:
        return "年龄不能为负数"
    if age < 18:
        return "未成年"
    if age < 60:
        return "成年人"
    return "老年人"

print(check_age(15))   # 未成年
print(check_age(30))   # 成年人
print(check_age(-5))   # 年龄不能为负数
```

---

## 4. 作用域与命名空间

### 4.1 LEGB 规则

Python 变量查找顺序：**L → E → G → B**

- **L (Local)**: 局部作用域
- **E (Enclosing)**: 嵌套函数的外层作用域
- **G (Global)**: 全局作用域
- **B (Built-in)**: 内置作用域

```python
# B: 内置作用域
print(len([1, 2, 3]))  # len 是内置函数

# G: 全局作用域
x = "全局变量"

def outer():
    # E: 外层函数作用域
    y = "外层变量"
    
    def inner():
        # L: 局部作用域
        z = "局部变量"
        print(z)  # 局部变量
        print(y)  # 外层变量
        print(x)  # 全局变量
    
    inner()

outer()
```

### 4.2 局部变量与全局变量

```python
x = 100  # 全局变量

def func():
    x = 200  # 局部变量（不影响全局变量）
    print(f"函数内: {x}")

func()  # 函数内: 200
print(f"函数外: {x}")  # 函数外: 100
```

### 4.3 global 关键字

```python
count = 0  # 全局变量

def increment():
    global count  # 声明使用全局变量
    count += 1
    print(f"count = {count}")

increment()  # count = 1
increment()  # count = 2
print(count)  # 2

# 不使用 global 会报错
def increment_wrong():
    # count += 1  # UnboundLocalError
    pass
```

### 4.4 nonlocal 关键字

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x  # 声明使用外层函数的变量
        x += 1
        print(f"inner: x = {x}")
    
    inner()  # inner: x = 11
    print(f"outer: x = {x}")  # outer: x = 11

outer()

# 实际应用：计数器
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

### 4.5 命名空间

```python
# 查看局部命名空间
def func():
    a = 1
    b = 2
    print(locals())  # {'a': 1, 'b': 2}

func()

# 查看全局命名空间
x = 100
y = 200
print(globals())  # 包含所有全局变量的字典

# 查看内置命名空间
import builtins
print(dir(builtins))  # 所有内置函数和异常
```

---

## 5. 高阶函数

### 5.1 函数作为参数

```python
def apply_operation(x, y, operation):
    """将操作应用于两个数"""
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(5, 3, add))       # 8
print(apply_operation(5, 3, multiply))  # 15

# 实际应用：排序
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"])
print(sorted_students)
```

### 5.2 函数作为返回值

```python
def make_multiplier(n):
    """返回一个乘法函数"""
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5))  # 10
print(times_3(5))  # 15

# 实际应用：创建验证器
def make_validator(min_value, max_value):
    def validator(value):
        return min_value <= value <= max_value
    return validator

age_validator = make_validator(0, 120)
print(age_validator(25))   # True
print(age_validator(150))  # False
```



### 5.3 内置高阶函数

#### map()

```python
# map(function, iterable) - 对每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# 多个可迭代对象
a = [1, 2, 3]
b = [10, 20, 30]
result = map(lambda x, y: x + y, a, b)
print(list(result))  # [11, 22, 33]

# 实际应用：数据转换
prices = ["10.5", "20.3", "15.8"]
prices_float = list(map(float, prices))
print(prices_float)  # [10.5, 20.3, 15.8]
```

#### filter()

```python
# filter(function, iterable) - 过滤元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6, 8, 10]

# 实际应用：筛选数据
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 58}
]
passed = filter(lambda s: s["score"] >= 60, students)
print(list(passed))
```

#### reduce()

```python
from functools import reduce

# reduce(function, iterable[, initializer]) - 累积计算
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15

# 带初始值
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120

# 实际应用：找最大值
numbers = [3, 7, 2, 9, 1, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # 9
```

---

## 6. Lambda 表达式

### 6.1 Lambda 基础

```python
# 语法：lambda 参数: 表达式

# 普通函数
def add(x, y):
    return x + y

# Lambda 等价形式
add_lambda = lambda x, y: x + y

print(add(3, 5))        # 8
print(add_lambda(3, 5)) # 8

# Lambda 特点：
# 1. 匿名函数（没有名字）
# 2. 只能包含一个表达式
# 3. 自动返回表达式的值
```

### 6.2 Lambda 使用场景

```python
# 1. 作为参数传递
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers, key=lambda x: -x)  # 降序
print(sorted_numbers)  # [9, 8, 5, 2, 1]

# 2. 简单的一次性函数
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])  # 按第二个元素排序
print(pairs)  # [(1, 'one'), (3, 'three'), (2, 'two')]

# 3. 与 map、filter 配合
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

### 6.3 Lambda 的限制

```python
# ❌ 不能包含多条语句
# lambda x: print(x); return x  # SyntaxError

# ❌ 不能包含赋值语句
# lambda x: y = x + 1  # SyntaxError

# ✅ 可以使用条件表达式
abs_lambda = lambda x: x if x >= 0 else -x
print(abs_lambda(-5))  # 5

# ✅ 可以嵌套
outer = lambda x: (lambda y: x + y)
add_5 = outer(5)
print(add_5(3))  # 8
```

### 6.4 Lambda vs 普通函数

```python
# 何时使用 Lambda：
# ✅ 简单的一次性函数
# ✅ 作为参数传递
# ✅ 逻辑简单明了

# 何时使用普通函数：
# ✅ 复杂逻辑
# ✅ 需要文档字符串
# ✅ 需要复用
# ✅ 需要调试

# 示例对比
# Lambda - 适合简单场景
students.sort(key=lambda s: s["score"])

# 普通函数 - 适合复杂场景
def get_student_grade(student):
    """根据分数计算等级"""
    score = student["score"]
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'

students.sort(key=get_student_grade)
```

---

## 7. 装饰器

### 7.0 装饰器工作原理深度解析

#### 什么是装饰器？

装饰器本质上是一个**接受函数作为参数，并返回一个新函数的高阶函数**。它允许我们在不修改原函数代码的情况下，为函数添加额外的功能。

#### 核心概念

```python
# 装饰器的本质
def decorator(func):
    """装饰器函数"""
    def wrapper(*args, **kwargs):
        # 在原函数执行前做些什么
        result = func(*args, **kwargs)
        # 在原函数执行后做些什么
        return result
    return wrapper

# 使用装饰器的两种等价方式
@decorator
def my_function():
    pass

# 等价于：
my_function = decorator(my_function)
```

#### 装饰器的执行流程

```python
def trace(func):
    """追踪函数执行的装饰器"""
    print(f"1. 装饰器 trace 被调用，接收函数: {func.__name__}")
    
    def wrapper(*args, **kwargs):
        print(f"3. wrapper 被调用，参数: {args}, {kwargs}")
        print(f"4. 准备调用原函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"6. 原函数执行完毕，返回值: {result}")
        return result
    
    print(f"2. 装饰器返回 wrapper 函数")
    return wrapper

@trace
def add(a, b):
    print(f"5. add 函数执行中: {a} + {b}")
    return a + b

# 输出:
# 1. 装饰器 trace 被调用，接收函数: add
# 2. 装饰器返回 wrapper 函数

print("=" * 50)
result = add(3, 5)
# 输出:
# 3. wrapper 被调用，参数: (3, 5), {}
# 4. 准备调用原函数: add
# 5. add 函数执行中: 3 + 5
# 6. 原函数执行完毕，返回值: 8

print(f"最终结果: {result}")  # 最终结果: 8
```

**关键点：**
1. **装饰时机**：装饰器在函数定义时就被调用（不是函数调用时）
2. **函数替换**：`@decorator` 会将原函数替换为 `wrapper` 函数
3. **闭包机制**：`wrapper` 通过闭包保持对原函数 `func` 的引用

#### 装饰器的内存模型

```python
def my_decorator(func):
    def wrapper():
        return func()
    return wrapper

@my_decorator
def greet():
    return "Hello!"

# 内存中的变化：
# 1. 定义 greet 函数 → greet 指向原函数对象
# 2. 应用装饰器 → greet = my_decorator(greet)
# 3. 现在 greet 指向 wrapper 函数对象
# 4. wrapper 通过闭包保持对原 greet 函数的引用

print(greet.__name__)  # wrapper（不是 greet！）
print(greet.__closure__)  # 包含对原函数的引用
```

#### 为什么需要 *args 和 **kwargs？

```python
# ❌ 不灵活的装饰器
def bad_decorator(func):
    def wrapper():  # 只能装饰无参数函数
        print("Before")
        result = func()
        print("After")
        return result
    return wrapper

@bad_decorator
def no_args():
    print("No arguments")

no_args()  # ✅ 正常工作

@bad_decorator
def with_args(x, y):
    print(f"x={x}, y={y}")

# with_args(1, 2)  # ❌ TypeError: wrapper() takes 0 positional arguments

# ✅ 灵活的装饰器
def good_decorator(func):
    def wrapper(*args, **kwargs):  # 接受任意参数
        print("Before")
        result = func(*args, **kwargs)  # 传递给原函数
        print("After")
        return result
    return wrapper

@good_decorator
def add(a, b):
    return a + b

print(add(3, 5))  # ✅ 正常工作
```

#### 装饰器的三层结构

```python
# 1. 无参数装饰器（两层）
def simple_decorator(func):           # 第1层：接收函数
    def wrapper(*args, **kwargs):     # 第2层：替换原函数
        return func(*args, **kwargs)
    return wrapper

# 2. 带参数装饰器（三层）
def parametrized_decorator(param):    # 第1层：接收装饰器参数
    def decorator(func):               # 第2层：接收函数
        def wrapper(*args, **kwargs):  # 第3层：替换原函数
            print(f"参数: {param}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@parametrized_decorator("配置")
def my_func():
    pass

# 等价于：
# my_func = parametrized_decorator("配置")(my_func)
#         = decorator(my_func)
#         = wrapper
```

#### 装饰器执行顺序详解

```python
def decorator_a(func):
    print(f"A: 装饰 {func.__name__}")
    def wrapper(*args, **kwargs):
        print("A: 执行前")
        result = func(*args, **kwargs)
        print("A: 执行后")
        return result
    return wrapper

def decorator_b(func):
    print(f"B: 装饰 {func.__name__}")
    def wrapper(*args, **kwargs):
        print("B: 执行前")
        result = func(*args, **kwargs)
        print("B: 执行后")
        return result
    return wrapper

@decorator_a
@decorator_b
def greet():
    print("Hello!")

# 装饰时的输出（从下到上）:
# B: 装饰 greet
# A: 装饰 wrapper

print("=" * 50)
greet()

# 执行时的输出（从上到下）:
# A: 执行前
# B: 执行前
# Hello!
# B: 执行后
# A: 执行后

# 等价于：
# greet = decorator_a(decorator_b(greet))
```

**记忆口诀：装饰从下到上，执行从上到下**

#### functools.wraps 的作用

```python
from functools import wraps

# ❌ 不使用 @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        """wrapper 的文档"""
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

print(greet.__name__)  # wrapper（丢失了原函数名）
print(greet.__doc__)   # wrapper 的文档（丢失了原文档）

# ✅ 使用 @wraps
def good_decorator(func):
    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        """wrapper 的文档"""
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def greet2(name):
    """问候函数"""
    return f"Hello, {name}!"

print(greet2.__name__)  # greet2（保留了原函数名）
print(greet2.__doc__)   # 问候函数（保留了原文档）
```

**@wraps 做了什么？**
```python
# @wraps(func) 等价于：
wrapper.__name__ = func.__name__
wrapper.__doc__ = func.__doc__
wrapper.__module__ = func.__module__
wrapper.__qualname__ = func.__qualname__
wrapper.__annotations__ = func.__annotations__
wrapper.__dict__.update(func.__dict__)
wrapper.__wrapped__ = func  # 保存原函数引用
```

#### 装饰器的常见陷阱

##### 陷阱1：装饰时机

```python
print("模块加载开始")

def decorator(func):
    print(f"装饰器被调用: {func.__name__}")
    return func

@decorator
def func1():
    print("func1 执行")

@decorator
def func2():
    print("func2 执行")

print("模块加载结束")

# 输出:
# 模块加载开始
# 装饰器被调用: func1
# 装饰器被调用: func2
# 模块加载结束

# 注意：装饰器在导入时就执行了，不是在调用函数时！
```

##### 陷阱2：闭包变量

```python
# ❌ 错误：所有装饰器共享同一个变量
def make_decorators():
    decorators = []
    for i in range(3):
        def decorator(func):
            def wrapper():
                print(f"装饰器 {i}")  # 闭包捕获的是变量引用
                return func()
            return wrapper
        decorators.append(decorator)
    return decorators

decs = make_decorators()

@decs[0]
def func1():
    pass

@decs[1]
def func2():
    pass

func1()  # 装饰器 2（不是 0！）
func2()  # 装饰器 2（不是 1！）

# ✅ 正确：使用默认参数固定值
def make_decorators_fixed():
    decorators = []
    for i in range(3):
        def decorator(func, index=i):  # 使用默认参数
            def wrapper():
                print(f"装饰器 {index}")
                return func()
            return wrapper
        decorators.append(decorator)
    return decorators
```

##### 陷阱3：装饰类方法

```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class MyClass:
    @simple_decorator
    def method(self, x):
        return x * 2

obj = MyClass()
print(obj.method(5))  # ✅ 正常工作

# 但是要注意 self 参数
# wrapper 接收的第一个参数是 self
```

#### 装饰器的实际应用场景

```python
# 1. 性能监控
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f}秒")
        return result
    return wrapper

# 2. 日志记录
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} 返回 {result}")
        return result
    return wrapper

# 3. 权限检查
def require_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if permission not in user.get("permissions", []):
                raise PermissionError(f"需要 {permission} 权限")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# 4. 缓存结果
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# 5. 重试机制
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"尝试 {attempt + 1} 失败，重试...")
        return wrapper
    return decorator
```

#### 装饰器设计原则

1. **单一职责**：一个装饰器只做一件事
2. **保留元信息**：始终使用 `@wraps`
3. **通用性**：使用 `*args, **kwargs` 支持任意参数
4. **可组合**：装饰器应该能够叠加使用
5. **文档完善**：说明装饰器的作用和副作用

---

### 7.1 装饰器基础

```python
# 装饰器是一个接受函数并返回新函数的函数
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

# 使用装饰器
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# 函数执行前
# Hello!
# 函数执行后

# 等价于：
# say_hello = my_decorator(say_hello)
```

### 7.2 带参数的装饰器

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回: {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 5)
# 输出:
# 调用 add
# add 返回: 8
```

### 7.3 保留函数元信息

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

print(greet.__name__)  # greet（而不是 wrapper）
print(greet.__doc__)   # 问候函数
```

### 7.4 带参数的装饰器

```python
def repeat(times):
    """重复执行函数的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# Hello!
# Hello!
# Hello!
```

### 7.5 类装饰器

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

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # 调用次数: 1
say_hello()  # 调用次数: 2
say_hello()  # 调用次数: 3
```

### 7.6 常用装饰器示例

```python
import time
from functools import wraps

# 1. 计时装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"

slow_function()  # slow_function 耗时: 1.0001秒

# 2. 缓存装饰器
def cache(func):
    cached_results = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"从缓存获取: {args}")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 55

# 3. 权限检查装饰器
def require_auth(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("需要登录")
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def delete_account(user):
    print(f"删除账户: {user['name']}")

# delete_account({"name": "Alice"})  # PermissionError
delete_account({"name": "Alice", "is_authenticated": True})  # 正常执行
```

### 7.7 多个装饰器

```python
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("装饰器1 - 前")
        result = func(*args, **kwargs)
        print("装饰器1 - 后")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("装饰器2 - 前")
        result = func(*args, **kwargs)
        print("装饰器2 - 后")
        return result
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# 装饰器1 - 前
# 装饰器2 - 前
# Hello!
# 装饰器2 - 后
# 装饰器1 - 后

# 执行顺序：从下到上装饰，从上到下执行
```

---

## 8. 生成器函数

### 8.1 生成器基础

```python
# 使用 yield 关键字的函数是生成器函数
def count_up_to(n):
    """生成 0 到 n-1 的数字"""
    i = 0
    while i < n:
        yield i
        i += 1

# 创建生成器对象
counter = count_up_to(5)
print(type(counter))  # <class 'generator'>

# 逐个获取值
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# 或使用 for 循环
for num in count_up_to(5):
    print(num, end=' ')  # 0 1 2 3 4
```

### 8.2 生成器 vs 列表

```python
# 列表：一次性创建所有元素
def get_numbers_list(n):
    return [i for i in range(n)]

# 生成器：按需生成元素
def get_numbers_generator(n):
    for i in range(n):
        yield i

# 内存对比
import sys
list_obj = get_numbers_list(1000000)
gen_obj = get_numbers_generator(1000000)

print(sys.getsizeof(list_obj))  # 约 8MB
print(sys.getsizeof(gen_obj))   # 约 128 字节

# 生成器的优势：
# 1. 节省内存
# 2. 延迟计算
# 3. 可以表示无限序列
```

### 8.3 生成器表达式

```python
# 类似列表推导式，但使用圆括号
squares_list = [x**2 for x in range(10)]  # 列表
squares_gen = (x**2 for x in range(10))   # 生成器

print(type(squares_list))  # <class 'list'>
print(type(squares_gen))   # <class 'generator'>

# 使用生成器
for square in squares_gen:
    print(square, end=' ')  # 0 1 4 9 16 25 36 49 64 81
```

### 8.4 yield from

```python
# yield from 用于委托给另一个生成器
def generator1():
    yield 1
    yield 2

def generator2():
    yield 3
    yield 4

def combined():
    yield from generator1()
    yield from generator2()

for num in combined():
    print(num, end=' ')  # 1 2 3 4

# 实际应用：展平嵌套列表
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 8.5 生成器的方法

```python
def echo():
    """接收并回显值的生成器"""
    while True:
        value = yield
        if value is not None:
            print(f"收到: {value}")

gen = echo()
next(gen)  # 启动生成器

# send() - 发送值给生成器
gen.send("Hello")   # 收到: Hello
gen.send("World")   # 收到: World

# close() - 关闭生成器
gen.close()

# throw() - 在生成器中抛出异常
def generator_with_exception():
    try:
        while True:
            yield "运行中"
    except ValueError:
        yield "捕获到 ValueError"

gen = generator_with_exception()
print(next(gen))  # 运行中
print(gen.throw(ValueError))  # 捕获到 ValueError
```

### 8.6 实际应用示例

```python
# 1. 读取大文件
def read_large_file(file_path):
    """逐行读取大文件"""
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# 2. 无限序列
def fibonacci():
    """无限斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=' ')  # 0 1 1 2 3 5 8 13 21 34

# 3. 数据管道
def read_data():
    for i in range(10):
        yield i

def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square(numbers):
    for n in numbers:
        yield n ** 2

# 组合管道
pipeline = square(filter_even(read_data()))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

---

## 9. 递归函数

### 9.1 递归基础

```python
# 递归：函数调用自身
def countdown(n):
    """倒计时"""
    if n <= 0:  # 基准情况（终止条件）
        print("发射!")
    else:
        print(n)
        countdown(n - 1)  # 递归调用

countdown(5)
# 输出:
# 5
# 4
# 3
# 2
# 1
# 发射!
```

### 9.2 递归的组成

```python
def factorial(n):
    """计算阶乘"""
    # 1. 基准情况（Base Case）- 终止条件
    if n == 0 or n == 1:
        return 1
    
    # 2. 递归情况（Recursive Case）- 问题分解
    return n * factorial(n - 1)

print(factorial(5))  # 120

# 执行过程：
# factorial(5) = 5 * factorial(4)
#              = 5 * 4 * factorial(3)
#              = 5 * 4 * 3 * factorial(2)
#              = 5 * 4 * 3 * 2 * factorial(1)
#              = 5 * 4 * 3 * 2 * 1
#              = 120
```

### 9.3 经典递归示例

```python
# 1. 斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 2. 二分查找
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(numbers, 7, 0, len(numbers)-1))  # 3

# 3. 树的遍历
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    """中序遍历"""
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.value, end=' ')
    inorder_traversal(node.right)

# 4. 汉诺塔
def hanoi(n, source, target, auxiliary):
    """汉诺塔问题"""
    if n == 1:
        print(f"移动盘子 1 从 {source} 到 {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"移动盘子 {n} 从 {source} 到 {target}")
    hanoi(n-1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
```

### 9.4 递归优化

```python
# 问题：递归可能导致栈溢出
# import sys
# sys.setrecursionlimit(10000)  # 设置递归深度限制

# 1. 尾递归优化（Python 不支持，但可以手动优化）
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# 2. 记忆化（Memoization）
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# 3. 使用装饰器缓存
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# 性能对比
import time

start = time.time()
fibonacci(35)  # 很慢
print(f"普通递归: {time.time() - start:.4f}秒")

start = time.time()
fibonacci_cached(35)  # 很快
print(f"缓存递归: {time.time() - start:.4f}秒")
```

### 9.5 递归 vs 迭代

```python
# 递归版本
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# 迭代版本
def sum_iterative(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# 何时使用递归：
# ✅ 问题本身具有递归性质（树、图）
# ✅ 代码更简洁易懂
# ✅ 数据规模不大

# 何时使用迭代：
# ✅ 性能要求高
# ✅ 数据规模大（避免栈溢出）
# ✅ 空间复杂度要求严格
```



---

## 10. 内置函数详解

### 10.1 数学相关

```python
# abs() - 绝对值
print(abs(-5))      # 5
print(abs(-3.14))   # 3.14

# round() - 四舍五入
print(round(3.14159, 2))  # 3.14
print(round(3.5))         # 4（银行家舍入法）

# pow() - 幂运算
print(pow(2, 3))      # 8
print(pow(2, 3, 5))   # 3（2^3 % 5）

# divmod() - 同时返回商和余数
quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # 3 2

# sum() - 求和
print(sum([1, 2, 3, 4, 5]))        # 15
print(sum([1, 2, 3], 10))          # 16（初始值为10）

# min() / max() - 最小值/最大值
print(min(3, 1, 4, 1, 5))          # 1
print(max([3, 1, 4, 1, 5]))        # 5
print(min("apple", "banana"))      # apple（字典序）
```

### 10.2 类型转换

```python
# int() - 转整数
print(int("123"))       # 123
print(int(3.14))        # 3
print(int("1010", 2))   # 10（二进制转十进制）
print(int("FF", 16))    # 255（十六进制转十进制）

# float() - 转浮点数
print(float("3.14"))    # 3.14
print(float(5))         # 5.0

# str() - 转字符串
print(str(123))         # "123"
print(str([1, 2, 3]))   # "[1, 2, 3]"

# bool() - 转布尔值
print(bool(0))          # False
print(bool(1))          # True
print(bool(""))         # False
print(bool("hello"))    # True

# list() / tuple() / set() - 转换为列表/元组/集合
print(list("hello"))    # ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3])) # (1, 2, 3)
print(set([1, 2, 2, 3])) # {1, 2, 3}

# dict() - 创建字典
print(dict(a=1, b=2))   # {'a': 1, 'b': 2}
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}
```

### 10.3 序列操作

```python
# len() - 长度
print(len([1, 2, 3]))       # 3
print(len("hello"))         # 5
print(len({"a": 1, "b": 2})) # 2

# range() - 生成数字序列
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]

# enumerate() - 枚举（索引和值）
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")
# 0: a
# 1: b
# 2: c

# zip() - 打包多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
# Alice: 25
# Bob: 30
# Charlie: 35

# reversed() - 反转
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# sorted() - 排序
print(sorted([3, 1, 4, 1, 5]))    # [1, 1, 3, 4, 5]
print(sorted([3, 1, 4], reverse=True))  # [4, 3, 1]
```

### 10.4 输入输出

```python
# print() - 打印
print("Hello", "World")              # Hello World
print("Hello", "World", sep="-")     # Hello-World
print("Hello", end="")               # Hello（不换行）
print("World")                       # World

# input() - 获取用户输入
# name = input("请输入姓名: ")
# print(f"你好, {name}!")

# open() - 打开文件
# with open('file.txt', 'r') as f:
#     content = f.read()
```

### 10.5 对象相关

```python
# type() - 获取类型
print(type(123))        # <class 'int'>
print(type("hello"))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

# isinstance() - 检查类型
print(isinstance(123, int))         # True
print(isinstance("hello", str))     # True
print(isinstance([1, 2], (list, tuple)))  # True

# id() - 获取对象的内存地址
a = [1, 2, 3]
print(id(a))  # 例如: 140234567890

# dir() - 查看对象的所有属性和方法
print(dir([]))  # 列表的所有方法

# hasattr() / getattr() / setattr() - 属性操作
class Person:
    name = "Alice"

p = Person()
print(hasattr(p, 'name'))       # True
print(getattr(p, 'name'))       # Alice
setattr(p, 'age', 25)
print(p.age)                    # 25

# callable() - 检查是否可调用
print(callable(print))          # True
print(callable(123))            # False
```

### 10.6 迭代器相关

```python
# iter() - 创建迭代器
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))  # 1
print(next(iterator))  # 2

# next() - 获取下一个元素
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration

# all() - 所有元素为真
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))            # True
print(all([1, 0, 3]))            # False

# any() - 任一元素为真
print(any([False, False, True]))  # True
print(any([False, False, False])) # False
print(any([0, 0, 1]))             # True
```

### 10.7 其他常用函数

```python
# eval() - 执行字符串表达式
result = eval("2 + 3 * 4")
print(result)  # 14

# exec() - 执行字符串代码
code = """
x = 10
y = 20
print(x + y)
"""
exec(code)  # 30

# compile() - 编译代码
code = compile("print('Hello')", "<string>", "exec")
exec(code)  # Hello

# format() - 格式化
print(format(123.456, ".2f"))  # 123.46
print(format(42, "b"))         # 101010（二进制）
print(format(42, "x"))         # 2a（十六进制）

# chr() / ord() - 字符与 ASCII 码转换
print(chr(65))   # A
print(ord('A'))  # 65

# bin() / oct() / hex() - 进制转换
print(bin(10))   # 0b1010
print(oct(10))   # 0o12
print(hex(10))   # 0xa
```

---

## 11. 函数式编程

### 11.1 纯函数

```python
# 纯函数：相同输入总是产生相同输出，无副作用

# ✅ 纯函数
def add(a, b):
    return a + b

# ❌ 非纯函数（有副作用）
total = 0
def add_to_total(x):
    global total
    total += x  # 修改外部状态
    return total

# ❌ 非纯函数（依赖外部状态）
import random
def get_random():
    return random.randint(1, 10)  # 输出不确定
```

### 11.2 不可变性

```python
# 函数式编程倾向于使用不可变数据

# ❌ 修改原数据
def add_item_mutable(lst, item):
    lst.append(item)
    return lst

# ✅ 返回新数据
def add_item_immutable(lst, item):
    return lst + [item]

original = [1, 2, 3]
new_list = add_item_immutable(original, 4)
print(original)  # [1, 2, 3]（未改变）
print(new_list)  # [1, 2, 3, 4]
```

### 11.3 函数组合

```python
# 将多个函数组合成一个函数
def compose(*functions):
    """组合多个函数"""
    def inner(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return inner

# 示例函数
def add_one(x):
    return x + 1

def double(x):
    return x * 2

def square(x):
    return x ** 2

# 组合函数
combined = compose(square, double, add_one)
print(combined(3))  # ((3 + 1) * 2) ** 2 = 64
```

### 11.4 柯里化（Currying）

```python
# 将多参数函数转换为一系列单参数函数
def curry_add(a):
    def add_b(b):
        def add_c(c):
            return a + b + c
        return add_c
    return add_b

result = curry_add(1)(2)(3)
print(result)  # 6

# 实际应用：创建专用函数
def multiply(a):
    return lambda b: a * b

double = multiply(2)
triple = multiply(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### 11.5 偏函数（Partial Application）

```python
from functools import partial

# 固定部分参数
def power(base, exponent):
    return base ** exponent

# 创建平方函数
square = partial(power, exponent=2)
print(square(5))  # 25

# 创建立方函数
cube = partial(power, exponent=3)
print(cube(5))  # 125

# 实际应用：日志函数
def log(level, message):
    print(f"[{level}] {message}")

info = partial(log, "INFO")
error = partial(log, "ERROR")

info("程序启动")    # [INFO] 程序启动
error("发生错误")   # [ERROR] 发生错误
```

---

## 12. 闭包

### 12.1 闭包基础

```python
# 闭包：内部函数引用外部函数的变量
def outer(x):
    def inner(y):
        return x + y  # inner 引用了 outer 的变量 x
    return inner

add_5 = outer(5)
print(add_5(3))  # 8
print(add_5(10)) # 15

# 闭包的特点：
# 1. 内部函数引用外部函数的变量
# 2. 外部函数返回内部函数
# 3. 变量被"记住"
```

### 12.2 闭包的应用

```python
# 1. 数据封装
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

c1 = make_counter()
print(c1())  # 1
print(c1())  # 2

c2 = make_counter()
print(c2())  # 1（独立的计数器）

# 2. 延迟计算
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5))  # 10
print(times_3(5))  # 15

# 3. 回调函数
def make_button_handler(button_id):
    def handler():
        print(f"按钮 {button_id} 被点击")
    return handler

button1_click = make_button_handler(1)
button2_click = make_button_handler(2)

button1_click()  # 按钮 1 被点击
button2_click()  # 按钮 2 被点击
```

### 12.3 闭包陷阱

```python
# 问题：循环中的闭包
functions = []
for i in range(3):
    functions.append(lambda: i)

print([f() for f in functions])  # [2, 2, 2]（都是2！）

# 原因：闭包捕获的是变量引用，不是值
# 解决方案1：使用默认参数
functions = []
for i in range(3):
    functions.append(lambda x=i: x)

print([f() for f in functions])  # [0, 1, 2]

# 解决方案2：使用函数工厂
def make_func(x):
    return lambda: x

functions = []
for i in range(3):
    functions.append(make_func(i))

print([f() for f in functions])  # [0, 1, 2]
```

### 12.4 查看闭包变量

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

func = outer(10)

# 查看闭包变量
print(func.__closure__)  # (<cell at 0x...: int object at 0x...>,)
print(func.__closure__[0].cell_contents)  # 10
```

---

## 13. 函数注解

### 13.1 类型注解

```python
# Python 3.5+ 支持类型注解
def greet(name: str, age: int) -> str:
    """
    问候函数
    
    参数:
        name: 姓名（字符串）
        age: 年龄（整数）
    
    返回:
        问候语（字符串）
    """
    return f"Hello, {name}! You are {age} years old."

print(greet("Alice", 25))

# 查看注解
print(greet.__annotations__)
# {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
```

### 13.2 复杂类型注解

```python
from typing import List, Dict, Tuple, Optional, Union, Callable

# 列表类型
def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

# 字典类型
def get_user_info() -> Dict[str, Union[str, int]]:
    return {"name": "Alice", "age": 25}

# 元组类型
def get_coordinates() -> Tuple[float, float]:
    return (10.5, 20.3)

# 可选类型
def find_user(user_id: int) -> Optional[Dict[str, str]]:
    """返回用户信息或 None"""
    if user_id == 1:
        return {"name": "Alice"}
    return None

# 联合类型
def process_data(data: Union[str, int, List[str]]) -> str:
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return str(data)
    else:
        return ", ".join(data)

# 函数类型
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

### 13.3 自定义注解

```python
# 可以使用任意对象作为注解
def func(x: "这是 x 参数", y: "这是 y 参数") -> "返回值说明":
    return x + y

print(func.__annotations__)
# {'x': '这是 x 参数', 'y': '这是 y 参数', 'return': '返回值说明'}

# 注意：注解不会影响运行时行为
def add(a: int, b: int) -> int:
    return a + b

# 即使传入错误类型也能运行
print(add("hello", "world"))  # helloworld（不会报错）
```

---

## 14. 最佳实践

### 14.1 函数设计原则

```python
# 1. 单一职责原则
# ❌ 函数做太多事情
def process_user_data(user):
    # 验证数据
    if not user.get("name"):
        raise ValueError("缺少姓名")
    # 保存到数据库
    save_to_database(user)
    # 发送邮件
    send_email(user["email"])
    # 记录日志
    log(f"处理用户: {user['name']}")

# ✅ 拆分为多个函数
def validate_user(user):
    if not user.get("name"):
        raise ValueError("缺少姓名")

def save_user(user):
    save_to_database(user)

def notify_user(user):
    send_email(user["email"])

def process_user(user):
    validate_user(user)
    save_user(user)
    notify_user(user)
    log(f"处理用户: {user['name']}")
```

### 14.2 命名规范

```python
# ✅ 好的命名
def calculate_total_price(items):
    pass

def is_valid_email(email):
    pass

def get_user_by_id(user_id):
    pass

# ❌ 不好的命名
def calc(x):  # 太简短
    pass

def function1():  # 无意义
    pass

def do_stuff():  # 太模糊
    pass
```

### 14.3 参数数量

```python
# ❌ 参数太多
def create_user(name, age, email, phone, address, city, country, zipcode):
    pass

# ✅ 使用字典或对象
def create_user(user_info: dict):
    pass

# 或使用 **kwargs
def create_user(**user_info):
    pass

create_user(name="Alice", age=25, email="alice@example.com")
```

### 14.4 返回值一致性

```python
# ❌ 返回类型不一致
def find_user(user_id):
    if user_id == 1:
        return {"name": "Alice"}
    return None  # 有时返回 dict，有时返回 None

# ✅ 返回类型一致
def find_user(user_id):
    if user_id == 1:
        return {"name": "Alice"}
    return {}  # 总是返回 dict
```

### 14.5 错误处理

```python
# ✅ 明确的错误处理
def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# ✅ 使用异常而不是返回错误码
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {filename}")
```

### 14.6 文档字符串

```python
def calculate_bmi(weight: float, height: float) -> float:
    """
    计算身体质量指数（BMI）
    
    BMI = 体重(kg) / 身高(m)²
    
    参数:
        weight (float): 体重，单位：千克
        height (float): 身高，单位：米
    
    返回:
        float: BMI 值
    
    异常:
        ValueError: 当体重或身高为负数时
    
    示例:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if weight <= 0 or height <= 0:
        raise ValueError("体重和身高必须为正数")
    return weight / (height ** 2)
```

### 14.7 性能优化

```python
# 1. 避免重复计算
# ❌ 低效
def process_data(data):
    for item in data:
        if len(data) > 100:  # 每次循环都计算长度
            process_large_data(item)

# ✅ 高效
def process_data(data):
    data_length = len(data)  # 只计算一次
    for item in data:
        if data_length > 100:
            process_large_data(item)

# 2. 使用生成器
# ❌ 内存占用大
def get_squares(n):
    return [i**2 for i in range(n)]

# ✅ 内存友好
def get_squares(n):
    return (i**2 for i in range(n))

# 3. 使用局部变量
import math

# ❌ 低效
def calculate(data):
    result = []
    for x in data:
        result.append(math.sqrt(x))
    return result

# ✅ 高效
def calculate(data):
    sqrt = math.sqrt  # 局部变量
    result = []
    for x in data:
        result.append(sqrt(x))
    return result
```

---

## 总结

### 核心要点

1. **函数基础**
   - 函数定义、调用、文档字符串
   - 参数类型：位置、默认、*args、**kwargs
   - 返回值：单个、多个、None

2. **高级特性**
   - 高阶函数：函数作为参数和返回值
   - Lambda 表达式：简洁的匿名函数
   - 装饰器：增强函数功能
   - 生成器：延迟计算，节省内存

3. **作用域**
   - LEGB 规则
   - global 和 nonlocal 关键字
   - 闭包：捕获外部变量

4. **函数式编程**
   - 纯函数、不可变性
   - map、filter、reduce
   - 函数组合、柯里化

5. **最佳实践**
   - 单一职责原则
   - 清晰的命名
   - 完善的文档
   - 适当的错误处理

### 学习建议

1. **循序渐进**：从基础函数开始，逐步学习高级特性
2. **多写代码**：通过实践加深理解
3. **阅读源码**：学习优秀项目的函数设计
4. **性能意识**：了解不同实现的性能差异
5. **代码审查**：与他人交流，改进代码质量

