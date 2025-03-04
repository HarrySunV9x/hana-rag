在 Python 中，排序可以通过 sorted() 函数或列表的 sort() 方法实现，支持正序、倒序以及自定义规则排序。以下是不同场景下的具体用法：

一、正序（升序）和倒序（降序）
​1. 默认正序（升序）​
python
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)  # 升序
print(sorted_numbers)  # 输出: [1, 2, 3, 4]
​2. 倒序（降序）​
使用 reverse=True 参数：

python
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # 输出: [4, 3, 2, 1]
二、按字母序排序
​1. 字符串列表按字母序排序
python
fruits = ["banana", "Apple", "Cherry", "date"]
sorted_fruits = sorted(fruits)  # 默认区分大小写（ASCII顺序）
print(sorted_fruits)  # 输出: ['Apple', 'Cherry', 'banana', 'date']
​2. 忽略大小写排序
使用 key=str.lower：

python
sorted_fruits = sorted(fruits, key=str.lower)
print(sorted_fruits)  # 输出: ['Apple', 'banana', 'Cherry', 'date']
三、按自定义规则排序
通过 key 参数指定排序依据的规则，key 是一个函数，作用于每个元素后返回排序的依据值。

​1. 按字符串长度排序
python
words = ["apple", "kiwi", "banana", "pear"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # 输出: ['kiwi', 'pear', 'apple', 'banana']
​2. 按字典的键或值排序
​按字典的键排序：
python
my_dict = {"b": 2, "a": 1, "c": 3}
sorted_by_key = sorted(my_dict.items(), key=lambda x: x[0])
print(sorted_by_key)  # 输出: [('a', 1), ('b', 2), ('c', 3)]
​按字典的值排序：
python
sorted_by_value = sorted(my_dict.items(), key=lambda x: x[1])
print(sorted_by_value)  # 输出: [('a', 1), ('b', 2), ('c', 3)]
​3. 按元组的第二个元素排序
python
tuples = [(1, 5), (3, 2), (2, 8)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # 输出: [(3, 2), (1, 5), (2, 8)]
四、多级排序（多个条件）
通过 key 返回一个元组，依次按多条件排序。

​示例：先按字符串长度排序，长度相同再按字母序排序。
python
words = ["apple", "kiwi", "banana", "pear"]
sorted_words = sorted(words, key=lambda x: (len(x), x.lower()))
print(sorted_words)  # 输出: ['kiwi', 'pear', 'apple', 'banana']
五、稳定排序（保持相同键元素的原始顺序）
Python 的排序是稳定的，即当两个元素排序键相同时，它们的相对顺序与原列表一致。

​示例：
python
data = [("a", 2), ("b", 1), ("a", 1)]
sorted_data = sorted(data, key=lambda x: x[0])  # 按第一个元素排序
print(sorted_data)  # 输出: [('a', 2), ('a', 1), ('b', 1)]（两个 "a" 保持原顺序）
六、原地排序 vs 生成新列表
​1. sorted()
生成新列表，不修改原对象。
适用于所有可迭代对象（列表、元组、字符串等）。
​2. list.sort()
原地修改列表，返回 None。
仅适用于列表。
​示例：
python
numbers = [3, 1, 4, 2]
numbers.sort()  # 原地排序
print(numbers)  # 输出: [1, 2, 3, 4]
七、总结
​场景​	​代码示例​
正序（升序）	sorted(list) 或 list.sort()
倒序（降序）	sorted(list, reverse=True) 或 list.sort(reverse=True)
按字符串长度排序	sorted(list, key=lambda x: len(x))
按字典值排序	sorted(dict.items(), key=lambda x: x[1])
多级排序	sorted(list, key=lambda x: (条件1, 条件2))
忽略大小写排序	sorted(list, key=str.lower)
通过灵活使用 key 和 reverse 参数，可以覆盖绝大多数排序需求！