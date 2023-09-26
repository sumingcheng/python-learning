#!/usr/bin/python3

# import keyword
# print(keyword.kwlist)

# if True:
#     print("This is true.")
#
#     for i in range(5):
#         print(i)


# user_input = input("Please enter something: ")
# print(f"You entered: {user_input}")

# 代码组
# for i in range(5):
#     print(i)
#     print("Inside the for loop")
# print("Outside of the for loop")

# print(True + 4)  # 输出 5，因为 True 被当作 1
# print(False * 3)  # 输出 0，因为 False 被当作 0

# a, b, c, d = 20, 5.5, True, 4 + 3j
#
# print(type(a), type(b), type(c), type(d))

# class MyBaseList(list):
#     pass
#
#
# x = MyBaseList()
# print(isinstance(x, MyBaseList))  # 输出 True
# print(isinstance(x, list))  # 输出 True
# print(isinstance(x, (list, dict)))  # 输出 True，因为 x 是 list 或 dict 的实例


# name = "Alice"
# age = 30
# formatted1 = "My name is %s and I am %d years old." % (name, age)
# formatted2 = "My name is {} and I am {} years old.".format(name, age)
# formatted3 = f"My name is {name} and I am {age} years old."
#
# print(formatted1, formatted2, formatted3, sep="\n")

# result = 5 > 3  # True，因为 5 确实大于 3
# another_result = 5 == 6  # False，因为 5 不等于 6
#
# print(result, another_result, sep="\n")

# print(type(list(range(5))))

# import array
#
# # 创建一个整数数组
# # 第一个参数 'i' 指示这是一个整数数组
# my_array = array.array('i', [1, 2, 3, 4, 5])
#
# # 添加元素到数组
# my_array.append(6)
#
# # 修改数组中的元素
# my_array[0] = 7
#
# print(my_array)  # 输出 array('i', [7, 2, 3, 4, 5, 6])

# 注意：你不能在这个整数数组中添加一个字符串或其他非整数类型
# 以下操作会引发错误
# my_array.append("Hello")  # TypeError: an integer is required (got type str)


# list = [1, 2, 3, 4, 5, "a", "b", "c"]
#
# print(list[0:5:2])  # 输出 [1, 3, 5]


# 定义一个包含商品信息的列表，每个商品是一个字典，包含名称和类别
products = [
    {"name": "apple", "category": "fruit"},
    {"name": "broccoli", "category": "vegetable"},
    {"name": "banana", "category": "fruit"},
]

# 初始化一个空字典，用于存储分组后的商品
grouped_products = {}

# 遍历每个商品
# for product in products:
#     # 检查商品的类别是否已经作为键存在于 grouped_products 字典中
#     if product["category"] not in grouped_products:
#         # 如果不存在，为该类别创建一个新的空列表
#         grouped_products[product["category"]] = []
#     # 将商品的名称添加到相应类别的列表中
#     grouped_products[product["category"]].append(product["name"])
#
# # 打印分组后的商品
# print(grouped_products)  # 输出: {'fruit': ['apple', 'banana'], 'vegetable': ['broccoli']}

with open('mini.jpg', 'rb') as file:  # 注意 'rb' 模式表示二进制读取
    data = file.read()
    print(type(data))  # 输出: <class 'bytes'>
