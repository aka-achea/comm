# !/usr/bin/python3
# coding:utf-8

from pprint import pprint


# 检查内存使用情况
import sys    
variable = 20     
print(sys.getsizeof(variable)) # 24

# 每个词进行首字母大写
s = "programming is awesome"    
print(s.title())

# 删除列表中的错误值（如：False, None, 0 和“”）
def compact(lst):    
    return list(filter(bool, lst))    
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]


# 间隔数
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]    
transposed = zip(*array)    
pprint(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]


# 链式比较
a = 3    
print( 2 < a < 8) # True    
print(1 == a < 2) # False

# 合并两个词典
def merge_dictionaries(a, b):
   return {**a, **b}
a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}


# 查找最常见元素
def most_frequent(list):
    return max(set(list), key = list.count)

list = [1,2,1,2,3,2,1,4,2]
print(most_frequent(list))


# 列表扁平化
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]