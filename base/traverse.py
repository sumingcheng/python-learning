# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.items())
# for key, value in d.items():
#     print(key, value)

# lst = ['a', 'b', 'c']
#
# # 使用enumerate()函数同时遍历列表的索引和元素
# for index, value in enumerate(lst):
#     print(index, value)  # 打印索引和元素

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# print(zip(keys, values))
# for key, value in zip(keys, values):
#     print(key, value)

a = [1, 2, 3]
b = ['a', 'b', 'c']

zipped = zip(a, b)

for pair in zipped:
    print(pair)
