# Python3 Set 练习题

## 基础题 (10题)

### 1. 创建集合
创建一个包含 1 到 5 的集合,并打印出来。

<details>
<summary>点击查看答案</summary>

```python
# 方法1: 直接创建
s = {1, 2, 3, 4, 5}
print(s)  # {1, 2, 3, 4, 5}

# 方法2: 使用 set()
s = set([1, 2, 3, 4, 5])
print(s)  # {1, 2, 3, 4, 5}

# 方法3: 使用 range
s = set(range(1, 6))
print(s)  # {1, 2, 3, 4, 5}
```
</details>

---

### 2. 自动去重
创建一个包含重复元素的列表 `[1, 2, 2, 3, 3, 3, 4]`,使用集合去重。

<details>
<summary>点击查看答案</summary>

```python
my_list = [1, 2, 2, 3, 3, 3, 4]

# 转换为集合自动去重
unique_set = set(my_list)
print(unique_set)  # {1, 2, 3, 4}

# 转回列表
unique_list = list(unique_set)
print(unique_list)  # [1, 2, 3, 4] (顺序可能不同)
```
</details>

---

### 3. 添加元素
创建集合 `s = {1, 2, 3}`,添加元素 4 和 5。

<details>
<summary>点击查看答案</summary>

```python
s = {1, 2, 3}

# 方法1: add() 逐个添加
s.add(4)
s.add(5)
print(s)  # {1, 2, 3, 4, 5}

# 方法2: update() 批量添加
s = {1, 2, 3}
s.update([4, 5])
print(s)  # {1, 2, 3, 4, 5}
```
</details>

---

### 4. 删除元素
创建集合 `s = {1, 2, 3, 4, 5}`,删除元素 3。

<details>
<summary>点击查看答案</summary>

```python
s = {1, 2, 3, 4, 5}

# 方法1: remove() (不存在会报错)
s.remove(3)
print(s)  # {1, 2, 4, 5}

# 方法2: discard() (不存在不报错)
s = {1, 2, 3, 4, 5}
s.discard(3)
print(s)  # {1, 2, 4, 5}

# discard 的安全性
s.discard(10)  # 不报错
print(s)  # {1, 2, 4, 5}
```
</details>

---

### 5. 成员检查
创建集合 `s = {1, 2, 3, 4, 5}`,检查 3 和 10 是否在集合中。

<details>
<summary>点击查看答案</summary>

```python
s = {1, 2, 3, 4, 5}

print(3 in s)   # True
print(10 in s)  # False
print(10 not in s)  # True
```
</details>

---

### 6. 集合长度
创建集合 `s = {1, 2, 3, 4, 5}`,获取集合的长度。

<details>
<summary>点击查看答案</summary>

```python
s = {1, 2, 3, 4, 5}
print(len(s))  # 5

# 空集合
empty = set()
print(len(empty))  # 0
```
</details>

---

### 7. 并集运算
给定 `a = {1, 2, 3}` 和 `b = {3, 4, 5}`,计算并集。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3}
b = {3, 4, 5}

# 方法1: | 运算符
print(a | b)  # {1, 2, 3, 4, 5}

# 方法2: union() 方法
print(a.union(b))  # {1, 2, 3, 4, 5}
```
</details>

---

### 8. 交集运算
给定 `a = {1, 2, 3, 4}` 和 `b = {3, 4, 5, 6}`,计算交集。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 方法1: & 运算符
print(a & b)  # {3, 4}

# 方法2: intersection() 方法
print(a.intersection(b))  # {3, 4}
```
</details>

---

### 9. 差集运算
给定 `a = {1, 2, 3, 4}` 和 `b = {3, 4, 5, 6}`,计算 a-b 和 b-a。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# a - b (a中有但b中没有)
print(a - b)  # {1, 2}
print(a.difference(b))  # {1, 2}

# b - a (b中有但a中没有)
print(b - a)  # {5, 6}
print(b.difference(a))  # {5, 6}
```
</details>

---

### 10. 对称差集
给定 `a = {1, 2, 3}` 和 `b = {3, 4, 5}`,计算对称差集。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3}
b = {3, 4, 5}

# 方法1: ^ 运算符
print(a ^ b)  # {1, 2, 4, 5}

# 方法2: symmetric_difference() 方法
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# 等价于
print((a - b) | (b - a))  # {1, 2, 4, 5}
```
</details>

---

## 进阶题 (10题)

### 11. 子集判断
判断 `{1, 2}` 是否是 `{1, 2, 3, 4}` 的子集。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2}
b = {1, 2, 3, 4}

# 方法1: <= 运算符
print(a <= b)  # True

# 方法2: issubset() 方法
print(a.issubset(b))  # True

# 真子集(不相等)
print(a < b)  # True
print(a < a)  # False
```
</details>

---

### 12. 超集判断
判断 `{1, 2, 3, 4}` 是否是 `{1, 2}` 的超集。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3, 4}
b = {1, 2}

# 方法1: >= 运算符
print(a >= b)  # True

# 方法2: issuperset() 方法
print(a.issuperset(b))  # True

# 真超集
print(a > b)  # True
```
</details>

---

### 13. 不相交判断
判断 `{1, 2, 3}` 和 `{4, 5, 6}` 是否不相交。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

# isdisjoint() 方法
print(a.isdisjoint(b))  # True (没有交集)
print(a.isdisjoint(c))  # False (有交集3)
```
</details>

---

### 14. 集合推导式
使用集合推导式创建 1-10 中所有偶数的集合。

<details>
<summary>点击查看答案</summary>

```python
# 方法1: 集合推导式
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)  # {2, 4, 6, 8, 10}

# 方法2: 直接用 range
evens = set(range(2, 11, 2))
print(evens)  # {2, 4, 6, 8, 10}
```
</details>

---

### 15. 字符串去重
给定字符串 `"hello world"`,统计其中有多少个不同的字符。

<details>
<summary>点击查看答案</summary>

```python
text = "hello world"

# 转换为集合自动去重
unique_chars = set(text)
print(unique_chars)  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
print(f"不同字符数: {len(unique_chars)}")  # 8

# 去除空格
unique_chars = set(text.replace(' ', ''))
print(f"不同字母数: {len(unique_chars)}")  # 7
```
</details>

---

### 16. 查找共同元素
给定两个列表 `list1 = [1, 2, 3, 4, 5]` 和 `list2 = [4, 5, 6, 7, 8]`,找出共同元素。

<details>
<summary>点击查看答案</summary>

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# 转换为集合求交集
common = set(list1) & set(list2)
print(common)  # {4, 5}

# 转回列表
common_list = list(common)
print(common_list)  # [4, 5]
```
</details>

---

### 17. 查找唯一元素
给定两个列表,找出只在第一个列表中出现的元素。

<details>
<summary>点击查看答案</summary>

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# 差集
unique_to_list1 = set(list1) - set(list2)
print(unique_to_list1)  # {1, 2, 3}

# 所有唯一元素(对称差集)
all_unique = set(list1) ^ set(list2)
print(all_unique)  # {1, 2, 3, 6, 7, 8}
```
</details>

---

### 18. 原地修改
创建集合 `a = {1, 2, 3}`,使用原地修改方法添加集合 `b = {3, 4, 5}` 的元素。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3}
b = {3, 4, 5}

# update() - 原地并集
a.update(b)
print(a)  # {1, 2, 3, 4, 5}

# 其他原地修改方法
a = {1, 2, 3}
a |= b  # 等价于 a.update(b)
print(a)  # {1, 2, 3, 4, 5}
```
</details>

---

### 19. frozenset
创建一个 frozenset 并尝试修改它。

<details>
<summary>点击查看答案</summary>

```python
# 创建 frozenset
fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})
print(type(fs))  # <class 'frozenset'>

# 不可修改
try:
    fs.add(4)
except AttributeError as e:
    print(f"错误: frozenset 不可修改")

# 可以进行集合运算
fs2 = frozenset([3, 4, 5])
print(fs | fs2)  # frozenset({1, 2, 3, 4, 5})

# 可以作为字典键
d = {fs: 'value'}
print(d[fs])  # 'value'
```
</details>

---

### 20. 多集合运算
给定三个集合,找出它们的交集。

<details>
<summary>点击查看答案</summary>

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = {4, 5, 7, 8, 9}

# 方法1: 连续运算
intersection = a & b & c
print(intersection)  # {4, 5}

# 方法2: intersection() 方法
intersection = a.intersection(b, c)
print(intersection)  # {4, 5}
```
</details>

---

## 挑战题 (10题)

### 21. 统计唯一单词
编写函数 `count_unique_words(text)`,统计文本中有多少个不同的单词(不区分大小写)。

<details>
<summary>点击查看答案</summary>

```python
def count_unique_words(text):
    # 转小写并分割
    words = text.lower().split()
    # 使用集合去重
    return len(set(words))

# 测试
text = "Hello world hello Python python world"
print(count_unique_words(text))  # 3 (hello, world, python)

# 更严格的版本(去除标点)
import string

def count_unique_words_v2(text):
    # 去除标点
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    return len(set(words))

text2 = "Hello, world! Hello Python. Python, world."
print(count_unique_words_v2(text2))  # 3
```
</details>

---

### 22. 查找重复元素
编写函数 `find_duplicates(lst)`,返回列表中所有重复的元素(作为集合)。

<details>
<summary>点击查看答案</summary>

```python
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return duplicates

# 测试
lst = [1, 2, 3, 2, 4, 5, 3, 6]
print(find_duplicates(lst))  # {2, 3}

# 方法2: 使用 Counter
from collections import Counter

def find_duplicates_v2(lst):
    counts = Counter(lst)
    return {item for item, count in counts.items() if count > 1}

print(find_duplicates_v2(lst))  # {2, 3}
```
</details>

---

### 23. 集合的幂集
编写函数 `powerset(s)`,返回集合的所有子集(幂集)。

<details>
<summary>点击查看答案</summary>

```python
from itertools import combinations

def powerset(s):
    result = []
    s_list = list(s)
    
    # 生成所有长度的组合
    for i in range(len(s_list) + 1):
        for combo in combinations(s_list, i):
            result.append(set(combo))
    
    return result

# 测试
s = {1, 2, 3}
ps = powerset(s)
for subset in ps:
    print(subset)

# 输出:
# set()
# {1}
# {2}
# {3}
# {1, 2}
# {1, 3}
# {2, 3}
# {1, 2, 3}

print(f"幂集大小: {len(ps)}")  # 8 (2^3)
```
</details>

---

### 24. 判断是否为回文
编写函数 `is_anagram(s1, s2)`,判断两个字符串是否为字母异位词(包含相同字母但顺序不同)。

<details>
<summary>点击查看答案</summary>

```python
def is_anagram(s1, s2):
    # 去除空格并转小写
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # 比较字符集合和长度
    return set(s1) == set(s2) and len(s1) == len(s2)

# 测试
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
print(is_anagram("Dormitory", "Dirty room"))  # True

# 更准确的方法(使用 Counter)
from collections import Counter

def is_anagram_v2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return Counter(s1) == Counter(s2)

print(is_anagram_v2("aab", "aba"))  # True
```
</details>

---

### 25. 集合分区
编写函数 `partition(s, predicate)`,将集合分为满足条件和不满足条件的两个集合。

<details>
<summary>点击查看答案</summary>

```python
def partition(s, predicate):
    true_set = set()
    false_set = set()
    
    for item in s:
        if predicate(item):
            true_set.add(item)
        else:
            false_set.add(item)
    
    return true_set, false_set

# 测试
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 分为偶数和奇数
evens, odds = partition(numbers, lambda x: x % 2 == 0)
print(f"偶数: {evens}")  # {2, 4, 6, 8, 10}
print(f"奇数: {odds}")   # {1, 3, 5, 7, 9}

# 分为大于5和小于等于5
greater, less_equal = partition(numbers, lambda x: x > 5)
print(f">5: {greater}")    # {6, 7, 8, 9, 10}
print(f"<=5: {less_equal}") # {1, 2, 3, 4, 5}
```
</details>

---

### 26. 笛卡尔积
编写函数 `cartesian_product(a, b)`,返回两个集合的笛卡尔积(作为元组集合)。

<details>
<summary>点击查看答案</summary>

```python
def cartesian_product(a, b):
    return {(x, y) for x in a for y in b}

# 测试
a = {1, 2, 3}
b = {'a', 'b'}
result = cartesian_product(a, b)
print(result)
# {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')}

# 使用 itertools
from itertools import product

def cartesian_product_v2(a, b):
    return set(product(a, b))

print(cartesian_product_v2(a, b))
```
</details>

---

### 27. 对称差集链
给定多个集合,计算它们的对称差集链(依次计算对称差集)。

<details>
<summary>点击查看答案</summary>

```python
def symmetric_difference_chain(*sets):
    if not sets:
        return set()
    
    result = sets[0]
    for s in sets[1:]:
        result ^= s
    
    return result

# 测试
a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}

result = symmetric_difference_chain(a, b, c)
print(result)  # {1, 2, 4, 6, 7}

# 验证
print((a ^ b) ^ c)  # {1, 2, 4, 6, 7}
```
</details>

---

### 28. 集合相等性
编写函数判断两个集合列表是否包含相同的集合(忽略顺序)。

<details>
<summary>点击查看答案</summary>

```python
def sets_equal(list1, list2):
    # 转换为 frozenset 的集合进行比较
    set1 = {frozenset(s) for s in list1}
    set2 = {frozenset(s) for s in list2}
    return set1 == set2

# 测试
list1 = [{1, 2}, {3, 4}, {5, 6}]
list2 = [{5, 6}, {1, 2}, {3, 4}]  # 顺序不同
list3 = [{1, 2}, {3, 4}, {7, 8}]  # 内容不同

print(sets_equal(list1, list2))  # True
print(sets_equal(list1, list3))  # False
```
</details>

---

### 29. 最大公共子集
编写函数 `max_common_subset(*sets)`,找出所有集合的最大公共子集。

<details>
<summary>点击查看答案</summary>

```python
def max_common_subset(*sets):
    if not sets:
        return set()
    
    # 所有集合的交集
    result = sets[0]
    for s in sets[1:]:
        result &= s
    
    return result

# 测试
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = {4, 5, 7, 8, 9}

common = max_common_subset(a, b, c)
print(common)  # {4, 5}

# 使用 set.intersection
def max_common_subset_v2(*sets):
    if not sets:
        return set()
    return set.intersection(*sets)

print(max_common_subset_v2(a, b, c))  # {4, 5}
```
</details>

---

### 30. 集合覆盖问题
给定一个全集和多个子集,找出最少需要多少个子集才能覆盖全集(贪心算法)。

<details>
<summary>点击查看答案</summary>

```python
def set_cover(universe, subsets):
    """
    贪心算法求解集合覆盖问题
    """
    universe = set(universe)
    subsets = [set(s) for s in subsets]
    covered = set()
    selected = []
    
    while covered != universe:
        # 选择覆盖最多未覆盖元素的子集
        best_subset = max(subsets, key=lambda s: len(s - covered))
        
        if len(best_subset - covered) == 0:
            # 无法完全覆盖
            return None
        
        covered |= best_subset
        selected.append(best_subset)
        subsets.remove(best_subset)
    
    return selected

# 测试
universe = {1, 2, 3, 4, 5, 6, 7, 8}
subsets = [
    {1, 2, 3},
    {2, 4, 5},
    {5, 6, 7},
    {1, 4, 7, 8}
]

result = set_cover(universe, subsets)
print(f"需要 {len(result)} 个子集:")
for s in result:
    print(s)

# 输出:
# 需要 3 个子集:
# {1, 4, 7, 8}
# {2, 4, 5}
# {5, 6, 7}
```
</details>

---

## 综合应用题 (5题)

### 31. 学生选课系统
设计一个学生选课系统,实现以下功能:
- 添加/删除课程
- 查找选了某门课的所有学生
- 查找两个学生的共同课程
- 查找某学生还没选的课程

<details>
<summary>点击查看答案</summary>

```python
class CourseSystem:
    def __init__(self):
        # 学生 -> 课程集合
        self.student_courses = {}
        # 所有课程
        self.all_courses = set()
    
    def add_course(self, student, course):
        """学生选课"""
        if student not in self.student_courses:
            self.student_courses[student] = set()
        self.student_courses[student].add(course)
        self.all_courses.add(course)
    
    def remove_course(self, student, course):
        """学生退课"""
        if student in self.student_courses:
            self.student_courses[student].discard(course)
    
    def get_students_in_course(self, course):
        """查找选了某门课的学生"""
        return {student for student, courses in self.student_courses.items()
                if course in courses}
    
    def get_common_courses(self, student1, student2):
        """查找两个学生的共同课程"""
        courses1 = self.student_courses.get(student1, set())
        courses2 = self.student_courses.get(student2, set())
        return courses1 & courses2
    
    def get_remaining_courses(self, student):
        """查找学生还没选的课程"""
        selected = self.student_courses.get(student, set())
        return self.all_courses - selected

# 测试
system = CourseSystem()

# 添加课程
system.add_course('Alice', 'Math')
system.add_course('Alice', 'Physics')
system.add_course('Bob', 'Math')
system.add_course('Bob', 'Chemistry')
system.add_course('Charlie', 'Physics')

# 查询
print(system.get_students_in_course('Math'))  # {'Alice', 'Bob'}
print(system.get_common_courses('Alice', 'Bob'))  # {'Math'}
print(system.get_remaining_courses('Alice'))  # {'Chemistry'}
```
</details>

---

### 32. 社交网络好友推荐
实现一个简单的好友推荐系统:推荐与用户有共同好友但还不是好友的人。

<details>
<summary>点击查看答案</summary>

```python
class SocialNetwork:
    def __init__(self):
        # 用户 -> 好友集合
        self.friends = {}
    
    def add_friendship(self, user1, user2):
        """添加好友关系(双向)"""
        if user1 not in self.friends:
            self.friends[user1] = set()
        if user2 not in self.friends:
            self.friends[user2] = set()
        
        self.friends[user1].add(user2)
        self.friends[user2].add(user1)
    
    def recommend_friends(self, user):
        """推荐好友"""
        if user not in self.friends:
            return set()
        
        user_friends = self.friends[user]
        recommendations = set()
        
        # 遍历好友的好友
        for friend in user_friends:
            for friend_of_friend in self.friends.get(friend, set()):
                # 不是自己,也不是已有好友
                if friend_of_friend != user and friend_of_friend not in user_friends:
                    recommendations.add(friend_of_friend)
        
        return recommendations
    
    def get_mutual_friends(self, user1, user2):
        """获取共同好友"""
        friends1 = self.friends.get(user1, set())
        friends2 = self.friends.get(user2, set())
        return friends1 & friends2

# 测试
network = SocialNetwork()

# 建立好友关系
network.add_friendship('Alice', 'Bob')
network.add_friendship('Alice', 'Charlie')
network.add_friendship('Bob', 'David')
network.add_friendship('Charlie', 'David')

# 推荐好友
print(network.recommend_friends('Alice'))  # {'David'}
print(network.get_mutual_friends('Bob', 'Charlie'))  # {'Alice'}
```
</details>

---

### 33. 文本相似度计算
使用 Jaccard 相似度计算两个文本的相似度(基于单词集合)。

<details>
<summary>点击查看答案</summary>

```python
def jaccard_similarity(text1, text2):
    """
    计算 Jaccard 相似度
    公式: |A ∩ B| / |A ∪ B|
    """
    # 转换为单词集合
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    # 交集和并集
    intersection = words1 & words2
    union = words1 | words2
    
    if len(union) == 0:
        return 0.0
    
    return len(intersection) / len(union)

# 测试
text1 = "I love Python programming"
text2 = "I love Java programming"
text3 = "The weather is nice today"

print(f"相似度(1-2): {jaccard_similarity(text1, text2):.2f}")  # 0.75
print(f"相似度(1-3): {jaccard_similarity(text1, text3):.2f}")  # 0.00

# 更复杂的版本(去除标点,停用词)
import string

def jaccard_similarity_advanced(text1, text2, stop_words=None):
    if stop_words is None:
        stop_words = {'the', 'is', 'a', 'an', 'and', 'or', 'but'}
    
    # 去除标点
    translator = str.maketrans('', '', string.punctuation)
    text1 = text1.translate(translator)
    text2 = text2.translate(translator)
    
    # 转换为单词集合并去除停用词
    words1 = set(text1.lower().split()) - stop_words
    words2 = set(text2.lower().split()) - stop_words
    
    intersection = words1 & words2
    union = words1 | words2
    
    return len(intersection) / len(union) if union else 0.0

text4 = "The cat is on the mat"
text5 = "A dog is on the floor"
print(f"高级相似度: {jaccard_similarity_advanced(text4, text5):.2f}")
```
</details>

---

### 34. 权限管理系统
实现一个基于角色的权限管理系统(RBAC)。

<details>
<summary>点击查看答案</summary>

```python
class PermissionSystem:
    def __init__(self):
        # 角色 -> 权限集合
        self.role_permissions = {}
        # 用户 -> 角色集合
        self.user_roles = {}
    
    def add_role(self, role, permissions):
        """添加角色及其权限"""
        self.role_permissions[role] = set(permissions)
    
    def assign_role(self, user, role):
        """给用户分配角色"""
        if user not in self.user_roles:
            self.user_roles[user] = set()
        self.user_roles[user].add(role)
    
    def get_user_permissions(self, user):
        """获取用户的所有权限"""
        if user not in self.user_roles:
            return set()
        
        permissions = set()
        for role in self.user_roles[user]:
            permissions |= self.role_permissions.get(role, set())
        
        return permissions
    
    def has_permission(self, user, permission):
        """检查用户是否有某权限"""
        return permission in self.get_user_permissions(user)
    
    def get_missing_permissions(self, user, required_permissions):
        """获取用户缺少的权限"""
        user_perms = self.get_user_permissions(user)
        return set(required_permissions) - user_perms

# 测试
system = PermissionSystem()

# 定义角色和权限
system.add_role('admin', ['read', 'write', 'delete', 'execute'])
system.add_role('editor', ['read', 'write'])
system.add_role('viewer', ['read'])

# 分配角色
system.assign_role('Alice', 'admin')
system.assign_role('Bob', 'editor')
system.assign_role('Bob', 'viewer')  # 可以有多个角色

# 检查权限
print(system.get_user_permissions('Alice'))  # {'read', 'write', 'delete', 'execute'}
print(system.get_user_permissions('Bob'))    # {'read', 'write'}
print(system.has_permission('Bob', 'delete'))  # False

# 检查缺少的权限
required = ['read', 'write', 'delete']
missing = system.get_missing_permissions('Bob', required)
print(f"Bob 缺少的权限: {missing}")  # {'delete'}
```
</details>

---

### 35. 标签推荐系统
基于用户浏览历史的标签,推荐相关内容。

<details>
<summary>点击查看答案</summary>

```python
class TagRecommendation:
    def __init__(self):
        # 内容 -> 标签集合
        self.content_tags = {}
        # 用户 -> 浏览过的内容集合
        self.user_history = {}
    
    def add_content(self, content_id, tags):
        """添加内容及其标签"""
        self.content_tags[content_id] = set(tags)
    
    def add_history(self, user, content_id):
        """记录用户浏览历史"""
        if user not in self.user_history:
            self.user_history[user] = set()
        self.user_history[user].add(content_id)
    
    def get_user_interests(self, user):
        """获取用户感兴趣的标签"""
        if user not in self.user_history:
            return set()
        
        interests = set()
        for content_id in self.user_history[user]:
            interests |= self.content_tags.get(content_id, set())
        
        return interests
    
    def recommend(self, user, top_n=5):
        """推荐内容"""
        user_interests = self.get_user_interests(user)
        viewed = self.user_history.get(user, set())
        
        # 计算每个内容的相关度
        scores = {}
        for content_id, tags in self.content_tags.items():
            if content_id not in viewed:
                # 相关度 = 共同标签数
                score = len(user_interests & tags)
                if score > 0:
                    scores[content_id] = score
        
        # 按分数排序
        recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [content_id for content_id, score in recommended[:top_n]]

# 测试
system = TagRecommendation()

# 添加内容
system.add_content('article1', ['python', 'programming', 'tutorial'])
system.add_content('article2', ['python', 'data-science', 'pandas'])
system.add_content('article3', ['javascript', 'web', 'tutorial'])
system.add_content('article4', ['python', 'machine-learning', 'ai'])
system.add_content('article5', ['java', 'programming', 'oop'])

# 用户浏览历史
system.add_history('Alice', 'article1')
system.add_history('Alice', 'article2')

# 推荐
print(system.get_user_interests('Alice'))  # {'python', 'programming', 'tutorial', 'data-science', 'pandas'}
print(system.recommend('Alice', top_n=3))  # ['article4', 'article3', 'article5']
```
</details>

---

## 学习建议

1. **理解集合特性** - 无序、不重复、快速查找
2. **掌握集合运算** - 并、交、差、对称差
3. **活用集合去重** - 这是最常见的应用
4. **注意性能优势** - 成员检查 O(1) vs 列表 O(n)
5. **实践应用** - 在实际项目中使用集合

祝学习愉快! 🎉
